from IAnimalClass import IAnimal

class penguins(IAnimal):
    """Concrete Product B"""

    @property
    def objType(self) -> str:
        return "penguins sound like "
    
    @property
    def say(self) -> str:
        return "noot noot"