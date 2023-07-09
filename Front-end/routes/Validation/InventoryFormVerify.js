const Validator = require('validator');
const isEmpty = require('./Emptyemail');

const validateInventoryInput = data =>{
    let errors={};

    //check if the content is empty
    if(isEmpty(data.content)){
        errors.content = "Content field can not be empty"
    }
    else if(!Validator.isLength(data.content)){
        errors.content = "Content field must be between 1 and 300 characters";
    }

    return{
        errors,
        isValid: isEmpty(errors)
    }
}

module.exports = validateInventoryInput;