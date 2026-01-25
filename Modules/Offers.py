### READ
#
# - Discount object
# - Stores multiple types of discounts
# - Universal usage, Wrapper & Objects
#
###

# Modules
# INT
from .Class import Class

# EXT

# CORE

# Functions
# CLASSES
class Offer(Class):
    def __init__(self, Meta):
        # CORE
        super().__init__()
        
        # Functions
        # INIT
        self.Public["Type"] = Meta["Type"]
        self.Public["Options"] = Meta["Options"]

        self.Public["DisplayName"] = self.GetDisplayName(self)

##

class BuyXGetXFree(Offer):
    def __init__(self, *Args):
        # Functions
        # INIT
        super().__init__(*Args)

    # UNIVERSAL / CLASS & SERVICE METHOD
    @classmethod
    def GetDisplayName(cls, OptionsOrSelf):
        # CORE
        if isinstance(OptionsOrSelf, cls):
            OptionsOrSelf = OptionsOrSelf.Public["Options"]

        # Functions
        # INIT
        return f"Buy {OptionsOrSelf["Buy"]} Get {OptionsOrSelf["Free"]} Free"

class Percentage(Offer):
    def __init__(self, *Args):
        # Functions
        # INIT
        super().__init__(*Args)

    # UNIVERSAL / CLASS & SERVICE METHOD
    @classmethod
    def GetDisplayName(cls, OptionsOrSelf):
        # CORE
        if isinstance(OptionsOrSelf, cls):
            OptionsOrSelf = OptionsOrSelf.Public["Options"]

        # Functions
        # INIT
        return f"{OptionsOrSelf["DiscountBy"]}% Off"

##
##
TypeMapping = {
    "BuyXGetXFree" : BuyXGetXFree,
    "Percentage": Percentage
}

##
class Offers():
    @staticmethod
    def GetOffer(OfferName):
        # Functions
        # INIT
        return TypeMapping[OfferName]

    @staticmethod
    def GetDisplayName(OfferName, *Args):
        # Functions
        # INIT
        return Offers.GetOffer(OfferName).GetDisplayName(*Args)
    


