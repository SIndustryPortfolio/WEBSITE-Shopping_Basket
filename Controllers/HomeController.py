# MODULES
# INTERNAL
from Modules.Utilities import Utilities
from Modules.Shortcuts import Shortcuts
from Modules.CatalogueHandler import CatalogueHandler
from Modules.BasketHandler import BasketHandler
from Modules.BasketPricer import BasketPricer

# EXTERNAL
from flask import Blueprint, session, redirect, request
import copy

# CORE
BluePrint = Blueprint("Home", __name__)

CurrentApp = None

# Functions
# MECHANICS
def Initialise(App):
    # CORE
    global CurrentApp
    
    # Functions
    # INIT
    CurrentApp = App


# ROUTE CALLBACKS
def RootRouteCallback():
    # Functions
    # INIT
    BasketId = session.get("BasketId", None)

    # CREATE NEW BASKET
    if not Shortcuts.UserBasketExists(BasketId):
        BasketId = BasketHandler.New(Shortcuts.GetClientIP())
        session["BasketId"] = BasketId

    UserBasket = BasketHandler.GetBasket(BasketId)
    session["Costs"] = BasketPricer.CalculateCosts(UserBasket)

    Response = Shortcuts.RenderPage(
        "Home.html",
        "Home",
        Products = CatalogueHandler.GetProducts()
    )

    return Response

def ResetBasketRouteCallback():
    # Functions
    # INIT
    BasketId = session.get("BasketId", None)

    if BasketId != None:
        UserBasket = BasketHandler.GetBasket(BasketId)
        UserBasket.Clear()

    return redirect("/")

def UpdateBasketRouteCallback():
    # CORE
    Data = request.form
    
    # Functions
    # INIT
    BasketId = session.get("BasketId", None)

    if BasketId != None:
        UserBasket = BasketHandler.GetBasket(BasketId)

        UserBasket.Clear()

        for ProductName, Quantity in Data.items():
            for x in range(0, int(Quantity)):
                UserBasket.Add(copy.copy(CatalogueHandler.GetProductByName(ProductName)))

    return redirect("/")


# DIRECT
@BluePrint.route("/ResetBasket", methods=["POST"])
def HandleResetRoute():
    # Functions
    # INIT
    return Shortcuts.RouteFired(ResetBasketRouteCallback)

@BluePrint.route("/UpdateBasket", methods=["POST"])
def HandleAddRoute():
    # Functions
    # INIT
    return Shortcuts.RouteFired(UpdateBasketRouteCallback)
    

@BluePrint.route("/", methods=["GET"])
def HandleRootRoute():
    # Functions
    # INIT
    return RootRouteCallback()