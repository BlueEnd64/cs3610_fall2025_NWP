from IAnimalClass import IAnimal

class grizzlyBears(IAnimal):
    """Concrete Product B"""

    @property
    def objType(self) -> str:
        return "grizzly bears sound like "
    
    @property
    def say(self) -> str:
        return "Roaring"