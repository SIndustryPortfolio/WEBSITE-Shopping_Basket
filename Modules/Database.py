### READ
#
# - NoSQL DB / MongoDB
#
###

# MODULES
# INT
from .Utilities import Utilities

# EXT
from pymongo import MongoClient

# CORE
CurrentApp = None
Client = None

# Functions
# MECHANICS
def Connect():
    # CORE
    global Client

    # Functions
    # INIT
    Client = MongoClient(f"mongodb+srv://{CurrentApp.config["DBUsername"]}:{CurrentApp.config["DBPassword"]}@public.x6tqh43.mongodb.net/?appName=Public")

def Initialise(App):
    # CORE
    global CurrentApp

    # Functions
    # INIT
    CurrentApp = App

    Utilities.TryFor(3, Connect)

def End():
    # Functions
    # INIT
    if Client != None:
        Client.close()

##

class Database:
    @staticmethod
    def GetDatabase():
        # Functions
        # INIT
        return Client[CurrentApp.config["CoreInfo"]["DB"]["ClusterName"]]
    
    @staticmethod
    def GetAndUpdateCounter(CollectionName): # FOR NUMBER BASED IDs ON RECORDS
        counterCollection = Database.getDatabase()["Counter"]

        document = counterCollection.find_one_and_update( 
            {"collection": CollectionName},
            {"$inc": {"count": 1}},
            upsert = True,
            return_document = True
        )

        return document["count"]