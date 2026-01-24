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

        
