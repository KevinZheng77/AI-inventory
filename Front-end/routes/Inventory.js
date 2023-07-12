const express = require('express');
const router = express.Router();
const InventoryModel = require('../Models/InventoryModel');
const requireAuth = require('../middleware/permission');
const { route } = require('./auth');
const validateInventoryInput = require("./Validation/InventoryFormVerify");

// @route Get  /api/Inventory/test
// @desc  Test the inventory route
// @access Public
router.get("/test", (req, res) => {
    res.send("Inventory route is working");
})

// @route POST /api/Inventory/new
// @desc  Create a new inventory entry
// @access Private
router.post("/new", requireAuth, async (req,res) =>{
    try{
        //checks for valid input in inventory form
        const {isValid, errors} = validateInventoryInput(req.body);
        if(!isValid){
            return res.status(400).json(errors);
        }
        const entry = new InventoryModel({
            user: req.user._id,
            ProductName: req.body.ProductName,
            Selling: req.body.Selling,
            Cost: req.body.Cost,
            Size: req.body.Size,
        });

        await entry.save();
        return res.json(entry);
    }catch(error){
        console.log(error);
        return res.status(500).send(error.message);
    }
})

// @route POST /api/Inventory/current
// @desc  Current user inventory
// @access Private
router.get('/current', requireAuth, async (req, res) =>{
    try{
        const returnInventory = await InventoryModel.find({
            user: req.user._id
        })

        return res.json({returnInventory});
    }catch(error){
        console.log(error);
        return res.status(500).send(error.message);
    }
});

module.exports = router;
