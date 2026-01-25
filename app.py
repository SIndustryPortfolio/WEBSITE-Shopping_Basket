# Modules
# INIT
import os
import threading

from Modules.Utilities import Utilities

# EXT
from flask import Flask

# CORE
App = Flask(__name__)
Host = "0.0.0.0"
Port = os.environ.get("PORT", 5000)
Debug = True
Alive = True

StartTime = None
MainThread = None

App.config["SECRET_KEY"] = "MySecretKey"
App.config["DBUsername"] = "admin"
App.config["DBPassword"] = "admin"

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
    global MainThread, StartTime

    Busy = False

    ##
    StartTime = Utilities.GetTick()
    LastBeatTime = StartTime

    # Functions
    # MECHANICS
    def Cycle(*Args):
        # Functions
        # INIT
        for Required in RequiredModules.values():
            if hasattr(Required, "Heartbeat"):
                Utilities.TryFor(1, Required.Heartbeat, *Args)

    def Render():
        # Functions
        # INIT
        while Alive:
            if Busy:
                return None
            
            Busy = True

            # CORE
            TimeNow = Utilities.GetTick()
            TotalTimeSpan = TimeNow - StartTime
            DeltaTime = TimeNow - LastBeatTime

            RenderMeta = { # Packaged
                "DeltaTime" : DeltaTime,
                "AccumulatedTime": TotalTimeSpan,
                "TimeNow" : TimeNow
            }

            Cycle(RenderMeta)

            Busy = False


    # INIT
    MainThread = threading.Thread(target=Render)
    MainThread.daemon = True
    MainThread.start()

    
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
        App.run(host=Host, port=Port, debug=Debug)

# CLEANUP vv
def End():
    # Functions
    # INIT
    Alive = False

    for Required in RequiredModules.values():
        if hasattr(Required, "End"):
            Utilities.TryFor(1, Required.End)

# INIT
if __name__ == "__main__":
    #Utilities.TryFor(1, Initialise)
    Initialise()
    End()

