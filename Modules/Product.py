### READ
#
# - Product / "ORM" entity
#
###

# Modules
# INT
from .Class import Class

# EXT

# Functions
# MECHANICS

##
class Product(Class):
    def __init__(self, Options):
        # CORE
        super().__init__()

        # Functions
        # INIT
        self.Public["Name"] = Options.get("Name", None)
        self.Public["Price"] = Options.get("Price", 0)
        self.Public["Offer"] = Options.get("Options", {})