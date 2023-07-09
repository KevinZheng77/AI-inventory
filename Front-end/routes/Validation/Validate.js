const Validator = require('validator');
const isEmpty = require('./Emptyemail');

const validateRegisterInput = (data) => {
    let errors = {};

    if(isEmpty(data.email)) {
        errors.email = "Email field can not be empty";
    }
    // checks to see if email is not empty
    else if(Validator.isEmpty(data.email) == true){
        errors.email = "Invalid email";
    }

    //Checks Password
    if(isEmpty(data.password)){
        errors.password = 'Password can not be empty';
    }
    else if(Validator.isLength(data.password, {min: 6, max:50}) == false){
        errors.password = "Password must be between 6 and 50 characters";
    }

     //Checks Name Field
     if(isEmpty(data.name)){
        errors.name = 'Name can not be empty';
    }
    //makes sure the name is not too long
    else if(Validator.isLength(data.name, {min:1, max:50}) == false){
        errors.name = "Your name is too Long"
    }

    //check confirmed password field
    if(isEmpty(data.confirmPassword)){
        errors.confirmPassword = 'Confirm Password can not be empty';
    }
    else if(Validator.equals(data.password, data.confirmPassword) == false){
        errors.confirmPassword = 'Password and confirmed passwords do not match'
    }

    return{
        errors,
        isValid: isEmpty(errors),
    }
}

module.exports = validateRegisterInput;