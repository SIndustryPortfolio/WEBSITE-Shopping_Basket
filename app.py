# Modules
# INIT
import os
import threading
import time

from Modules.Utilities import Utilities

# EXT
from flask import Flask

# CORE / CONFIG
## WEB SERVER
App = Flask(
    __name__,
    static_folder="Static",
    static_url_path="/Static",
    template_folder="Templates"
)

AppHost = "0.0.0.0"
AppPort = os.environ.get("PORT", 5000)
AppDebug = True
AppAlive = True
## HEARTBEAT
HeartbeatBusy = False
HeartbeatStartTime = None
HeartbeatMainThread = None
## CONFIG
App.config["SECRET_KEY"] = "MySecretKey"
App.config["DBUsername"] = "admin"
App.config["DBPassword"] = "admin"

## CORE
ModuleRegistry = [
    # SERVICES
    "Modules.Shortcuts",
    "Modules.Database",
    "Modules.BasketHandler",

    # CONTROLLERS
    "Controllers.HomeController"
]

RequiredModules = {} # Imported Registry

# Functions
# MECHANICS
def Heartbeat():
    # CORE
    global HeartbeatStartTime

    ##
    HeartbeatStartTime = Utilities.GetTick()
    LastBeatTime = HeartbeatStartTime

    # Functions
    # MECHANICS
    def Cycle(*Args):
        # Functions
        # INIT
        for Required in RequiredModules.values():
            if hasattr(Required, "Heartbeat"):
                Utilities.TryFor(1, Required.Heartbeat, *Args)

    def Render():
        # CORE
        global HeartbeatBusy

        # Functions
        # INIT
        while AppAlive:
            # Skip on busy
            if HeartbeatBusy:
                return None
            
            HeartbeatBusy = True

            # CORE
            TimeNow = Utilities.GetTick()
            TotalTimeSpan = TimeNow - HeartbeatStartTime
            DeltaTime = TimeNow - LastBeatTime

            RenderMeta = { # Packaged
                "DeltaTime" : DeltaTime,
                "AccumulatedTime": TotalTimeSpan,
                "TimeNow" : TimeNow
            }

            Cycle(RenderMeta)

            time.sleep(0.005)

            HeartbeatBusy = False


    # INIT
    HeartbeatMainThread = threading.Thread(target=Render)
    HeartbeatMainThread.daemon = True
    
    Utilities.TryFor(1, HeartbeatMainThread.start)

    
def Initialise():
    # Functions
    # INIT
    App.config["CoreInfo"] = Utilities.LoadJson("static/JSON/Core.json")

    with App.app_context():
        Utilities.LoadModules(ModuleRegistry, RequiredModules, App)

        for Required in RequiredModules.values():
            if hasattr(Required, "BluePrint"):
                App.register_blueprint(Required.BluePrint)


        Heartbeat()
        App.run(host=AppHost, port=AppPort, debug=AppDebug)

# CLEANUP vv
def End():
    # CORE
    global AppAlive

    # Functions
    # INIT
    AppAlive = False

    for Required in RequiredModules.values():
        if hasattr(Required, "End"):
            Utilities.TryFor(1, Required.End)

# INIT
if __name__ == "__main__":
    #Utilities.TryFor(1, Initialise)
    Initialise()
    End()

