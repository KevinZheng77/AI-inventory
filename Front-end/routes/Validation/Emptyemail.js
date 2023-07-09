const isEmpty = (value) =>
    value === undefined || //checks to see if the value is undefined
    value === null || // Checks if the value is null
    (typeof value === "object" && Object.keys(value).length === 0) || //Checks if value is an object with no properties
    (typeof value === "string" && value.trim().length ===0); //Cehcks if the value is a string with only spaces

module.exports = isEmpty;