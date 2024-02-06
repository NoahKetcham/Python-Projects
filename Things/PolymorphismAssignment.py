
#Creating parent class
class BMW:
    where = "Munich, Germany"
    Type = "car manufacturer"

    def info(brand):
        msg = "\nBMW is based in {} and they are a luxury {}, some of the more exciting models include ".format(brand.where,brand.Type)
        return msg

#Child class instance
class M3(BMW):
    chassis_code = 'e36'
    horsepower = 220
    weight = 3100
#method
    def spec(model):
        msg = "the {} M3, which is a midsize luxury sportscar with a horsepower of {} and a curb weight of {}lbs.".format(model.chassis_code,model.horsepower,model.weight)
        return msg

#Another child class instance
class M5(BMW):
    chassis_code = 'e39'
    horsepower = 400
    weight = 4000
#method
    def spec(model):
        msg = "The {} M5, which is a large luxury super saloon with a horsepower of {} and a curb weight of {}lbs.".format(model.chassis_code,model.horsepower,model.weight)
        return msg

if __name__ == "__main__":
    M3 = M3()
    print(M3.info())
    print(M3.spec())

    M5 = M5()
    print(M5.info())
    print(M5.spec())


    
