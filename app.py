# Modules
# INIT
import os

from Modules.Utilities import Utilities

# EXT
from flask import Flask

# CORE
App = Flask(__name__)
Host = "0.0.0.0"
Port = os.environ.get("PORT", 5000)
Debug = True

App.config["DBUsername"] = "admin"
App.config["DBPassword"] = "admin"

ModuleRegistry = [
    # SERVICES
    "Modules.Shortcuts",
    "Modules.Database",

    # CONTROLLERS
    "Controllers.HomeController"
]

RequiredModules = {} # Imported Registry

# Functions
# MECHANICS
def Initialise():
    # Functions
    # INIT
    App.config["CoreInfo"] = Utilities.LoadJson("static/JSON/Core.json")

    with App.app_context():
        Utilities.LoadModules(ModuleRegistry, RequiredModules, App)

        for Required in RequiredModules.values():
            if hasattr(Required, "BluePrint"):
                App.register_blueprint(Required.BluePrint)

        print("RUNNING APP")
        App.run(host=Host, port=Port, debug=Debug)

# CLEANUP vv
def End():
    # Functions
    # INIT
    pass

# INIT
if __name__ == "__main__":
    Utilities.TryFor(1, Initialise)
    End()

