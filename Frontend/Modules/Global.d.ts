export {};

declare global 
{
    type Module = {[key : string] : any}

    type Product = 
    {
        "Name" : string,
        "Price" : number,

        "BasketPrice" : number | undefined,
        "ImportedQuantity" : number | undefined,
        
        "Items" : Item[],
        "Offers" : string[] | undefined
    }

    type Item = Omit<Product, "ImportedQuantity" | "Items">

    interface Window {
        "Config": {
            
            "CoreInfo": {
                "Currency": { "Prefix": string };

                "Meta" : { "Name": string, "Display Name": string }

                "Basket" : 
                {
                    "Quantities" : { "Max" : number, "Min" : number }
                }

                "DB" : { "ClusterName" : string }
            }

            "HostURL": string,
            "CurrentPageName" : string,
            "StaticPath" : string,
            "Products": Product[]
        },

        //

        "PageData": {[key : string]: any[]};
    }
}
