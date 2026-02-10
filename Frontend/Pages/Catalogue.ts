var PageModule: Module = {}

// Modules
import UtilitiesModule from "../Modules/Utilities.js";

// CORE
let QuantitiesCache: {[key : string]: number} = {};

// Functions
// MECHANICS

function HandleQuantities() : void
{
    // CORE
    const QuantitiesInfo = window.Config["CoreInfo"]["Basket"]["Quantities"];
    
    // Functions
    // INIT
    window.Config["Products"].forEach((Product) => {
        // CORE
        QuantitiesCache[Product["Name"]] = Product["ImportedQuantity"] || 0;


        // Elements
        // DIVS        
        let QuantityBacking = document.getElementById("Product" + Product["Name"] + "Quantity") as HTMLDivElement;
        let QuantityBackingColumns : HTMLCollection = QuantityBacking.children;

        // BUTTONS
        let SubtractButton = QuantityBackingColumns[0]!.firstElementChild as HTMLButtonElement;
        let AddButton = QuantityBackingColumns[2]!.firstElementChild as HTMLButtonElement;

        // TEXTS
        let QuantityValueText = QuantityBackingColumns[1]!.firstElementChild as HTMLParagraphElement;
        
        // Functions
        // MECHANICS
        function Update() : void
        {
            // CORE
            const CurrentQuantity : number = QuantitiesCache[Product["Name"]] || 0;

            // Functions
            // INIT
            QuantityValueText.innerHTML = CurrentQuantity.toString();

            if (CurrentQuantity == QuantitiesInfo["Max"]) 
            {
                QuantityValueText.innerHTML += " [MAX]"
            }
        }

        function Add() : void
        {
            // CORE
            const CurrentQuantity : number = QuantitiesCache[Product["Name"]] || 0;

            // Functions
            // INIT
            QuantitiesCache[Product["Name"]] = UtilitiesModule.Clamp(CurrentQuantity + 1, QuantitiesInfo["Min"], QuantitiesInfo["Max"]);

            return Update();
        }

        function Subtract() : void
        {
            // CORE
            const CurrentQuantity : number = QuantitiesCache[Product["Name"]] || 0;

            // Functions
            // INIT
            QuantitiesCache[Product["Name"]] = UtilitiesModule.Clamp(CurrentQuantity - 1, QuantitiesInfo["Min"], QuantitiesInfo["Max"]);

            return Update();
        }
        
        // INIT
        AddButton.onclick = Add;
        SubtractButton.onclick = Subtract;

        Update();
    });
}

function HandleForm() : void
{
    // CORE
    let Form = document.getElementById("UpdateBasketForm") as HTMLFormElement;

    // Functions
    // INIT
    Form.addEventListener("submit", (event) => 
    {
        // Functions
        // INIT
        event.preventDefault();

        for (let ProductName in QuantitiesCache) {
            const Quantity : number = QuantitiesCache[ProductName] || 0;

            let ProductHiddenInput = document.createElement("input");
            ProductHiddenInput.type = "hidden";
            ProductHiddenInput.name = ProductName;
            ProductHiddenInput.value = Quantity.toString();

            Form.appendChild(ProductHiddenInput);
        };

        return Form.submit();
    });
}

function Initialise() : void
{
    // CORE

    // Functions
    // INIT
    HandleQuantities();
    HandleForm();
}

function End() : void
{
    // Functions
    // INIT

}

// DIRECT
PageModule.Initialise = Initialise;
PageModule.End = End;

export default PageModule