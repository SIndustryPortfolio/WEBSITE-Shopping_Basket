# Modules
# INIT
import os

from Modules.Utilities import Utilities

# EXT
from flask import Flask

# CORE
App = Flask(__name__)
Host = "0.0.0.0"
Port = os.environ.get("Port", 5000)
Debug = True

App.config["DBUsername"] = "mdb_sa_id_6974e092fc710c6947e9b866"
App.config["DBKey"] = "mdb_sa_sk_8TIPaAlQLIA3qk6NMi3BsEWt0Xgxy9TeGCcTPDC2"

ModuleRegistry = {
    # SERVICES
    "Modules.Shortcuts",
    "Modules.Database",

    # CONTROLLERS
    "Controllers.HomeController"
}

RequiredModules = {} # Imported Registry

# Functions
# MECHANICS
def Initialise():
    # Functions
    # INIT
    App.config["CoreInfo"] = Utilities.LoadJson("static/JSON/Core.json")

    with App.app_context():
        Utilities.LoadModules(ModuleRegistry, RequiredModules, App)

        for ModulePath in RequiredModules.items():
            Required = RequiredModules[ModulePath]

            if hasattr(Required, "BluePrint"):
                App.register_blueprint(Required.BluePrint)

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

