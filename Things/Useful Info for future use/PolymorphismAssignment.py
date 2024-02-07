# Creating parent class
class BMW_M5:
    Type = "M5"
    where = "German"

    def info(self):
        msg = "\nThe BMW {} is a {} luxury super saloon, ".format(self.Type, self.where)
        return msg

# Child class instance
class M5_Option(BMW_M5):
    curb_weight = 4000
    transmission = 'manual transmission'

    # Method
    def info(self):
        msg = "coming in at {}lbs and only available with a {}.".format(self.curb_weight, self.transmission)
        return msg

# Another child class instance
class M5_Motor(BMW_M5):
    engine_size = "4.4 liter v8"
    horsepower = 400

    # Method
    def info(self):
        msg = "the engine is a {} making over {} horsepower".format(self.engine_size, self.horsepower)
        return msg

if __name__ == "__main__":

    # Instane of parent class
    bmw_m5 = BMW_M5()
    print(bmw_m5.info())

    # Instance of first child class
    m5_option = M5_Option()
    print(m5_option.info())

    # Instance of second child class
    m5_motor = M5_Motor()
    print(m5_motor.info())


#NOTE TO SELF
    #TO CORRECTLY USE POLYMORPHISM, THE CHILD CLASSES ARE THEIR OWN CLASS BUT STILL A PART OF THE PARENTS CLASS.
    #CHILD CLASSES SHOULD WORK INTO THE PARENT CLASS WITHOUT HAVING TO DEFINE DIFFERENT METHODS, INSTEAD USE THE SAME METHOD TO "ADD INTO THE PARENT CLASS"
    
