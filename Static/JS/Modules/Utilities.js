const UtilitiesModule = {
    "Clamp": function (Value, Min, Max) {
        // Functions
        // INIT
        return Math.min(Math.max(Value, Min), Max);
    },
    "Round": function (Value, Decimals = 0) {
        // Functions
        // INIT
        const factor = 10 ** Decimals;
        return Math.round((Value + Number.EPSILON) * factor) / factor;
    },
    "FormatMoney": function (Value) {
        // Functions
        // INIT
        const prefix = window.Config["CoreInfo"]["Currency"]["Prefix"];
        const number = Number(Value).toFixed(2);
        return prefix + number;
    }
};
export default UtilitiesModule;
//# sourceMappingURL=Utilities.js.map