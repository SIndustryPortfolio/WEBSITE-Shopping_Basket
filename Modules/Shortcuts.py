### READ
#
# - Site specific short hands
#
###

# MODULES
# INT
from .Utilities import Utilities
from .Basket import Basket

# EXT
from flask import session, request, render_template, make_response, redirect

# CORE
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

class Shortcuts:
    @staticmethod
    def RouteFired(RouteCallback, *Args):
        # CORE
        UserBasket = session.get("Basket", None)
        
        # Functions
        # INIT
        if UserBasket == None:
            return redirect("/")
        
        return Utilities.TryFor(1, RouteCallback, *Args)
        
    
    @staticmethod
    def GetHostURL():
        # Functions
        # INIT
        Host = CurrentApp.config.get("HOST", "127.0.0.1")
        Port = CurrentApp.config.get("PORT", 5000)
        Scheme = "http"

        return f"{Scheme}://{Host}:{Port}"

    @staticmethod
    def GetPageEssentials():
        # Functions
        # INIT
        if not session.get("Basket", None):
            session["Basket"] = Basket()

        return {
            "CoreInfo": CurrentApp.config["CoreInfo"] or {},
            "HostURL" : request.host_url or Shortcuts.GetHostURL(),
            "Basket": session.get("Basket").items()
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
        
        print("1")
        Packaged = {
            **Shortcuts.GetPageEssentials(),
            **(KWArgs or {}),
            "PageName": PageName,
        }
       
        print("2")
        Response = make_response(render_template(TemplatePath, **Packaged))
        print("3")

        return Response