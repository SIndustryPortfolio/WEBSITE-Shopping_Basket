# MODULES
# INT
from Utilities import Utilities

# EXT
from flask import session, request, render_template, make_response

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
    

class Shortcuts:
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
        return {
            "CoreInfo": CurrentApp.config["CoreInfo"] or {},
            "HostURL" : request.host_url or Shortcuts.GetHostURL()
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
        Response = make_response(render_template(
            TemplatePath,
            PageName = PageName,
            **KWArgs or {},
            **Shortcuts.GetPageEssentials()
        ))