from abc import ABC, abstractmethod
from IProductClass import IProduct

class Pizza(IProduct):
    
    def get_Price(self):
            return {"price":self.__price}
            
    def get_Description(self):
        return {"descr":self.__descr}