from ProductFactoryClass import ProductFactory
from IProductClass import IProduct

class FoodApp():
    
    def __init__(self):
        self._Dict ={'nonVegBurger':ProductFactory,'VegBurger':ProductFactory,'nonVegPizza':ProductFactory,'VegPizza':ProductFactory}
        self.AvailableFood=['nonVegBurger','VegBurger','nonVegPizza','VegPizza']
        self.order=[]
    
    
    def makeOrder(prodNames) -> list: #prodNames is a list, 
        
        #for product in prodNames:
            #res=ProductFactory.c
        pass
    
    def getOrderDescription()->str:
        pass