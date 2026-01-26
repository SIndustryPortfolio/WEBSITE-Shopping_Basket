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
    # CORE
    Costs = session.get("Costs", {})

    # Functions
    # INIT
    print("Rendering page")
    Response = Shortcuts.RenderPage(
        "Home.html",
        "Home",
        Products = CatalogueHandler.GetProducts(),
        Costs = Costs
    )

    return Response

def UpdateBasketRouteCallback():
    # CORE
    Data = request.form
    
    # Functions
    # INIT
    BasketId = session.get("BasketId", None)
    UserBasket = BasketHandler.GetBasket(BasketId)

    UserBasket.Clear()

    for ProductName, Quantity in Data.items():
        for x in range(0, int(Quantity)):
            UserBasket.Add(copy.copy(CatalogueHandler.GetProductByName(ProductName)))

    session["Costs"] = BasketPricer.CalculateCosts(UserBasket)

    return redirect("/")


# DIRECT
@BluePrint.route("/UpdateBasket", methods=["POST"])
def HandleAddRoute():
    # Functions
    # INIT
    return Shortcuts.RouteFired(UpdateBasketRouteCallback)
    

@BluePrint.route("/", methods=["GET"])
def HandleRootRoute():
    # Functions
    # INIT
    print("ROUTE FIRED")
    return RootRouteCallback()