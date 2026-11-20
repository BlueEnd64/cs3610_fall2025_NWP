from IAnimalClass import IAnimal

class elephants(IAnimal):
    """Concrete Product B"""

    @property
    def objType(self) -> str:
        return "elephants sound like "
    
    @property
    def say(self) -> str:
        return "trumpet"