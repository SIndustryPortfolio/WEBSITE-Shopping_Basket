# MODULES
# INTERNAL
from Modules.Utilities import Utilities
from Modules.Shortcuts import Shortcuts
from Modules.CatalogueHandler import CatalogueHandler

# EXTERNAL
from flask import Blueprint, session, redirect, url_for

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
    print("Rendering page")
    Response = Shortcuts.RenderPage(
        "Home.html",
        "Home",
        Products = CatalogueHandler.GetProducts()
    )

    print("Responded")

    return Response

def UpdateBasketRouteCallback():
    # Functions
    # INIT
    pass

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