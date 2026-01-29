var UtilitiesModule = {}

// CORE


// Functions
// DIRECT
UtilitiesModule.Clamp = function(Value, Min, Max) {
    // Functions
    // INIT
    return Math.min(Math.max(Value, Min), Max);
}

UtilitiesModule.Round = function(Value, Decimals = 0) {
  const factor = 10 ** Decimals;
  return Math.round((Value + Number.EPSILON) * factor) / factor;
}


export default UtilitiesModule;