
from typing import Any
from config import *

class Credits:
    
    def __init__(self, credit) -> None:
        self.credits     = credit
        self.platinum    = credit / Configs.__Config().platinum_VALUE
        self.gold        = credit / Configs.__Config().gold_VALUE
        self.silver      = credit / Configs.__Config().silver_VALUE

class Platinum:
    
    def __init__(self, platinum) -> None:
        self.credits     = platinum * Configs.__Config().platinum_VALUE
        self.platinum    = platinum
        self.gold        = (platinum * Configs.__Config().platinum_VALUE) / Configs.__Config().gold_VALUE
        self.silver      = (platinum * Configs.__Config().platinum_VALUE) / Configs.__Config().silver_VALUE


class Gold:
    
    def __init__(self, gold) -> None:
        self.credits     = gold * Configs.__Config().gold_VALUE
        self.platinum    = (gold * Configs.__Config().gold_VALUE) / Configs.__Config().platinum_VALUE
        self.gold        = gold
        self.silver      = (gold * Configs.__Config().gold_VALUE) / Configs.__Config().silver_VALUE


class Silver:
    
    def __init__(self, silver) -> None:
        self.credits     = silver * Configs.__Config().silver_VALUE
        self.platinum    = (silver * Configs.__Config().silver_VALUE) / Configs.__Config().platinum_VALUE
        self.gold        = (silver * Configs.__Config().silver_VALUE) / Configs.__Config().gold_VALUE
        self.silver      = silver
    
    


if  __name__ == "__main__":
    # Testing the class and its methods.
    c = Credits(10)
    c1 = Credits(c.credits)
    c2 = Platinum(c.platinum)
    c3 = Gold(c.gold)
    c4 = Silver(c.silver)
    
    print("Is Credits Values Accurate:\t", c1.credits == c2.credits == c3.credits == c4.credits)
    print("Is Platinum Values Accurate:\t", c1.platinum == c2.platinum == c3.platinum == c4.platinum)
    print("Is Gold Values Accurate:\t", c1.gold == c2.gold == c3.gold == c4.gold)
    print("Is Silver Values Accurate:\t", c1.silver == c2.silver == c3.silver == c4.silver)
    