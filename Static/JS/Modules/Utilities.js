var UtilitiesModule = {}

// CORE


// Functions
// DIRECT
UtilitiesModule.Clamp = function(Value, Min, Max) {
    // Functions
    // INIT
    return Math.min(Math.max(Value, Min), Max);
}


export default UtilitiesModule;