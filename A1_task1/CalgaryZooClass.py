from IZooClass import IZoo


class CalgaryZoo(IZoo):
    
    def __init__(self) -> None:
        super().__init__()
        self.__Itinerary="Welcome to the Calgary Zoo! Our Itinerary: 1) Penguin Plunge. 2) Wild Canada"
        self.__animals=['penguins','grizzly bears', 'moose']
    
    def create_animals(self) -> list:
            return ['penguins','grizzly bears', 'moose']
    
    def get_itinerary(self):
        return self.__Itinerary
    
    