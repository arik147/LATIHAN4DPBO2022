from Vehicle import Vehicle

class Airplane(Vehicle):
    # constructor
    def __init__(self):
        super().__init__()
        self.__type = "<No Input>"
        self.__age = 0
        self.__wingsLength = 0

    # setter
    def setDataAirplane(self, age, airplaneType, wingsLength):
        self.__age = age
        self.__type = airplaneType
        self.__wingsLength = wingsLength

    def setAge(self, age):
        self.__age = age

    def setType(self, type):
        self.__type = type

    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength

    # getter
    def getAge(self):
        return self.__age

    def getType(self):
        return self.__type

    def getWingsLength(self):
        return self.__wingsLength

    # method
    def printAirplane(self):
        print("Type                   : ", self.getType())
        print("Age                    : ", self.getAge(), "Years Old")
        print("Wings Length           : ", self.getWingsLength(), "Meters")
        self.printVehicle()
        self.move(self.getType())
        print("------------------------------------------------------")