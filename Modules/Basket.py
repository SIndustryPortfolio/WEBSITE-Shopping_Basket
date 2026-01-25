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

    # OVERWRITE to pure JSON, all items become serialised.
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