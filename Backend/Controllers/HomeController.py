### READ
#
# - Home page "/"
# - Handles Session reset / New user join
#
###

# MODULES
# INTERNAL
from ..Modules.Utilities import Utilities
from ..Modules.Shortcuts import Shortcuts

# EXTERNAL
from flask import Blueprint, session, redirect, request

# CORE
# CORE
BluePrint = Blueprint("Home", __name__)

CurrentApp = None

# Functions
# MECHANICS


# ROUTE CALLBACKS
def RootRouteCallback():
    # Functions
    # INIT
    return Shortcuts.RenderPage(
        "Home.html",
        "Home"
        )

##
def Initialise(App):
    # CORE
    global CurrentApp

    # Functions
    # INIT
    CurrentApp = App


@BluePrint.route("/", methods=["GET"])
def HandleRootRoute():
    # Functions
    # INIT
    Shortcuts.AddRequest()
    return RootRouteCallback()