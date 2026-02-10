var ComponentModule = {};
// Modules
import UtilitiesModule from "../Modules/Utilities.js";
// Functions
// MECHANICS
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
            CheckoutToggleButton.classList.remove("btn-light");
            CheckoutToggleButton.classList.add("btn-secondary");
            CheckoutToggleButton.style.backgroundImage = "";
            CheckoutToggleButton.style.borderRadius = "8px";
            CheckoutToggleButton.style.boxShadow = "";
            CheckoutToggleButton.style.marginRight = "0";
            CheckoutToggleButton.style.transform = "translate(-110%, 50%)";
            ClassList.remove("CloseCheckout");
            if (ShopContainerDiv) {
                ShopContainerDiv.classList.remove("OpenShopContainer");
            }
        }
        else {
            CheckoutToggleButton.innerHTML = "";
            CheckoutToggleButton.classList.remove("btn-secondary");
            CheckoutToggleButton.classList.add("btn-light");
            CheckoutToggleButton.innerHTML = "🧺";
            CheckoutToggleButton.style.borderRadius = "50%";
            CheckoutToggleButton.style.boxShadow = "0 10px 24px rgba(0, 0, 0, 0.3)";
            CheckoutToggleButton.style.transform = "translate(-110%, 50%)";
            ClassList.add("CloseCheckout");
            if (ShopContainerDiv) {
                ShopContainerDiv.classList.add("OpenShopContainer");
            }
        }
    }
    // INIT
    CheckoutToggleButton.onclick = Toggle;
}
function Initialise() {
    // Functions
    // INIT
    HandleUserBasketTable();
    HandleCheckout();
}
// DIRECT   
ComponentModule.Initialise = Initialise;
export default ComponentModule;
//# sourceMappingURL=CheckoutBasket.js.map