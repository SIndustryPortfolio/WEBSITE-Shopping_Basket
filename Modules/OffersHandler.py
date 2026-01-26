### READ
#
# - Discount wrapper object
# - Stores multiple types of discounts
#
###

# Modules
# INT
from .Class import Class
from .Utilities import Utilities
from .Shortcuts import Shortcuts
from .Database import Database

from .CatalogueHandler import CatalogueHandler

# EXT
import math

# CORE
OffersCache = {}

CurrentApp = None

# Functions
# CLASSES
class Offer(Class):
    def __init__(self, Meta):
        # CORE
        super().__init__()
        
        # Functions
        # INIT
        self.Public["Type"] = Meta["Type"]
        #self.Public["Options"] = Meta["Options"]

        self.Public["DisplayName"] = self.GetDisplayName(self)

##

class BuyXGetXFree(): #(Offer):
    #def __init__(self, *Args):
    #    # Functions
    #    # INIT
    #    super().__init__(*Args)

    @staticmethod
    def GetPriceReduction(OfferName, RelevantItemsMeta):
        # CORE
        Cache = OffersCache[OfferName]
        Targets = Cache["Targets"]

        SubTotal = 0
        PriceReduction = 0
        Skip = 0

        # Functions
        # INIT
        for ProductNameOrFamily in Targets:
            Skip = False

            ###################
            # DISCOUNT FAMILY #
            ###################
            if isinstance(ProductNameOrFamily, list):
                FamilySize = len(ProductNameOrFamily)
                
                Count = 0
                for x in range(FamilySize - 1, -1, -1):
                    ProductName = ProductNameOrFamily[x]
                    BasePrice = CatalogueHandler.GetProductByName(ProductName)["Price"]
                    Quantity = RelevantItemsMeta["Counters"][ProductName]
                    SubTotal += Quantity * BasePrice

                    for y in range(0, Quantity):
                        if Skip > 0:
                            PriceReduction += BasePrice
                            Skip -= 1
                            continue

                        Count += 1

                        if Count % Cache["Options"]["Buy"] == 0:
                            Skip = Cache["Options"]["Free"]

                continue

            ###################
            # SINGLE  PRODUCT #
            ###################
            ProductName = ProductNameOrFamily
            BasePrice = CatalogueHandler.GetProductByName(ProductName)["Price"]
            Quantity = RelevantItemsMeta["Counters"][ProductName]
            SubTotal += Quantity * BasePrice
            Count = 0

            for y in range(0, Quantity):
                if Skip > 0:
                    PriceReduction += BasePrice
                    Skip -= 1
                    continue

                Count += 1

                if Count % Cache["Options"]["Buy"] == 0:
                    Skip = Cache["Options"]["Free"]


        """
        for Item in RelevantItems:
            SubTotal += BasePrice

            if Skip:
                PriceReduction += BasePrice
                Skip = False
                continue

            Count += 1

            if Count % Options["Buy"] == 0:
                Skip = True
                continue
        """

        return round(PriceReduction, 2), SubTotal
            

    # UNIVERSAL / CLASS & SERVICE METHOD
    @staticmethod
    def GetDisplayName(OfferName):
        # CORE
        Cache = OffersCache[OfferName]
        Options = Cache["Options"]

        # Functions
        # INIT
        return f"Buy {Options["Buy"]} Get {Options["Free"]} Free"

class Percentage(): #(Offer):
    #def __init__(self, *Args):
    #    # Functions
    #    # INIT
    #    super().__init__(*Args)

    @staticmethod
    def GetPriceReduction(OfferName, RelevantItemsMeta):
        # CORE
        Cache = OffersCache[OfferName]

        SubTotal = 0
        PriceReduction = 0
        
        # Functions
        # INIT
        for ProductName in Cache["Targets"]:
            BasePrice = CatalogueHandler.GetProductByName(ProductName)["Price"]
            Quantity = RelevantItemsMeta["Counters"][ProductName]
            SubTotal = Quantity * BasePrice
            PriceReduction += Utilities.Clamp((Quantity * (Cache["Options"]["DiscountBy"] / 100)), 0, math.inf) * BasePrice

        #for Item in RelevantItems:
        #    SubTotal += BasePrice
        #    PriceReduction += Utilities.Clamp(BasePrice * (Options["DiscountBy"] / 100), 0, math.inf)

        return round(PriceReduction, 2), SubTotal

    # UNIVERSAL / CLASS & SERVICE METHOD
    @staticmethod
    def GetDisplayName(OfferName):
          # CORE
        Cache = OffersCache[OfferName]
        Options = Cache["Options"]

        # Functions
        # INIT
        return f"{Options["DiscountBy"]}% Off"
            

##
##
TypeMapping = {
    "BuyXGetXFree" : BuyXGetXFree,
    "Percentage": Percentage
}

##
class OffersHandler():
    @staticmethod
    def GetOffersCache():
        # Functions
        # INIT
        return OffersCache

    @staticmethod
    def GetTypeMapping():
        # Functions
        # INIT
        return TypeMapping

    @staticmethod
    def GetOffer(OfferName):
        # Functions
        # INIT
        return TypeMapping[OfferName]

    @staticmethod
    def GetDisplayName(OfferName, *Args):
        # Functions
        # INIT
        return OffersHandler.GetOffer(OfferName).GetDisplayName(*Args)
    
    @staticmethod
    def GetRelevantItemsMeta(OfferName, UserBasket):
        # CORE
        Cache = OffersCache[OfferName]
        RelevantItemsMeta = {
            "Counters": {},
            "Raw": []
        }

        # Functions
        # MECHANICS
        def HandleOne(ProductName):
            # CORE
            AllProductsOfName = UserBasket.FindAll(ProductName)

            # Functions
            # INIT
            RelevantItemsMeta["Counters"][ProductName] = len(AllProductsOfName)
            Utilities.AddToTable(RelevantItemsMeta["Raw"], *AllProductsOfName)

        # INIT
        for ProductNameOrFamily in Cache["Targets"]:
            if isinstance(ProductNameOrFamily, list):
                for ProductName in ProductNameOrFamily:
                    HandleOne(ProductName)
                continue

            HandleOne(ProductNameOrFamily)

        HandleOne = None # Clean Up

        return RelevantItemsMeta
    

##
def Initialise(App):
    # CORE
    global CurrentApp

    # Functions
    # INIT
    CurrentApp = App

    OffersCollection = Database.GetDatabase()["Offers"]

    Success, Records = Utilities.TryFor(3, OffersCollection.find)

    if not Success:
        return
    
    for Record in Records:
        OfferName = Record["Name"]
        OfferType = Record["Type"]
        OfferOptions = Record["Options"]
        OfferTargets = Record["Targets"]

        OffersCache[OfferName] = {
            "Object": TypeMapping[OfferType],
            "Options": OfferOptions,
            "Targets": OfferTargets
        }

        for ProductNameOrFamily in OfferTargets:
            if isinstance(ProductNameOrFamily, list):
                for ProductName in ProductNameOrFamily:
                    CatalogueHandler.GetProductByName(ProductName)["Offer"] = OfferName
                
                continue
            
            CatalogueHandler.GetProductByName(ProductNameOrFamily)["Offer"] = OfferName