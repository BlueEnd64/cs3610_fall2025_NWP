from abc import ABC, abstractmethod
from BurgerClass import Burger
from PizzaClass import Pizza

class ProductFactory(ABC):
    
    
    @staticmethod
    @abstractmethod
    def createBurger(p,c,d) -> Burger:
        pass
    
    @staticmethod
    @abstractmethod
    def createPizza(p,c,s,d) -> Pizza:
        pass
    