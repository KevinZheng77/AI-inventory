const {Schema, model} = require('mongoose');

const InventoryModelSchema = new Schema(
    {
        user: {
            type: Schema.Types.ObjectId,
            ref: "User"
        },
        ProductName: {
            type: String,
            required: true,
        },
        Size: {
            type: Number,
            required: true,
        },
        Cost: {
            type: Number,
            required: true,
        },
        Selling: {
            type: Number,
            required: true,
        }
    }
)

//export model
const InventoryModel = model("InventoryModel", InventoryModelSchema);
module.exports = InventoryModel;