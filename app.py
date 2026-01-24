# Modules
# INIT
import os
import importlib

from Modules.Utilities import Utilities

# EXT
from flask import Flask

# CORE
App = Flask(__name__)

ModuleRegistry = {
    # SERVICES

    # CONTROLLERS
}

RequiredModules = {} # Bulk 

# Functions
# MECHANICS
def Initialise():
    # Functions
    # INIT
    with App.app_context():
        Utilities.LoadModules(ModuleRegistry, RequiredModules, App)

        for ModulePath in RequiredModules.items():
            Required = RequiredModules[ModulePath]

            if hasattr(Required, "BluePrint"):
                App.register_blueprint(Required.BluePrint)

# CLEANUP vv
def End():
    # Functions
    # INIT
    pass

# INIT
if __name__ == "__main__":
    Utilities.TryFor(1, Initialise)
    End()

