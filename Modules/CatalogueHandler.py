### READ
#
# - Main Catalogue wrapper
#
###

# Modules
# INT
from .Database import Database
from .Product import Product
from .Utilities import Utilities

# EXT

# CORE
ProductsCache = {}

CurrentApp = None

# Functions
## MECHANICS
class CatalogueHandler():
    # Get Product holding collection
    @staticmethod
    def GetCatalogueCollection():
        # Functions
        # INIT
        Response = Database.GetDatabase()["Catalogue"]

        return Response

    # Get cached product object via string name
    @staticmethod
    def GetProductByName(ProductName):
        # Functions
        # INIT
        return ProductsCache.get(ProductName, None)

    # Get & Parse Products into Objects
    @staticmethod
    def GetProducts(JSON=False):
        # Functions
        # INIT
        if len(ProductsCache) != 0: # BASE CASE
            Products = [] # LIST

            for ProductName, ProductObject in ProductsCache.items():
                if JSON:
                    Products.append(ProductObject.GetDict(JSON=True))
                else:
                    Products.append(ProductObject)

            return Products


        Success, Result = Utilities.TryFor(3, 
            CatalogueHandler.GetCatalogueCollection().find,
        )

        if Success:
            for Record in (Result  or []):
                ProductObject = Product(Record)

                ProductsCache[ProductObject["Name"]] = ProductObject

            # RECURSION
            return CatalogueHandler.GetProducts(JSON=JSON)


##
def Initialise(App):
    # CORE
    global CurrentApp
    
    # Functions
    # INIT
    CurrentApp = App

    CatalogueHandler.GetProducts()