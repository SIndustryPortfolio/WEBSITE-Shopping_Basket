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


# DIRECT
@BluePrint.route("/")
def PageHandler():
    # Functions
    # INIT
    return Shortcuts.RenderPage(
        "Home.html",
        "Home",
        Products = CatalogueHandler.GetProducts()
    )
