#Create parent class
class Restaurant:
    name = 'bobs pizza' #VALUES
    email = 'bobspiaza@yahoo.com' #VALUES
    address = '1234 se 4th st' #VALUES
    franchise = 1 #VALUES

#Child class 1
class menu(Restaurant): #Input parent class within () to inherit attributes
    pizza_price = 16 #VALUES
    topping_price = 1 #VALUES

#Child class 2
class cost(Restaurant):
    dough = 2 #VALUES
    marinara_sauce = 1 #VALUES
    cheese = 1 #VALUES
    
