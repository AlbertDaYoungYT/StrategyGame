
from typing import Any
from currency import *
import os


class Configs:
    
    class _Credits__Config:
        
        def  __init__(self) -> None:
            self.credits_VALUE      = 1.0
            self.platinum_VALUE     = 50.0
            self.gold_VALUE         = 25.0
            self.silver_VALUE       = 10.0
    
    class _Platinum__Config:
        
        def  __init__(self) -> None:
            self.credits_VALUE      = 1.0
            self.platinum_VALUE     = 50.0
            self.gold_VALUE         = 25.0
            self.silver_VALUE       = 10.0
    
    class _Gold__Config:
        
        def  __init__(self) -> None:
            self.credits_VALUE      = 1.0
            self.platinum_VALUE     = 50.0
            self.gold_VALUE         = 25.0
            self.silver_VALUE       = 10.0
    
    class _Silver__Config:
        
        def  __init__(self) -> None:
            self.credits_VALUE      = 1.0
            self.platinum_VALUE     = 50.0
            self.gold_VALUE         = 25.0
            self.silver_VALUE       = 10.0
            
    
    class _Battlepass__Config:
        
        def __init__(self) -> None:
            pass
    
    class _Routes:
    
        class _Home__Config:
            routes               = {}
            routes["Index"]      = "/"
            
        


    class FileStructure:
        globals()["Structure"] = {}
        globals()["Structure"]["readable"] = {}
        
        globals()["Structure"]["resources"]         = "./resources/"
        globals()["Structure"]["logs"]              = "./logs/"
        globals()["Structure"]["data"]              = "./data/"
        
        
        # Inventory Items
        globals()["Structure"]["items"]             = "./resources/items/"
        globals()["Structure"]["materials"]         = "./resources/items/materials/"
        globals()["Structure"]["weapons"]           = "./resources/items/weapons/"
        globals()["Structure"]["armor"]             = "./resources/items/armor/"
        globals()["Structure"]["gems"]              = "./resources/items/gems/"
        
        # Characters and NPC's
        globals()["Structure"]["characters"]        = "./resources/characters/"
        globals()["Structure"]["npcs"]              = "./resources/npcs/"
        
        # Readable Text
        globals()["Structure"]["readable"]["EN"]    = "./resources/readable/en/"
        
    class GameConstraints():
        VERSION_PARTS = {1, 0, 0}
        SERVER_CONSOLE_UID = 99 # The UID of the server console's "player".
        BATTLE_PASS_MAX_LEVEL = 100
        BATTLE_PASS_POINT_PER_LEVEL = 1000
        BATTLE_PASS_POINT_PER_WEEK = 10000
        BATTLE_PASS_LEVEL_PRICE = 1000
        BATTLE_PASS_CURRENT_INDEX = 2
        
        
    
    def __init__(self) -> None:
        for k, v in Structure.items():
            if type(v) == dict:
                for sub_value in v.values():
                    os.makedirs(sub_value, exist_ok=True)
            else:
                os.makedirs(v, exist_ok=True)
            
# Testing the config system
if __name__ == '__main__':
    cfg = Configs()