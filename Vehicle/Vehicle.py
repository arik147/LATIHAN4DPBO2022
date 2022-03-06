class Vehicle:
    # constructor
    def __init__(self):
        self.__fuelType = "<No Input>"
        self.__maxPassanger = 0
        self.__name = "<No Input>"

    # setter
    def setDataVehicle(self, fuelType, maxPassanger):
        self.__fuelType = fuelType
        self.__maxPassanger = maxPassanger

    def setName(self, name):
        self.__name = name

    def setFuelType(self, fuelType):
        self.__fuelType = fuelType

    def setMaxPassanger(self, maxPassanger):
        self.__maxPassanger = maxPassanger

    # getter
    def getName(self):
        return self.__name
        
    def getFuelType(self):
        return self.__fuelType

    def getMaxPassanger(self):
        return self.__maxPassanger

    # method
    def move(self, vehicleType):
        print(vehicleType, "is currently moving ...")

    def printVehicle(self):
        print("Fuel Type              : ", self.getFuelType())
        print("Max Passanger          : ", self.getMaxPassanger())
    