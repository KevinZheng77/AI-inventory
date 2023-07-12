const express = require('express');
const router = express.Router();
const User = require('../Models/UserModel');
const bcrypt = require('bcryptjs');
const validateRegisterInput = require("./Validation/Validate");
const jsonwebtoken = require('jsonwebtoken');
const requireAuth = require('../middleware/permission');
const cors = require("cors");
const app = express();
app.use(cors());
// @route GET  /api/auth/test
// @desc  Test the auth route
// @access Public
router.get('/test', (req, res) =>{
    res.send('Authentication route is working')
});

// @route POST  /api/auth/test
// @desc  Creating a new user
// @access Public
router.post("/register", async (req, res) =>{
    try{
        // uses destructuring to get errors and isValid from the function
        const {errors, isValid} = validateRegisterInput(req.body);
        if(isValid == false){
            return res.status(400).json(errors);
        }

        // checks for existing user
        // the i checks for case sensitivity
        const existingEmail = await User.findOne({email: new RegExp("^" + req.body.email + "$", "i")})

        if(existingEmail == true){
            return res.status(400).json({ error: 'User already exists'})
        }

        //hashes the password
        const hashedPassword = await bcrypt.hash(req.body.password, 12);

        //create a new user
        const newUser = new User({
            email: req.body.email,
            password: hashedPassword,
            name: req.body.name,
        });

        //save the user to the database
        const savedUser = await newUser.save();

        //makes sure that the response does not return the hashed password
        const returnUser = {...savedUser._doc};
        delete returnUser.password;
        //returns the new user
        return res.json(returnUser);
    } catch(error){
        console.log(error);
        res.status(500).send(error.message);
    }
})

// @route POST  /api/auth/login
// @desc  Creating a new user
// @access Public
router.post("/login", async(req, res) =>{
    try{
        //checks if the user exists
        const user = await User.findOne({
            email: new RegExp("^" + req.body.email + "$", "i"),
        })
        // does not find user
        if(!user){
            return res.status(400).json({error: "User does not exist"});
        }

        //returns true if passwords match returns false if it does not
        const passwordMatch = await bcrypt.compare(req.body.password, user.password);

        //passwords do not match
        if(!passwordMatch){
            return res.status(400).json({error: "User does not exist"});
        };

        const payload = {userId: user._id};
        const token = jsonwebtoken.sign(payload, process.env.JWT_SECRET, {
            expiresIn: "7d"
        });

        //token expires in 7 days
        res.cookie("access-token", token, {
            expires: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000),
            httpOnly: true,
            secure: process.env.NODE_ENV === "production"
        })

        const returnUser = {...user._doc};
        delete returnUser.password;
        return res.json({
            token: token,
            user: returnUser,
        })
    }
    catch(error){
        console.log(error);
        return res.status(500).send(error.message);
    }
})

// @route   PUT /api/auth/logout
// @desc    Logout user a clear the cookie
// @access  Private
router.put("/logout", requireAuth, async (req, res) => {
    try {
      res.clearCookie("access-token");
      return res.json({ success: true });
    } catch (err) {
      console.log(err);
      return res.status(500).send(err.message);
    }
  });

  
// @route POST  /api/auth/current
// @desc  Return the currently authenticated user
// @access Private
router.get("/current", requireAuth, (req,res) =>{
    if(!req.user){
        return res.status(401).send("unauthorized");
    }
    return res.json(req.user);
})
module.exports = router;