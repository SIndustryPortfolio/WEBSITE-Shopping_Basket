### READ
#
# - Site specific short hands
#
###

# MODULES
# INT
from .Utilities import Utilities
from .BasketHandler import BasketHandler
from .Product import Product

# EXT
from flask import session, request, render_template, make_response, redirect

# CORE
CurrentApp = None

# Functions
# MECHANICS
class Shortcuts:
    @staticmethod
    def GetNumberOfProducts(Table, ItemOrItemName):
        # CORE
        Count = 0

        # Functions
        # INIT
        if isinstance(ItemOrItemName, Product):
            ItemOrItemName = ItemOrItemName["Name"]
        
        for Item in Table:
            if Item["Name"] != ItemOrItemName:
                continue

            Count += 1

        return Count

    @staticmethod
    def UserBasketExists(BasketId):
        # Functions
        # INIT
        return (BasketId != None and BasketHandler.GetBasket(BasketId) != None)

    @staticmethod
    def RouteFired(RouteCallback, *Args):
        # CORE
        BasketId = session.get("BasketId", None)
        
        # Functions
        # INIT
        if not Shortcuts.UserBasketExists(BasketId):
            return redirect("/")
        
        #Success, Response = Utilities.TryFor(1, RouteCallback, *Args)
        
        #return Response
        return RouteCallback(*Args)

    @staticmethod
    def GetHostURL():
        # Functions
        # INIT
        Host = CurrentApp.config["HOST"]
        Port = CurrentApp.config["PORT"]
        Scheme = "http"

        return f"{Scheme}://{Host}:{Port}"

    @staticmethod
    def GetPageEssentials():
        # Functions
        # INIT
        BasketId = session.get("BasketId", None)

        if not Shortcuts.UserBasketExists(BasketId):
            BasketId = BasketHandler.New(Shortcuts.GetClientIP())
            session["BasketId"] = BasketId

        return {
            "CoreInfo": CurrentApp.config["CoreInfo"] or {},
            "HostURL" : request.host_url or Shortcuts.GetHostURL(),
            "Basket": BasketHandler.GetBasket(BasketId),
            "Utilities": Utilities
        }
        

    @staticmethod
    def GetClientIP():
        # CORE
        RequestIP = None
        
        # Functions
        # INIT
        if request.headers.getlist("X-Forwarded-For"):
            RequestIP = request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
        else:
            RequestIP = request.remote_addr
        
        return RequestIP

    @staticmethod
    def RenderPage(TemplatePath, PageName, **KWArgs):
        # Functions
        # INIT
        Packaged = {
            **Shortcuts.GetPageEssentials(),
            **(KWArgs or {}),
            "PageName": PageName,
        }
       
        Response = make_response(render_template(TemplatePath, **Packaged))

        return Response
    
##
def Initialise(App):
    # CORE
    global CurrentApp

    # Functions
    # INIT
    CurrentApp = App