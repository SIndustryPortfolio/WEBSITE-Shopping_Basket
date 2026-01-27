### READ
#
# - General usage short hands
#
###

# Module
# INT

# EXT
import json
import importlib
import time
import math
from datetime import datetime, timezone

# CORE

class Utilities:
    # Get Number of class objects in list / array
    @staticmethod
    def GetNumberOfObjects(Table, Class):
        # CORE
        Count = 0
        
        # Functions
        # INIT
        for Item in Table:
            if not isinstance(Item, Class):
                continue

            Count += 1

        return Count

    # Add many unpacked values to list
    @staticmethod
    def AddToTable(Table, *Values):
        # Functions
        # INIT
        for Value in Values:
            Table.append(Value)

    # Double clamp numbers, a range that cannot be exceeded
    @staticmethod
    def Clamp(Number, Min, Max):
        # Functions
        # INIT
        return max(Min, min(Number, Max))

    # Convert Minutes to Seconds. E.G: 2 Mins -> 120 Seconds
    @staticmethod
    def MinutesToSeconds(Minutes):
        # Functions
        # INIT
        return Minutes * 60

    # Get seconds since EPOC (1970 ish)
    @staticmethod
    def GetTick():
        # Functions
        # INIT
        return round(datetime.now(timezone.utc).timestamp(), 3)

    # Format large numbers. E.G: 10,000 -> 10K
    @staticmethod
    def FormatNumber(Number):
        # Functions
        # INIT
        try:
            Number = float(Number)
        except (TypeError, ValueError):
            return "nil"

        if Number <= 1000:
            return str(Number)


        Suffixes = ["K", "M", "B", "T", "q", "Q", "s", "S", "O", "N", "d", "U", "D"]

        if not isinstance(Number, (int, float)):
            return Number

        if Number < 10000:
            return math.floor(Number)

        Magnitude = math.floor(math.log10(Number) / 3) * 3
        Scaled = str(Number / (10 ** Magnitude))[:5]

        SuffixIndex = int(math.floor(Magnitude / 3)) - 1
        Suffix = Suffixes[SuffixIndex] if 0 <= SuffixIndex < len(Suffixes) else ""

        return f"{Scaled} {Suffix}"

    # Parse JSON file as Dict
    @staticmethod
    def LoadJson(Path):
        # Functions
        # INIT
        data = None

        with open(Path, "r", encoding="utf-8") as File:
            data = json.load(File)
        
        return data
    
    # Method retry-er, Good for API calls and fail safes (Not exactly a Promise object: that's soon to come!)
    @staticmethod
    def TryFor(Attempts, Function, *Args):
        # CORE
        Success = False
        Response = None

        # Functions
        # INIT
        for x in range(0, Attempts):
            try:
                Response = Function(*Args)
                Success = True
            except Exception as Error:
                Success = False
                Response = str(Error)
            
            if not Success:
                time.sleep(1)
            else:
                break

        return Success, Response

    # Module loader & initialiser, Centralised imports -> Prevents huge module-based bulk
    @staticmethod
    def LoadModules(Registry, RequiredModules, *Args):
        # Functions
        # INIT
        for ModulePath in Registry:
            Required = importlib.import_module(ModulePath)

            if hasattr(Required, "Initialise"):
                #Success, Error = Utilities.TryFor(1, Required.Initialise, *Args)
                Required.Initialise(*Args)

            RequiredModules[ModulePath] = Required
