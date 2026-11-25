from IAnimalClass import IAnimal
# from AnimalFactoryClass import AnimalFactory

from typing import Type
from abc import abstractmethod

class IZoo():
    def __init__(self) -> None:
        self.__animals: list[IAnimal]
        self.__name: str
    
    def get_itinerary(self) -> str:
        pass
    
    @abstractmethod
    def create_animals() -> None:
        pass
    
    def show_animals(self) -> None:
        animals= self.create_animals() 
        # zoosAnimals=list(map(AnimalFactory.create_Animal,animals))
        
        for zoosAnimal in animals:
            
            if zoosAnimal:
                #self.__animals.append(zoosAnimal)
                print(zoosAnimal.say()) # this works but the creation of the animal objects come first, and the animal is not show doing it.  
    