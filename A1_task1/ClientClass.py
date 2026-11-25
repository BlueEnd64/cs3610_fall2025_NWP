from CalgaryZooClass import CalgaryZoo
from TorontoZooClass import TorontoZoo
from IZooClass import IZoo

class client():
    def __init__(self):
        self.__available_zoos = [TorontoZoo,CalgaryZoo]
        self.__selected_zoo: IZoo
        self.__outputFormat="test"
    
    def addZoo(zoo : IZoo) -> None:
        pass
    
    def removeZoo(zooName):
        pass
    
    def selectZoo(self, zooName):
        if zooName.lower()=='toronto':
            self.__selected_zoo=TorontoZoo
            return TorontoZoo()
        elif zooName.lower()=='calgary':
            self.__selected_zoo=CalgaryZoo
            return CalgaryZoo()
    
    
