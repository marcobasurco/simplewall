# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = False
#     def login(self):
#         self.logged = True
#         print(self.name + " is logged in. ")
#         return self

# new_user = User("Anna","anna@anna.com")
# print(new_user.name)


# class User:
#     name = "Anna"



# anna = User()
# print("anna's name:", anna.name)
# User.name = "Bob"
# print("anna's name after change:", anna.name)
# # bob = User()
# # print("bob's name:", bob.name)
# marco = User()
# print(marco.name)


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = False


# user1 = User("Anna Propas", "anna@anna.com")
# print(user1.name)
# print(user1.logged)
# print(user1.email)


# class Bike:
#     def __init__(self, price, max_speed, miles=0):
#         self.price = price
#         self.max_speed = max_speed
#         self.miles = miles

#     def displayInfo(self):
#         print("The price is " + str(self.price))
#         print("The maximum speed that you can achieve is " + str(self.max_speed))
#         print("This bike has run " + str(self.miles))

#     def ride(self):
#         self.miles += 10
#         return self

#     def reverse(self):
#         if (self.miles > 0):
#             self.miles -= 5
#         return self


# bike1 = Bike(10, 10)
# bike1.ride().ride().ride().reverse()
# bike1.displayInfo()

# bike2 = Bike(200, 20, 130)
# bike2.ride().ride().ride().reverse()
# bike2.displayInfo()

# bike3 = Bike(300, 50)
# bike3.ride().ride().ride().reverse()
# bike3.displayInfo()


# class Cars:
#     def __init__(self, price, speed, fuel, mileage, tax=0):
#         self.price = price
#         self.speed = speed
#         self.fuel = fuel
#         self.mileage = mileage
#         self.tax = tax

#         def display_all(self):
#             print("Price: " + str(self.price))
#             print("Speed: " + str(self.speed))
#             print("Fuel: " + str(self.fuel))
#             print("Mileage: " + str(self.mileage))
#             if(self.price > 10000):
#                 self.tax = 0.15
#             else:
#                 self.tax = 0.12
#             print("Tax: " + str(self.tax)+"\n")
#         display_all(self)


# car1 = Cars(10000, "180 Mph", "Full", "35mpg")
# car1 = Cars(15000, "180 Mph", "Full", "55mpg")
# car1 = Cars(2000, "220 Mph", "Empty", "35mpg")
# car1 = Cars(25000, "220 Mph", "Full", "25mpg")
# car1 = Cars(5000, "220 Mph", "Half", "45mpg")
# car1 = Cars(48000, "220 Mph", "Half", "15mpg")


# class Product:
#     def __init__(self, price, itemName, weight, brand, status="for sale"):
#         self.price = price
#         self.itemName = itemName
#         self.weight = weight
#         self.brand = brand
#         self.status = status

#     def sell(self, tax):
#         self.status = "sold"
#         print("\nThe item: " + str(self.itemName) +
#               "\nPrice before taxes is: " + str(self.price))
#         self.price = self.price + ((self.price * tax)/100)
#         print("\nTax amount charged: " + str(tax) + " percent." +
#               "\nPrice after taxes: " + str(self.price))
#         print("\nNew current item status: " + str(self.status))
#         return self

#     def saleReturns(self, reason_for_return):
#         if(reason_for_return == "defective"):
#             self.status = "defective"
#             self.price = 0
#             print("\nThis item is: " + str(self.status) +
#                   " and is not longer for sale")
#             print("Current item price: " + str(self.price))
#         elif(reason_for_return == "like_new"):
#             self.status = "for sale"
#             print(
#                 "\nThis item is like new and the current status shows: " + str(self.status))
#         elif(reason_for_return == "opened"):
#             self.status = "used"
#             self.price = self.price * 0.8
#             print("Open Box status: " + str(self.status))
#             print("20% discounted price: " + str(self.price))
#         return self

#     def displayInfo(self):
#         print("\n\n\nProduct Name: " + str(self.itemName) + "\nProduct Price: " + str(self.price) + "\nProduct Weight: " +
#               str(self.weight) + "\nProduct Brand: " + str(self.brand) + "\nProduct Availability Status: " + str(self.status))

# # gameConsole = Product(100,"Game Console", "12 pounds", "Nintendo")


# # gameConsole.sell(8)

# watch = Product(5000, "rolex", "50 pounds", "rolex")
# # watch.sell(1)
# watch.saleReturns("defective")
# # watch.displayInfo()

# # gameConsole.saleReturns("defective")
# # gameConsole.saleReturns("like_new")
# # gameConsole.saleReturns("opened")


class Vehicle:
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        return self

    def reverse(self, miles):
        self.mileage -= miles
        return self


class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"


class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self


class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self


v = Vehicle(4, 8, "dodge", "minivan")
print(v.make)
b = Bike(2, 1, "Schwinn", "Paramount")
print(b.vehicle_type())
c = Car(8, 5, "Toyota", "Matrix")
c.set_wheels()
print(c.wheels)
a = Airplane(22, 853, "Airbus", "A380")
a.fly(580)
print(a.mileage)
