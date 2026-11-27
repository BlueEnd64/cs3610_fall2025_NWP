from IZooClass import IZoo
from LionsClass import lions
from ElephantsClass import elephants
from PenguinsClass import penguins
from PolarBearsClass import polarBears

class TorontoZoo(IZoo):
    
    def __init__(self) -> None:
        super().__init__()
        self.__name="toronto"
        self.__animals=['lions','elephants','penguins','white bears']
    
    
    def create_animals(self) -> list:
        return [lions, elephants ,penguins,polarBears]
    
    def get_itinerary(self):
        return "\nWelcome to the Toronto Zoo! Our Itinerary: 1) African Savanna. 2) Tundra Trek \n"
    
    
                

