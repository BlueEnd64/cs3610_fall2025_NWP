from IAnimalClass import IAnimal
from AnimalFactoryClass import AnimalFactory

from typing import Type
from abc import abstractmethod

class IZoo():
    def __init__(self) -> None:
        self._animals: list[Type[IAnimal]]=[]
    
    @property
    @abstractmethod
    def Animal(self) -> list:
        pass
    
    @property
    @abstractmethod
    def itinerary(self) -> str:
        pass
    
    @abstractmethod
    def askEachAnimalSaySomething():
        pass
    
    @abstractmethod
    def create_Animal() -> None:
        pass
    
    
    """
    def startVisit(self) -> None:
        self.create_Animal()
        for zoosAnimal in self._animals:
            print(zoosAnimal.say)
    """
    def startVisit(self) -> None:
        animals= self.Animal() 
        zoosAnimals=list(map(AnimalFactory.create_Animal,animals))
        
        print(self.itinerary())
        
        for zoosAnimal in zoosAnimals:
            if zoosAnimal:
                self._animals.append(zoosAnimal)
                print(zoosAnimal.objType + zoosAnimal.say) # this works but the creation of the animal objects come first, and the animal is not show doing it.  
