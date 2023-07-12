const Validator = require('validator');
const isEmpty = require('./Emptyemail');

const validateInventoryInput = data =>{
    let errors={};

    //check if the Name is empty
    if(isEmpty(data.ProductName)){
        errors.ProductName = "Name Can't be empty"
    }

    //check if the Selling is empty
    if(isEmpty(data.Selling)){
        errors.Selling = "Selling Price can not be empty"
    }


    //check if the Cost is empty
    if(isEmpty(data.Cost)){
        errors.Cost = "Cost of Product can not be empty"
    }


    //check if the Size is empty
    if(isEmpty(data.Size)){
        errors.Cost = "Size can not be empty"
    }

    return{
        errors,
        isValid: isEmpty(errors)
    }
}

module.exports = validateInventoryInput;