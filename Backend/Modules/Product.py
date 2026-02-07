### READ
#
# - Product / "ORM" entity
# - Standalone Item from catalogue
#
###

# Modules
# INT
from .Class import Class
#from .OffersHandler import Offers
#from .Utilities import Utilities

# EXT

# Functions
# MECHANICS

##
class Product(Class):
    def __init__(self, Options):
        # CORE
        super().__init__()

        # Functions
        # INIT
        self.Public["Name"] = Options.get("Name", None)
        self.Public["Price"] = Options.get("Price", 0)

        ## DEPRECATED, Superseded by Offershandler ## 
        #############################################
        
        #OfferInfo = Options.get("Offer", None)

        #if OfferInfo != None:
        #    OfferObject = Offers.GetOffer(OfferInfo["Type"])(OfferInfo)
        #    self.Public["Offer"] = OfferObject

        