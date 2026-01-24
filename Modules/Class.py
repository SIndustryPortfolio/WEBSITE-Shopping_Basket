### READ
#
# - Super class!
# - Adds better support for subscriptable objects
# - In theory: As the front end is in JavaScript, it's less confusing to index Python objects like JSON tables
#
###

# Modules
# INT

# EXT

class Class:
    def __init__(self):
        # CORE
        Public  = {} # Subscriptable / [] Accessible
        Private = {} # Hidden

        # Functions
        # INIT
        self.Public = Public
        self.Private = Private
    
    # Shorthand for subscriptatble ([] indexing) -> PREFERABLE TO SEPARATE SYNTAX
    def __getitem__(self, Key):
        # Functions
        # INIT
        return self.Public.get(Key, None)
    
    # Return subscriptable (Treat object like dict)
    def items(self):
        # Functions
        # INIT
        return self.Public
        