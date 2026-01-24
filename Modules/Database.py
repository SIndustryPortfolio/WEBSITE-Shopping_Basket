# MODULES
# INT
from Utilities import Utilities

# EXT
from pymongo import MongoClient

# CORE
CurrentApp = None
Client = None

# Functions
# MECHANICS
def Initialise(App):
    # CORE
    global CurrentApp, Client

    # Functions
    # INIT
    CurrentApp = App

    Client = MongoClient(f"mongodb+srv://{App.config["DBUsername"]}:{App.config["DBKey"]}@public.x6tqh43.mongodb.net/?appName=Public")

##

class Database:
    @staticmethod
    def GetDatabase():
        return Client[CurrentApp.config["CoreInfo"]]