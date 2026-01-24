# Module
# INIT
import json
import importlib
import asyncio

# CORE

class Utilities:
    @staticmethod
    def LoadJson(Path):
        # Functions
        # INIT
        data = None

        with open(Path, "r", encoding="utf-8") as File:
            data = json.load(File)
        
        return data
    
    @staticmethod
    async def TryFor(Attempts, Function, *Args):
        # CORE
        Success = False
        Response = None

        # Functions
        # INIT
        for x in range(0, Attempts):
            try:
                Response = await Function(*Args)
                Success = True
            except Exception as Error:
                Success = False
                Response = str(Error)
            
            if not Success:
                await asyncio.sleep(1)
            else:
                break

        return Success, Response

    @staticmethod
    def LoadModules(Registry, RequiredModules, *Args):
        # Functions
        # INIT
        for ModulePath in Registry:
            Required = importlib.import_module(ModulePath)

            if hasattr(Required, "Initialise"):
                Success, Error = Utilities.TryFor(1, Required.Initialise, *Args)
            
            RequiredModules[ModulePath] = Required
