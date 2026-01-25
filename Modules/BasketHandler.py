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
from .Utilities import Utilities

# EXT

# CORE
Baskets = {}

CurrentApp = None

# Functions
# MECHANICS
def DestroyCache(Key):
    # Functions
    # INIT
    Baskets.pop(Key, None)

def Heartbeat(RenderMeta):
    # CORE
    TimeNow = RenderMeta["TimeNow"]

    # Functions
    # INIT
    for Key, Cache in list(Baskets.items()): # Cloned dict
        LastInteractionTime = Cache["Time"]
        TimeSpan = TimeNow - LastInteractionTime
    
        if TimeSpan > Utilities.MinutesToSeconds(30):
            print("Destroying!!")
            DestroyCache(Key)


def Initialise(App):
    # CORE
    global CurrentApp

    # Functions
    # INIT
    CurrentApp = App

##

class BasketHandler():
    @staticmethod
    def FormatKey(Key):
        return str(Key)

    @staticmethod
    def New(Key):
        # CORE
        global Baskets

        Key = BasketHandler.FormatKey(Key)
        TimeNow = Utilities.GetTick()

        # Functions
        # INIT

        Baskets[Key] = {
            "Object" : Basket(),
            "Time" : TimeNow
        }

        return Key # Return KEY (IP)

    @staticmethod
    def GetBaskets():
        # CORE
        global Baskets

        # Functions
        # INIT
        return Baskets

    @staticmethod
    def GetBasket(Key):
        # CORE
        global Baskets

        TimeNow = Utilities.GetTick()
        Key = BasketHandler.FormatKey(Key)
        
        # Functions
        # INIT
        BasketMeta = Baskets.get(Key, {})
        BasketMeta["Time"] = TimeNow

        return BasketMeta.get("Object", None)

        
