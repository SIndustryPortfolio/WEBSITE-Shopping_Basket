### READ
#
# - The actual user basket
# - The task doesn't ask to make this but it's purely for demonstration -> It's much better to show how baskets & offers work together
# - No size constraint, user may have infinite items in the basket
#
###


# MODULES
# INT
from .Class import Class
from .Utilities import Utilities

# EXT


# Functions
# MECHANICS

##
class Basket(Class):
    def __init__(self):
        # CORE
        super().__init__()

        # Functions
        # INIT
        self.Public["Items"] = []

    def GetItemsFromName(self, ItemName, JSON=False):
        # CORE
        Items = []

        # Functions
        # INIT
        for Item in self["Items"]:
            if Item["Name"] != ItemName:
                continue
            
            if JSON:
                Items.append(Item.GetDict(JSON=True))
                continue

            Items.append(Item)

        return Items
    
    def FindAll(self, ProductName):
        # CORE
        ToReturn = []
        
        # Functions
        # INIT
        for Item in self["Items"]:
            if Item["Name"] != ProductName:
                continue
            
            ToReturn.append(Item)

        return ToReturn

    def Add(self, *Products):
        # Functions
        # INIT
        Utilities.AddToTable(self["Items"], *Products)

        #self.Public["Items"].append(*Products)

    def Remove(self, *Products):
        # Functions
        # INIT
        for Product in list(Products):
            FoundIndex = self.Public["Items"].index(Product)

            if not FoundIndex:
                continue
            
            self.Public["Items"].pop(FoundIndex)

    def Clear(self):
        # Functions
        # INIT
        self.Public["Items"] = []

    # OVERWRITE to pure JSON, all items become serialised.
    def GetDict(self, JSON=False):
        # CORE
        Dict = {
            "Items" : []
        }

        # Functions
        # INIT
        for Product in self.Public["Items"]:
            Dict["Items"].append(Product.GetDict(JSON=JSON))

        return Dict