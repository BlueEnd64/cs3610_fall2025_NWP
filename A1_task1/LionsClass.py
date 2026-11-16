from A1_task1.IAnimalClass import IAnimal

class lions(IAnimal):
    """Concrete Product A"""

    @property
    def objType(self) -> str:
        return "I am Class A"
    
    @property
    def say(self) -> str:
        return "Roaring"