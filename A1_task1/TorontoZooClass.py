from IZooClass import IZoo


class TorontoZoo(IZoo):
    
    def __init__(self) -> None:
        super().__init__()
    
    def Animal(self):
        return ['lions','elephants','penguins','white bears']
    
    
    def itinerary(self):
        return "Welcome to the Toronto Zoo! Our Itinerary: 1) African Savanna. 2) Tundra Trek \n"
    
    """
    def startVisit(self) -> None:
        animals= self.Animal() 
        zoosAnimals=list(map(AnimalFactory.create_Animal,animals))
        
        for zoosAnimal in zoosAnimals:
            if zoosAnimal:
                self._animals.append(zoosAnimal)
                print(zoosAnimal.say) # this works but the creation of the animal objects come first, and the animal is not show doing it.  
                """
                

