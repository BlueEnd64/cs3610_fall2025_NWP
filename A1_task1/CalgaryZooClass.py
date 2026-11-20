from IZooClass import IZoo


class CalgaryZoo(IZoo):
    
    def __init__(self) -> None:
        super().__init__()
    
    
    def Animal(self) -> list:
        return ['penguins','grizzly bears', 'moose']
    
    
    def itinerary(self):
        return "Welcome to the Calgary Zoo! Our Itinerary: 1) Penguin Plunge. 2) Wild Canad \n"
    
    """
    def startVisit(self) -> None:
            animals= self.Animal() 
            zoosAnimals=list(map(AnimalFactory.create_Animal,animals))
            
            for zoosAnimal in zoosAnimals:
                if zoosAnimal:
                    self._animals.append(zoosAnimal)
    """