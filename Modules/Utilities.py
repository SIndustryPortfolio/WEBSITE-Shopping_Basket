### READ
#
# - General usage short hands
#
###

# Module
# INT
import json
import importlib
import time
import math
from datetime import datetime, timezone

# CORE

class Utilities:
    # Get Milliseconds since EPOC (1970 ish)
    @staticmethod
    def GetTick():
        # Functions
        # INIT
        return datetime.now(timezone.utc).timestamp() * 1000

    # Format 10,000 -> 10K
    @staticmethod
    def FormatNumber(Number):
        # Functions
        # INIT
        try:
            Number = float(Number)
        except (TypeError, ValueError):
            return "nil"

        if Number <= 1000:
            return Number


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
