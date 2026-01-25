// CORE
class UtilitiesModule
{
    Clamp(Value, Min, Max) {
        // Functions
        // INIT
        return Math.min(Math.max(Value, Min), Max);
    };
}

export default UtilitiesModule;