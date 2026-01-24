### READ
#
# - Product / "ORM" entity
#
###

# Modules
# INT

# EXT

# Functions
# MECHANICS

##
class Product:
    def __init__(self, Options):
        # CORE
        Public = {} # SUBSCRIPTABLE / [] Accessible
        Private = {} # HIDDEN

        # Functions
        # INIT
        Public["Name"] = Options.get("Name", None)
        Public["Price"] = Options.get("Price", 0)
        Public["Offer"] = Options.get("Options", {})

        self.Public = Public
        self.Private = Private

    def __getitem__(self, Key):
        # Functions
        # INIT
        return self.Public[Key]
    
    def items(self):
        # Functions
        # INIT
        return self.Public