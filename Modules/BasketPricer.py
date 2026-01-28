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
    # Calculate all the final costs of a User Basket, returns a dictionary.
    @staticmethod
    def CalculateCosts(UserBasket):
        # CORE
        PriceReduction = 0 #Cost of discounts
        SubTotal = 0 # Undiscounted Cost
        Total = 0 # Final Cost
        
        #AlreadyChecked = []

        # Functions
        # INIT

        ## RESET ALL BASKET PRICES TO BASE PRICE
        for Product in UserBasket["Items"]:
            Product["BasketPrice"] = Product["Price"]

        for OfferName, Cache in OffersHandler.GetOffersCache().items(): #Offers.GetTypeMapping().items():
            RelevantItemsMeta = OffersHandler.GetRelevantItemsMeta(OfferName, UserBasket)

            if len(RelevantItemsMeta["Raw"]) == 0:
                continue

            Cache["Class"].HandlePriceReduction(OfferName, RelevantItemsMeta)

            #_PriceReduction, _SubTotal = Cache["Object"].GetPriceReduction(OfferName, RelevantItemsMeta)

            #Utilities.AddToTable(AlreadyChecked, *RelevantItemsMeta["Raw"])
            
            #PriceReduction += _PriceReduction
            #SubTotal += _SubTotal
        
        for Product in UserBasket["Items"]:
            SubTotal = round(SubTotal + Product["Price"], 2)
            PriceReduction = round(PriceReduction + Utilities.Clamp(Product["Price"] - Product["BasketPrice"], 0, math.inf), 2)


        # CALCULATE COSTS

        # Total cannot dive below 0
        Total = round(Utilities.Clamp(SubTotal - PriceReduction, 0, math.inf), 2)

        return {
            "PriceReduction": PriceReduction,
            "SubTotal": SubTotal,
            "Total": Total
        }
        

