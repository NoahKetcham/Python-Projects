class Vehicle:
    def __init__(self,make):
        self._make = make # This is a protected attribute
        self.__model = 'unknown' # This is a private attribute

    def set_model(self, model):
        self.__model = model # Allows you to set the private attribute from outside of the class, allowing controlled access to the attribute

    # A method to indirectly access the private attribute
    def access_model(self):
        print(f"The model of this {self._make} is {self.__model}.")
# Making the object
vehicle = Vehicle("BMW")
vehicle._make = "BMW"   #access the protected attribute
vehicle.set_model("M3") # set the private attribute using the "set_model" method.

vehicle.access_model()
