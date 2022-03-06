from Vehicle import Vehicle

class Ship(Vehicle):
    # constructor
    def __init__(self):
        super().__init__()
        self.__age = 0
        self.__type = "<No Input>"
        self.__countryOfManufacture = "<No Input>"

    # setter
    def setDataShip(self, age, shipType, com):
        self.__age = age
        self.__type = shipType
        self.__countryOfManufacture = com

    def setAge(self, age):
        self.__age = age

    def setType(self, type):
        self.__type = type

    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture

    # getter
    def getAge(self):
        return self.__age

    def getType(self):
        return self.__type

    def getCountryOfManufacture(self):
        return self.__countryOfManufacture

    # method
    def printShip(self):
        print("Type                   : ", self.getType())
        print("Age                    : ", self.getAge(), "Years Old")
        print("Country of Manufacture : ", self.getCountryOfManufacture())
        self.printVehicle()
        self.move(self.getType())
        print("------------------------------------------------------")
