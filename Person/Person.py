# Class Person
class Person:
    # constructor
    def __init__(self):
        self.__nik = "<No Input>"
        self.__name = "<No Input>"
        self.__gender = "<No Input>"

    # setter
    def setDataPerson(self, nik, name, gender):
        self.__nik = nik
        self.__name = name
        self.__gender = gender

    def setNik(self, nik):
        self.__nik = nik

    def setName(self, name):
        self.__name = name

    def setGender(self, gender):
        self.__gender = gender

    # getter
    def getNik(self):
        return self.__nik

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    # method
    def sleep(self, sleepMode, driver):
        if sleepMode == "Sleep":
            print(driver, "is Sleeping.")
        else:
            print(driver, "isn't Sleeping.")

    def printPerson(self):
        print("NIK              : ", self.getNik())
        print("Name             : ", self.getName())
        print("Gender           : ", self.getGender())