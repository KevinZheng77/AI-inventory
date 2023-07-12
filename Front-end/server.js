//requestAnimationFrame('dotenv').config();
require('dotenv').config();
const express = require('express');
const mongoose = require("mongoose");
const cookieParser = require('cookie-parser');
//importing routes
const authRoute = require("./routes/auth");
const InventoryRoute = require("./routes/Inventory");
const GoogleRoute = require("./routes/Google");
const { GoogleApis } = require('googleapis');
const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: true}));
app.use(cookieParser());

app.get('/', (req, res) => {
    res.send('Inventory React Project')
})

app.post('/name', (req, res) => {
    if(req.body.name){
        return res.json({name: req.body.name});
    }
    else{
        return res.status(400).json({error: "No name provided sorry"});
    }
})

app.use("/api/auth", authRoute);
app.use("/api/Inventory", InventoryRoute);
app.use("/api/google", GoogleRoute);

mongoose.connect(process.env.MONGO_URI).then(()=>{
    console.log(' You just connected to the database');
    //Connects to database then tells you what port its running on
    app.listen(process.env.PORT, ()=> {
        console.log(`server is running on port ${process.env.PORT}`);
    })
}).catch((error => {
    console.log(error);
}))
