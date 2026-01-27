### READ
#
# - Discount wrapper object
# - Stores multiple types of discounts
#
###

# Modules
# INT
#from .Class import Class
from .Utilities import Utilities
#from .Shortcuts import Shortcuts
from .Database import Database

from .CatalogueHandler import CatalogueHandler

# EXT

# CORE
OffersCache = {}

CurrentApp = None

# Functions
# CLASSES

## DEPRECATED, Pre discount-family system: Better for "stand-alone" discounts ##
################################################################################
""""
class Offer(Class):
    def __init__(self, Meta):
        # CORE
        super().__init__()
        
        # Functions
        # INIT
        self.Public["Type"] = Meta["Type"]
        #self.Public["Options"] = Meta["Options"]

        self.Public["DisplayName"] = self.GetDisplayName(self)
"""
##

# OFFER TYPE
class BuyXGetXFree(): #(Offer):
    
    ## DEPRECATED, NO LONGER A CLASS -> CHANGED TO "BEHAVIOUR" & Singleton ##
    #########################################################################

    #def __init__(self, *Args):
    #    # Functions
    #    # INIT
    #    super().__init__(*Args)


    @staticmethod
    def HandlePriceReduction(OfferName, RelevantItemsMeta):
        # CORE
        Cache = OffersCache[OfferName]
        Targets = Cache["Targets"]

        Buy = int(Cache["Options"]["Buy"])
        Free = int(Cache["Options"]["Free"])

        # Functions
        # INIT
        for ProductNameOrFamily in Targets:
            Skip = 0
            Count = 0

            ###################
            # DISCOUNT FAMILY #
            ###################
            if isinstance(ProductNameOrFamily, list):
                FamilySize = len(ProductNameOrFamily)
                
                for x in range(FamilySize - 1, -1, -1):
                    ProductName = ProductNameOrFamily[x]
                    CountersMeta = RelevantItemsMeta["Counters"][ProductName]

                    for Item in CountersMeta["Products"]:
                        if Skip > 0:
                            print("Skipping " + Item["Name"])
                            Item["BasketPrice"] = 0
                            Skip -= 1
                            continue

                        Count += 1

                        if Count == Buy:
                            Count = 0
                            Skip = Free
                            

                continue


            ###################
            # SINGLE  PRODUCT #
            ###################
            ProductName = ProductNameOrFamily
            CountersMeta = RelevantItemsMeta["Counters"][ProductName]           

            for Item in CountersMeta["Products"]:
                if Skip > 0:
                    Item["BasketPrice"] = 0
                    Skip -= 1
                    continue

                Count += 1

                if Count == Buy:
                    Count = 0
                    Skip = Free



    """"
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

        return round(PriceReduction, 2), SubTotal
    """
            

    # DEPRECATED, builds actual offer name based off options
    """
    @staticmethod
    def GetDisplayName(OfferName):
        # CORE
        Cache = OffersCache[OfferName]
        Options = Cache["Options"]

        # Functions
        # INIT
        return f"Buy {Options["Buy"]} Get {Options["Free"]} Free"
    """

## OFFER TYPE
class Percentage(): #(Offer):

    ## DEPRECATED, NO LONGER A CLASS -> CHANGED TO "BEHAVIOUR" & Singleton ##
    #########################################################################
    #def __init__(self, *Args):
    #    # Functions
    #    # INIT
    #    super().__init__(*Args)

    @staticmethod
    def HandlePriceReduction(OfferName, RelevantItemsMeta):
        # CORE
        Cache = OffersCache[OfferName]
        
        # Functions
        # INIT
        DiscountMultiplier = int(Cache["Options"]["DiscountBy"]) / 100

        for ProductName in Cache["Targets"]:
            CountersMeta = RelevantItemsMeta["Counters"][ProductName]

            print(CountersMeta["Products"])

            for Item in CountersMeta["Products"]:
                print("Item Id: " + str(id(Item)))
                print("Item Price: " + str(Item["Price"]))
                print("Item Basket Price: " + str(Item["BasketPrice"]))
                print("Discount Multiplier: " + str(DiscountMultiplier))
                print("New Basket Price: " + str(Item["BasketPrice"] - (Item["Price"] * DiscountMultiplier)))

                Item["BasketPrice"] -= (Item["Price"] * DiscountMultiplier)


    """"
    @staticmethod
    def GetPriceReduction(OfferName, RelevantItemsMeta):
        # CORE
        Cache = OffersCache[OfferName]

        SubTotal = 0
        PriceReduction = 0
        
        # Functions
        # INIT
        for ProductName in Cache["Targets"]:
            CountersMeta = RelevantItemsMeta["Counters"][ProductName]

            BasePrice = CatalogueHandler.GetProductByName(ProductName)["Price"]
            Quantity = CountersMeta["Count"]
            SubTotal = Quantity * BasePrice
            PriceReduction += Utilities.Clamp((Quantity * (Cache["Options"]["DiscountBy"] / 100)), 0, math.inf) * BasePrice

        return round(PriceReduction, 2), SubTotal
    """

    # DEPRECATED, builds actual offer name based off options
    """"
    @staticmethod
    def GetDisplayName(OfferName):
          # CORE
        Cache = OffersCache[OfferName]
        Options = Cache["Options"]

        # Functions
        # INIT
        return f"{Options["DiscountBy"]}% Off"
    """
            

##
##
TypeMapping = {
    "BuyXGetXFree" : BuyXGetXFree,
    "Percentage": Percentage
}

##
class OffersHandler():
    # Get DB-parsed offer data
    @staticmethod
    def GetOffersCache():
        # Functions
        # INIT
        return OffersCache

    # Get all offer behaviours / services
    @staticmethod
    def GetTypeMapping():
        # Functions
        # INIT
        return TypeMapping

    # Factory method to get "behaviours", return "Offer" singleton service
    @staticmethod
    def GetOffer(OfferName):
        # Functions
        # INIT
        return TypeMapping[OfferName]

    # DEPRECATED, Names now stored in DB for better offer grouping
    """"
    @staticmethod
    def GetDisplayName(OfferName, *Args):
        # Functions
        # INIT
        return OffersHandler.GetOffer(OfferName).GetDisplayName(*Args)
    """
        
    # Get relevant "products" in user basket along with how many
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
            RelevantItemsMeta["Counters"][ProductName] = {
                "Count" : len(AllProductsOfName),
                "Products" : AllProductsOfName
            }

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
def LoadRecords(Records):
    # Functions
    # MECHANICS
    def HandleOne(OfferName, ProductName):
        # Functions
        # INIT
        CatalogueProduct =  CatalogueHandler.GetProductByName(ProductName)

        # Product doesn't exist
        if not CatalogueProduct:
            return None

        if CatalogueProduct["Offers"] == None:
            CatalogueProduct["Offers"] = []
        
        CatalogueProduct["Offers"].append(OfferName)

    # INIT
    # Load DB Offers into cache
    for Record in Records:
        OfferName = Record["Name"]
        OfferType = Record["Type"]
        OfferOptions = Record["Options"]
        OfferTargets = Record["Targets"]

        OffersCache[OfferName] = {
            "Class": TypeMapping[OfferType],
            "Options": OfferOptions,
            "Targets": OfferTargets
        }

        for ProductNameOrFamily in OfferTargets:
            if isinstance(ProductNameOrFamily, list):
                for ProductName in ProductNameOrFamily:
                    HandleOne(OfferName, ProductName)
                
                continue
            
            HandleOne(OfferName, ProductNameOrFamily)

    HandleOne = None

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
    
    LoadRecords(Records)