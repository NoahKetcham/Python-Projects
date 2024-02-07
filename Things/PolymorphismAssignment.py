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
    def Option(self):
        msg = "coming in at {}lbs and only available with a {}.".format(self.curb_weight, self.transmission)
        return msg

# Another child class instance
class M5_Motor(BMW_M5):
    engine_size = "4.4 liter v8"
    horsepower = 400

    # Method
    def Motor(self):
        msg = "the engine is a {} making over {} horsepower".format(self.engine_size, self.horsepower)
        return msg

if __name__ == "__main__":
    option = M5_Option()
    motor = M5_Motor()

    print(option.info())  # Calling info method from M5_Option instance which inherits BMW_M5
    print(option.Option())  # Calling Option method from M5_Option instance

    print(motor.info())  # Calling info method from M5_Motor instance which inherits BMW_M5
    print(motor.Motor())  # Calling Motor method from M5_Motor instance
