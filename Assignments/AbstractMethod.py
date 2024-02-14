from abc import ABC, abstractmethod

#Define your class as abstract
class IceCreamFlavor(ABC):
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def getFlavor(self):
        pass

    def printFlavor(self):
        return (f"This flavor of ice cream is {self.name}.")
    

#Child class for this flavor
class Vanilla(IceCreamFlavor):
    def getFlavor(self):
        return ("Rich taste with strong hints of vanilla bean")
    
#Instantiate the object
vanilla = Vanilla("Vanilla Bean")
print (vanilla.printFlavor(), vanilla.getFlavor())
    
