const User= require("../Models/UserModel");
const jsonwebtoken = require('jsonwebtoken');
const cookieParser = require('cookie-parser');
const requireAuth = async (req, res, next) => {
    const token = req.cookies["access-token"];
    let isAuthenticated = false;

    if(token){
        try{
            const {userId} = jsonwebtoken.verify(token, process.env.JWT_SECRET);
            try{
                const user = await User.findById(userId);
                if(user){
                    const returnUser = {...user._doc};
                    delete returnUser.password;
                    req.user = returnUser;
                    isAuthenticated = true;
                }
            }
            catch{
                return res.status(401).send('User does not exist');
                isAuthenticated = false;
            }
        }
        catch{
            return res.status(401).send('token not verified');
            isAuthenticated = false;
        }
    }else{
        return res.status(401).send('No token');
    }

    if(isAuthenticated){
        return next();
    }
    else{
        return res.status(401).send("Unauthorized");
    }
};

module.exports = requireAuth;