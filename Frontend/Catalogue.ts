var PageModule: {[key : string]: any} = {}

// Modules
import UtilitiesModule from "./Modules/Utilities.js";

// CORE
let QuantitiesCache: {[key : string]: number} = {};

// Functions
// MECHANICS
function HandleCheckout() : void
{
    // Elements
    // DIVS 
    let ShopContainerDiv : HTMLDivElement = document.getElementById("ShopContainer") as HTMLDivElement;
    let UserBasketContainerDiv : HTMLDivElement = document.getElementById("UserBasketContainer") as HTMLDivElement;

    let CheckoutToggleButton : HTMLButtonElement = document.getElementById("CheckoutToggle") as HTMLButtonElement;

    // Functions
    // MECHANICS
    function Toggle() : void
    {
        // CORE
        let ClassList : DOMTokenList = UserBasketContainerDiv.classList as DOMTokenList;

        // Functions
        // INIT

        if (ClassList.contains("CloseCheckout"))
        {
            CheckoutToggleButton.innerHTML = ">";
            CheckoutToggleButton.classList.remove("btn-primary");
            CheckoutToggleButton.classList.add("btn-secondary");

            ClassList.remove("CloseCheckout");
            ShopContainerDiv.classList.remove("OpenShopContainer");
        }
        else  
        {
            CheckoutToggleButton.innerHTML = "<";
            CheckoutToggleButton.classList.remove("btn-secondary");
            CheckoutToggleButton.classList.add("btn-primary");
            
            ClassList.add("CloseCheckout");
            ShopContainerDiv.classList.add("OpenShopContainer");
        }
    }

    // INIT
    CheckoutToggleButton.onclick = Toggle
}

function HandleUserBasketTable() : void
{
    // Elements
    // DIVS
    let UserBasketTable : HTMLTableElement = document.getElementById("UserBasketTable") as HTMLTableElement;

    if (UserBasketTable == undefined) 
    {
        return;
    }

    let TableBody : HTMLTableElement = UserBasketTable.children[1] as HTMLTableElement;

    // Functions
    // MECHANICS
    function GetCostOfProduct(Product : Product) : {"Price" : number, "BasketPrice" : number} 
    {
        // CORE
        let Price = 0;
        let BasketPrice = 0;

        // Functions
        // INIT
        for (let index in Product["Items"]) 
        {
            const Item = Product["Items"][index] as Item;
            
            Price += Item["Price"];
            BasketPrice += Item["BasketPrice"] || 0;
        }

        return {
            "Price": UtilitiesModule.Round(Price, 2), 
            "BasketPrice": UtilitiesModule.Round(BasketPrice, 2)
        }
    }

    // INIT
    window.Config["Products"].forEach((Product : Product) =>
    {
        const Quantity : number = Product["ImportedQuantity"] || 0;
        const ProductName : string = Product["Name"];

        const PriceMeta = GetCostOfProduct(Product);
        const Price : number = PriceMeta["Price"];
        const BasketPrice : number = PriceMeta["BasketPrice"];

        let ProductNamePostfix : string = "";

        if (Quantity == 0) 
        {
            return;
        }

        let TableRow = document.createElement("tr") as HTMLTableRowElement;
        
        let TableProductNameDefinition = document.createElement("td") as HTMLTableCellElement;


        let TableProductQuantityDefinition = document.createElement("td") as HTMLTableCellElement;
        TableProductQuantityDefinition.classList.add("text-center");

        let TablePriceDefinition = document.createElement("td") as HTMLTableCellElement;
        TablePriceDefinition.classList.add("text-center");


        if (Price != BasketPrice) 
        {
            let UndiscountedText = document.createElement("p") as HTMLParagraphElement;
            UndiscountedText.classList.add("text-secondary");
            UndiscountedText.innerHTML = "<i>" + UtilitiesModule.FormatMoney(Price) + "</i>";
            UndiscountedText.style.textDecoration = "line-through";
            UndiscountedText.style.display = "inline-block";
            UndiscountedText.style.padding = "5px";

            TablePriceDefinition.appendChild(UndiscountedText);

            ProductNamePostfix = "<b>[OFFER]</b>";
        }

        let FinalPriceText = document.createElement("p") as HTMLParagraphElement;
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
    HandleUserBasketTable();
    HandleCheckout();
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