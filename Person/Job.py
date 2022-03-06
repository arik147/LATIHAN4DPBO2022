# Class Job
class Job:
    # constructor
    def __init__(self):
        self.__nip = "<No Input>"
        self.__companyName = "<No Input>"
        self.__position = "<No Input>"

    # setter
    def setDataJob(self, nip, companyName, position):
        self.__nip = nip
        self.__companyName = companyName
        self.__position = position

    def setNip(self, nip):
        self.__nip = nip

    def setCompanyName(self, companyName):
        self.__companyName = companyName

    def setPosition(self, position):
        self.__position = position

    # getter
    def getNip(self):
        return self.__nip

    def getCompanyName(self):
        return self.__companyName

    def getPosition(self):
        return self.__position

    # method
    def printJob(self):
        print("NIP              : ", self.getNip())
        print("Company Name     : ", self.getCompanyName())
        print("Position         : ", self.getPosition())