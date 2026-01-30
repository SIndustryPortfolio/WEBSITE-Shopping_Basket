var PageModule = {}

// Modules
import UtilitiesModule from "./Modules/Utilities.js"; //window.Config["StaticPath"] + "/Utilities.js";

// CORE
let QuantitiesCache = {};

// Functions
// MECHANICS
function HandleCheckout() 
{
    // Elements
    // DIVS 
    let ShopContainerDiv = document.getElementById("ShopContainer");

    let UserBasketContainerDiv = document.getElementById("UserBasketContainer")
    let CheckoutToggleButton = document.getElementById("CheckoutToggle");

    // Functions
    // MECHANICS
    function Toggle() 
    {
        // CORE
        let ClassList = UserBasketContainerDiv.classList;

        // Functions
        // INIT

        if (ClassList.contains("CloseCheckout"))
        {
            CheckoutToggleButton.innerHTML = ">";
            ClassList.remove("CloseCheckout");
            ShopContainerDiv.classList.remove("OpenShopContainer");
        }
        else  
        {
            CheckoutToggleButton.innerHTML = "<";
            ClassList.add("CloseCheckout");
            ShopContainerDiv.classList.add("OpenShopContainer");
        }
    }

    // INIT
    CheckoutToggleButton.onclick = Toggle
}

function HandleUserBasketTable() 
{
    // Elements
    // DIVS
    let UserBasketTable = document.getElementById("UserBasketTable");
    let TableBody = UserBasketTable.children[1];

    // Functions
    // MECHANICS
    function GetCostOfProduct(ProductInfo) 
    {
        // CORE
        let Price = 0;
        let BasketPrice = 0;

        // Functions
        // INIT
        for (let index in ProductInfo["Items"]) 
        {
            console.log(index);

            const Item = ProductInfo["Items"][index];

            console.log(Item);

            Price += Item["Price"];
            BasketPrice += Item["BasketPrice"];
        }

        return {
            "Price": UtilitiesModule.Round(Price, 2), 
            "BasketPrice": UtilitiesModule.Round(BasketPrice, 2)
        }
    }

    // INIT
    window.Config["Products"].forEach((ProductInfo) =>
    {
        const Quantity = ProductInfo["ImportedQuantity"] || 0;
        const CurrencyInfo = window.Config["CoreInfo"]["Currency"];
        const ProductName = ProductInfo["Name"];

        const PriceMeta = GetCostOfProduct(ProductInfo);
        const Price = PriceMeta["Price"];
        const BasketPrice = PriceMeta["BasketPrice"];

        if (Quantity == 0) 
        {
            return;
        }

        let TableRow = document.createElement("tr");
        
        let TableProductNameDefinition = document.createElement("td");


        let TableProductQuantityDefinition = document.createElement("td");
        TableProductQuantityDefinition.classList.add("text-center");

        let TablePriceDefinition = document.createElement("td");
        TablePriceDefinition.classList.add("text-center");


        if (Price != BasketPrice) 
        {
            let UndiscountedText = document.createElement("p");
            UndiscountedText.innerHTML = "<i>" + UtilitiesModule.FormatMoney(Price) + "</i>";
            UndiscountedText.style.textDecoration = "line-through";
            UndiscountedText.style.display = "inline-block";
            UndiscountedText.style.padding = "5px";

            TablePriceDefinition.appendChild(UndiscountedText);
        }

        let FinalPriceText = document.createElement("p");
        FinalPriceText.innerHTML = UtilitiesModule.FormatMoney(BasketPrice);
        FinalPriceText.style.display = "inline-block";
        FinalPriceText.style.padding = "5px";
        TablePriceDefinition.appendChild(FinalPriceText);

        TableProductQuantityDefinition.innerHTML = Quantity;
        TableProductNameDefinition.innerHTML = ProductName;

        TableRow.appendChild(TableProductNameDefinition);
        TableRow.appendChild(TableProductQuantityDefinition);
        TableRow.appendChild(TablePriceDefinition);

        TableBody.appendChild(TableRow);
    });
}

function HandleQuantities() 
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
        let QuantityBacking = document.getElementById("Product" + Product["Name"] + "Quantity");
        let QuantityBackingColumns = QuantityBacking.children;

        // BUTTONS
        let SubtractButton = QuantityBackingColumns[0].firstElementChild;
        let AddButton = QuantityBackingColumns[2].firstElementChild;

        // TEXTS
        let QuantityValueText = QuantityBackingColumns[1].firstElementChild;
        
        // Functions
        // MECHANICS
        function Update()
        {
            // Functions
            // INIT
            QuantityValueText.innerHTML = QuantitiesCache[Product["Name"]];
        }

        function Add() 
        {
            // CORE
            let CurrentQuantity = QuantitiesCache[Product["Name"]];

            // Functions
            // INIT
            QuantitiesCache[Product["Name"]] = UtilitiesModule.Clamp(CurrentQuantity + 1, QuantitiesInfo["Min"], QuantitiesInfo["Max"]);

            return Update();
        }

        function Subtract() 
        {
            // CORE
            let CurrentQuantity = QuantitiesCache[Product["Name"]];

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

function HandleForm() 
{
    // CORE
    let Form = document.getElementById("UpdateBasketForm");

    // Functions
    // INIT
    Form.addEventListener("submit", (event) => 
    {
        // Functions
        // INIT
        event.preventDefault();

        for (let ProductName in QuantitiesCache) {
            const Quantity = QuantitiesCache[ProductName];

            let ProductHiddenInput = document.createElement("input");
            ProductHiddenInput.type = "hidden";
            ProductHiddenInput.name = ProductName;
            ProductHiddenInput.value = Quantity;

            Form.appendChild(ProductHiddenInput);
        };

        return Form.submit();
    });
}

function Initialise() 
{
    // CORE

    // Functions
    // INIT
    HandleQuantities();
    HandleForm();
    HandleUserBasketTable();
    HandleCheckout();
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