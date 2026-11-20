from IAnimalClass import IAnimal

class whiteBears(IAnimal):
    """Concrete Product B"""

    @property
    def objType(self) -> str:
        return "white bears sound like"
    
    @property
    def say(self) -> str:
        return "Growling"