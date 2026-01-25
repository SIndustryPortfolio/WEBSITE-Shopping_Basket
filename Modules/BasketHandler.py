### READ
#
# - Session holder
# - Caches User-made baskets into a TTL cache
# - Cache expires after 30 Minutes of Idle!
# - As this is a demo, I map the baskets to Client IP strings
# 
###

# MODULES
# INT
from .Basket import Basket

# EXT

# CORE
Baskets = {}
CurrentApp = None

# Functions
# MECHANICS
def Initialise(App):
    # CORE
    global CurrentApp

    # Functions
    # INIT
    CurrentApp = App

##

class BasketHandler():
    @staticmethod
    def New(IP):
        # Functions
        # INIT
        Baskets[IP] = Basket()

        return IP # Return KEY
    
    @staticmethod
    def GetBasket(Key):
        # CORE
        global Baskets
        
        # Functions
        # INIT
        return Baskets.get(Key, None)

        
