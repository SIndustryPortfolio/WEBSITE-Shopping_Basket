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
  // Functions
  // INIT
  const factor = 10 ** Decimals;
  return Math.round((Value + Number.EPSILON) * factor) / factor;
}

UtilitiesModule.FormatMoney = function(Value) 
{
  // Functions
  // INIT
  return window.Config["CoreInfo"]["Currency"]["Prefix"] + Number(Value).toFixed(2);
}


export default UtilitiesModule;