# include Person and Job
from Person import Person
from Job import Job

# Person and Job are parent of Driver class
class Driver(Person, Job):
    # constructor
    def __init__(self):
        super().__init__()
        self.__licenseId = "<No Input>"
        self.__activeUntil = 0
        self.__vehicleType = "<No Input>"

    # setter
    def setDataDriver(self, licenseId, activeUntil, vehicleType):
        self.__licenseId = licenseId
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType

    def setLicenseID(self, licenseId):
        self.__licenseId = licenseId

    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType
        
    # getter 
    def getLicenseID(self):
        return self.__licenseId

    def getActiveUntil(self):
        return self.__activeUntil
        
    def getVehicleType(self):
        return self.__vehicleType

    # method
    def printDriver(self):
        self.printPerson()
        self.printJob()
        print("License ID       : ", self.getLicenseID())
        print("Active Until     : ", self.getActiveUntil())
        print("Vehicle Type     : ", self.getVehicleType())
        self.sleep("Not Sleep", self.getName())
        print("---------------------------------------")