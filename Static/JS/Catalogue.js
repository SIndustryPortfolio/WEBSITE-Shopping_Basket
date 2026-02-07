var PageModule = {};
// Modules
import UtilitiesModule from "./Modules/Utilities.js";
// CORE
let QuantitiesCache = {};
// Functions
// MECHANICS
function HandleCheckout() {
    // Elements
    // DIVS 
    let ShopContainerDiv = document.getElementById("ShopContainer");
    let UserBasketContainerDiv = document.getElementById("UserBasketContainer");
    let CheckoutToggleButton = document.getElementById("CheckoutToggle");
    // Functions
    // MECHANICS
    function Toggle() {
        // CORE
        let ClassList = UserBasketContainerDiv.classList;
        // Functions
        // INIT
        if (ClassList.contains("CloseCheckout")) {
            CheckoutToggleButton.innerHTML = ">";
            CheckoutToggleButton.classList.remove("btn-primary");
            CheckoutToggleButton.classList.add("btn-secondary");
            ClassList.remove("CloseCheckout");
            ShopContainerDiv.classList.remove("OpenShopContainer");
        }
        else {
            CheckoutToggleButton.innerHTML = "<";
            CheckoutToggleButton.classList.remove("btn-secondary");
            CheckoutToggleButton.classList.add("btn-primary");
            ClassList.add("CloseCheckout");
            ShopContainerDiv.classList.add("OpenShopContainer");
        }
    }
    // INIT
    CheckoutToggleButton.onclick = Toggle;
}
function HandleUserBasketTable() {
    // Elements
    // DIVS
    let UserBasketTable = document.getElementById("UserBasketTable");
    if (UserBasketTable == undefined) {
        return;
    }
    let TableBody = UserBasketTable.children[1];
    // Functions
    // MECHANICS
    function GetCostOfProduct(Product) {
        // CORE
        let Price = 0;
        let BasketPrice = 0;
        // Functions
        // INIT
        for (let index in Product["Items"]) {
            const Item = Product["Items"][index];
            Price += Item["Price"];
            BasketPrice += Item["BasketPrice"] || 0;
        }
        return {
            "Price": UtilitiesModule.Round(Price, 2),
            "BasketPrice": UtilitiesModule.Round(BasketPrice, 2)
        };
    }
    // INIT
    window.Config["Products"].forEach((Product) => {
        const Quantity = Product["ImportedQuantity"] || 0;
        const ProductName = Product["Name"];
        const PriceMeta = GetCostOfProduct(Product);
        const Price = PriceMeta["Price"];
        const BasketPrice = PriceMeta["BasketPrice"];
        let ProductNamePostfix = "";
        if (Quantity == 0) {
            return;
        }
        let TableRow = document.createElement("tr");
        let TableProductNameDefinition = document.createElement("td");
        let TableProductQuantityDefinition = document.createElement("td");
        TableProductQuantityDefinition.classList.add("text-center");
        let TablePriceDefinition = document.createElement("td");
        TablePriceDefinition.classList.add("text-center");
        if (Price != BasketPrice) {
            let UndiscountedText = document.createElement("p");
            UndiscountedText.classList.add("text-secondary");
            UndiscountedText.innerHTML = "<i>" + UtilitiesModule.FormatMoney(Price) + "</i>";
            UndiscountedText.style.textDecoration = "line-through";
            UndiscountedText.style.display = "inline-block";
            UndiscountedText.style.padding = "5px";
            TablePriceDefinition.appendChild(UndiscountedText);
            ProductNamePostfix = "<b>[OFFER]</b>";
        }
        let FinalPriceText = document.createElement("p");
        FinalPriceText.innerHTML = UtilitiesModule.FormatMoney(BasketPrice);
        FinalPriceText.style.display = "inline-block";
        FinalPriceText.style.padding = "5px";
        TablePriceDefinition.appendChild(FinalPriceText);
        TableProductQuantityDefinition.innerHTML = Quantity.toString();
        TableProductNameDefinition.innerHTML = ProductName + " " + ProductNamePostfix;
        TableRow.appendChild(TableProductNameDefinition);
        TableRow.appendChild(TableProductQuantityDefinition);
        TableRow.appendChild(TablePriceDefinition);
        TableBody.appendChild(TableRow);
    });
}
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
    HandleUserBasketTable();
    HandleCheckout();
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