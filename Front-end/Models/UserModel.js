const mongoose = require('mongoose');
const { Schema, model} = mongoose;

const UserSchema = new Schema(
    {
        email: {
            type: String,
            required: true
        },
        password: {
            type: String,
            required: true,
        },
        name: {
            type: String,
            required: true,
        }
    },
    {
        timestamps: true
    }
);

//exports the model
const User = model('User', UserSchema);
module.exports = User;
