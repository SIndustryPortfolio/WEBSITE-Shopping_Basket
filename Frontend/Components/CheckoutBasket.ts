var ComponentModule: Module = {}

// Modules
import UtilitiesModule from "../Modules/Utilities.js";

// Functions
// MECHANICS

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

function HandleCheckout() : void
{
    // Elements
    // DIVS 
    let ShopContainerDiv = document.getElementById("ShopContainer") as HTMLDivElement | null;
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
            CheckoutToggleButton.classList.remove("btn-light");
            CheckoutToggleButton.classList.add("btn-secondary");
            CheckoutToggleButton.style.backgroundImage = "";
            CheckoutToggleButton.style.borderRadius = "8px";
            CheckoutToggleButton.style.boxShadow = "";
            CheckoutToggleButton.style.marginRight = "0";
            CheckoutToggleButton.style.transform = "translate(-110%, 50%)";


            ClassList.remove("CloseCheckout");

            if (ShopContainerDiv) 
            {
                ShopContainerDiv.classList.remove("OpenShopContainer");
            }
        }
        else  
        {
            CheckoutToggleButton.innerHTML = "";

            CheckoutToggleButton.classList.remove("btn-secondary");
            CheckoutToggleButton.classList.add("btn-light");
            CheckoutToggleButton.innerHTML = "🧺";
            
            CheckoutToggleButton.style.borderRadius = "50%";
            CheckoutToggleButton.style.boxShadow = "0 10px 24px rgba(0, 0, 0, 0.3)";
            CheckoutToggleButton.style.transform = "translate(-110%, 50%)";
            

            ClassList.add("CloseCheckout");

            if (ShopContainerDiv) 
            {
                ShopContainerDiv.classList.add("OpenShopContainer");
            }
        }
    }

    // INIT
    CheckoutToggleButton.onclick = Toggle
}

function Initialise() 
{
    // Functions
    // INIT
    HandleUserBasketTable();
    HandleCheckout();
}

// DIRECT   
ComponentModule.Initialise = Initialise;

export default ComponentModule;