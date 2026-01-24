# MODULES
# INT
from .Utilities import Utilities
from .Class import Class

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

    def Add(self, *Products):
        # Functions
        # INIT
        self.Public["Items"].append(*Products)

    def Remove(self, *Products):
        # Functions
        # INIT
        for Product in Products:
            FoundIndex = self.Public["Items"].index(Product)

            if not FoundIndex:
                continue
            
            self.Public["Items"].pop(FoundIndex)

    def GetDict(self):
        # CORE
        JSONBasket = {
            "Items" : []
        }

        # Functions
        # INIT
        for Product in self.Public["Items"]:
            JSONBasket["Items"].append(Product.GetDict())

        return JSONBasket