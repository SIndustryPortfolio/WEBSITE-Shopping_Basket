var PageModule = {}

// Modules
import UtilitiesModule from (window.Config["StaticPath"] + "/Utilities.js");

// CORE

// Functions
// MECHANICS
function Initialise() 
{
    // CORE
    const QuantitiesInfo = CoreInfo["Basket"]["Quantities"];

    // Functions
    // INIT
    window.Config["Products"].array.forEach(Product => {
        // CORE
        let Quantity = 0

        // Elements
        // DIVS        
        let QuantityBacking = document.getElementById("Product" + Product["Name"] + "Quantity");
        let QuantityBackingColumns = QuantityBacking.children;

        // BUTTONS
        let SubtractButton = QuantityBackingColumns[0].firstChild;
        let AddButton = QuantityBackingColumns[2].firstChild;

        // TEXTS
        let QuantityValueText = QuantityBackingColumns[1].firstChild;
        
        // Functions
        // MECHANICS
        function Update()
        {
            // Functions
            // INIT
            QuantityValueText.innerHTML = Quantity;
        }

        function Add() 
        {
            // Functions
            // INIT
            Quantity = UtilitiesModule.Clamp(Quantity + 1, QuantitiesInfo["Min"], QuantitiesInfo["Max"]);

            return Update();
        }

        function Subtract() 
        {
            // Functions
            // INIT
            Quantity = UtilitiesModule.Clamp(Quantity - 1, QuantitiesInfo["Min"], QuantitiesInfo["Max"]);

            return Update();
        }
        
        // INIT
        AddButton.OnClick = Add;
        SubtractButton.OnClick = Subtract;

        Update();
    });
}

function End() 
{
    // Functions
    // INIT

}

// DIRECT
PageModule.Initialise = Initialise;
PageModule.End = End;

export default PageModule