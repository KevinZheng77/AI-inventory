const {Schema, model} = require('mongoose');

const InventoryModelSchema = new Schema(
    {
        user: {
            type: Schema.Types.ObjectId,
            ref: "User"
        },
        content: {
            type: String,
            require: true,
        },
    }
)

//export model
const InventoryModel = model("InventoryModel", InventoryModelSchema);
module.exports = InventoryModel;