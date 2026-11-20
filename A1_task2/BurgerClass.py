from abc import ABC, abstractmethod
from IProductClass import IProduct

class Burger(IProduct):
    
    def get_Price(self) -> str:
            return self._price
            
    def get_Description(self):
        return {"descr":self._descr}