var PageModule = {};
// Modules
import UtilitiesModule from "../Modules/Utilities.js";
// CORE
let QuantitiesCache = {};
// Functions
// MECHANICS
function HandleQuantities() {
    // CORE
    const QuantitiesInfo = window.Config["CoreInfo"]["Basket"]["Quantities"];
    // Functions
    // INIT
    window.Config["Products"].forEach((Product) => {
        // CORE
        QuantitiesCache[Product["Name"]] = Product["ImportedQuantity"] || 0;
        // Elements
        // DIVS        
        let QuantityBacking = document.getElementById("Product" + Product["Name"] + "Quantity");
        let QuantityBackingColumns = QuantityBacking.children;
        // BUTTONS
        let SubtractButton = QuantityBackingColumns[0].firstElementChild;
        let AddButton = QuantityBackingColumns[2].firstElementChild;
        // TEXTS
        let QuantityValueText = QuantityBackingColumns[1].firstElementChild;
        // Functions
        // MECHANICS
        function Update() {
            // CORE
            const CurrentQuantity = QuantitiesCache[Product["Name"]] || 0;
            // Functions
            // INIT
            QuantityValueText.innerHTML = CurrentQuantity.toString();
            if (CurrentQuantity == QuantitiesInfo["Max"]) {
                QuantityValueText.innerHTML += " [MAX]";
            }
        }
        function Add() {
            // CORE
            const CurrentQuantity = QuantitiesCache[Product["Name"]] || 0;
            // Functions
            // INIT
            QuantitiesCache[Product["Name"]] = UtilitiesModule.Clamp(CurrentQuantity + 1, QuantitiesInfo["Min"], QuantitiesInfo["Max"]);
            return Update();
        }
        function Subtract() {
            // CORE
            const CurrentQuantity = QuantitiesCache[Product["Name"]] || 0;
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
function HandleForm() {
    // CORE
    let Form = document.getElementById("UpdateBasketForm");
    // Functions
    // INIT
    Form.addEventListener("submit", (event) => {
        // Functions
        // INIT
        event.preventDefault();
        for (let ProductName in QuantitiesCache) {
            const Quantity = QuantitiesCache[ProductName] || 0;
            let ProductHiddenInput = document.createElement("input");
            ProductHiddenInput.type = "hidden";
            ProductHiddenInput.name = ProductName;
            ProductHiddenInput.value = Quantity.toString();
            Form.appendChild(ProductHiddenInput);
        }
        ;
        return Form.submit();
    });
}
function Initialise() {
    // CORE
    // Functions
    // INIT
    HandleQuantities();
    HandleForm();
}
function End() {
    // Functions
    // INIT
}
// DIRECT
PageModule.Initialise = Initialise;
PageModule.End = End;
export default PageModule;
//# sourceMappingURL=Catalogue.js.map