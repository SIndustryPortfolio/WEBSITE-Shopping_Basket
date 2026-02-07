// CORE
interface Utilities {
  Clamp: (Value: number, Min: number, Max: number) => number,
  Round: (Value: number, Decimals?: number) => number,
  FormatMoney: (Value: number | string) => string
}


const UtilitiesModule: Utilities =
{
  "Clamp": function(Value : number, Min : number, Max : number)  : number {
      // Functions
      // INIT
      return Math.min(Math.max(Value, Min), Max);
  },

  "Round": function(Value : number, Decimals : number = 0) : number {
    // Functions
    // INIT
    const factor : number = 10 ** Decimals;

    return Math.round((Value + Number.EPSILON) * factor) / factor;
  },

  "FormatMoney": function(Value : number | string) : string 
  {
    // Functions
    // INIT
    const prefix : string = window.Config["CoreInfo"]["Currency"]["Prefix"];
    const number : string = Number(Value).toFixed(2) as string;

    return prefix + number;
  }
}


export default UtilitiesModule;