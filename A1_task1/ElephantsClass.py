from A1_task1.IAnimalClass import IAnimal

class elephants(IAnimal):
    """Concrete Product B"""

    @property
    def objType(self) -> str:
        return "I am Class B"
    
    @property
    def say(self) -> str:
        return "trumpet"