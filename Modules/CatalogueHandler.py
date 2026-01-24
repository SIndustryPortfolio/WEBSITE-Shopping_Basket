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

# Functions
# MECHANICS

##
class CatalogueHandler():
    # Get Product holding collection
    @staticmethod
    def GetCatalogueCollection():
        # Functions
        # INIT
        Response = Database.GetDatabase()["Catalogue"]

        return Response

    # Get & Parse Products into Objects
    @staticmethod
    def GetProducts():
        # CORE
        Products = []

        # Functions
        # INIT
        Success, Result = Utilities.TryFor(1, 
            CatalogueHandler.GetCatalogueCollection().find,
        )

        if Success:
            for Record in (Result  or []):
                Products.append(Product(Record))

        return Products