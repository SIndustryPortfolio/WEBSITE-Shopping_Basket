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
def Initialise():
    # Functions
    # INIT
    App.config["CoreInfo"] = Utilities.LoadJson("static/JSON/Core.json")

    with App.app_context():
        Utilities.LoadModules(ModuleRegistry, RequiredModules, App)

        for Required in RequiredModules.values():
            if hasattr(Required, "BluePrint"):
                App.register_blueprint(Required.BluePrint)

        App.run(host=Host, port=Port, debug=Debug)

# CLEANUP vv
def End():
    # Functions
    # INIT
    for Required in RequiredModules.values():
        if hasattr(Required, "End"):
            Utilities.TryFor(1, Required.End)

# INIT
if __name__ == "__main__":
    #Utilities.TryFor(1, Initialise)
    Initialise()
    End()

