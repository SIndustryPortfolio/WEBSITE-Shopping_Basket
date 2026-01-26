### READ
#
# - The basket pricer / calculator in question
# - Calculates Subtotal & Total of baskets including Varying offers & discounts
# 
###

# MODULES
# INT
from .Utilities import Utilities
from .OffersHandler import OffersHandler

# EXT
import math

# Functions
# MECHANICS

##
class BasketPricer():
    @staticmethod
    def CalculateCosts(UserBasket):
        # CORE
        PriceReduction = 0 #Cost of discounts
        SubTotal = 0 # Undiscounted Cost
        Total = 0 # Final Cost
        
        AlreadyChecked = []

        # Functions
        # INIT
        for OfferName, Cache in OffersHandler.GetOffersCache().items(): #Offers.GetTypeMapping().items():
            RelevantItemsMeta = OffersHandler.GetRelevantItemsMeta(OfferName, UserBasket)

            if len(RelevantItemsMeta["Raw"]) == 0:
                continue

            
            
            #Product = OfferItems[0]

            #if Product == None:
            #    continue

            _PriceReduction, _SubTotal = Cache["Object"].GetPriceReduction(OfferName, RelevantItemsMeta)

            Utilities.AddToTable(AlreadyChecked, *RelevantItemsMeta["Raw"])

            #AlreadyChecked.append(*OfferItems)
            
            PriceReduction += _PriceReduction
            SubTotal += _SubTotal
        
        for Product in UserBasket["Items"]:
            if Product in AlreadyChecked:
                continue

            SubTotal += Product["Price"]


        Total = Utilities.Clamp(SubTotal - PriceReduction, 0, math.inf)

        return {
            "PriceReduction": round(PriceReduction, 2),
            "SubTotal": round(SubTotal, 2),
            "Total": round(Total, 2)
        }
        

