# include Person, Job, Driver
from Person import Person
from Job import Job
from Driver import Driver

# function main
def main():
    # initiate person class
    dataPerson = [Person() for i in range(5)]

    # input with setter
    dataPerson[0].setDataPerson("123321", "Burjo Casapa", "Male")
    dataPerson[1].setDataPerson("123322", "Jack Sparrow", "Male")
    dataPerson[2].setDataPerson("123323", "Tony Stark", "Male")
    dataPerson[3].setDataPerson("123324", "Cassandra Lee", "Female")
    dataPerson[4].setDataPerson("123325", "Angelina Jolie", "Female")

    # print Person Data
    print("=========================================")
    print("              Person Data")
    print("=========================================")

    for i in range(5):
        dataPerson[i].printPerson()
        print("---------------------------------------")

    # intiate job class
    dataJob = [Job() for i in range(5)]

    # input with setter
    dataJob[0].setDataJob("343", "Google", "Director")
    dataJob[1].setDataJob("345", "Facebook", "CEO")
    dataJob[2].setDataJob("346", "Oscorp", "Scientist")
    dataJob[3].setDataJob("323", "GoJek", "Car Driver")
    dataJob[4].setDataJob("373", "Stark Industries", "Janitor")

    # print job data
    print("=========================================")
    print("               Job Data")
    print("=========================================")

    for i in range(5):
        dataJob[i].printJob()
        print("---------------------------------------")

    # initiate driver class
    dataDriver = [Driver() for i in range(5)]
    
    # input with setter
    dataDriver[0].setDataPerson("2007392", "Aldi Taher", "Male")
    dataDriver[0].setDataJob("212", "Gopek", "Bike Driver")
    dataDriver[0].setDataDriver("001", 2023, "C")

    dataDriver[1].setDataPerson("2009232", "Vlakimir Putin", "Male")
    dataDriver[1].setDataJob("223", "Grab", "Car Driver")
    dataDriver[1].setDataDriver("002", 2027, "A")

    dataDriver[2].setDataPerson("2034492", "Tom Holang", "Male")
    dataDriver[2].setDataJob("245", "Si Kilat", "Expedition Driver")
    dataDriver[2].setDataDriver("003", 2024, "C")

    dataDriver[3].setDataPerson("2022378", "Iwan Herlambang", "Male")
    dataDriver[3].setDataJob("267", "Shoppe", "Bike Driver")
    dataDriver[3].setDataDriver("009", 2026, "C")

    dataDriver[4].setDataPerson("2007822", "Astra Chambere", "Male")
    dataDriver[4].setDataJob("231", "BukaLacak", "Car Driver")
    dataDriver[4].setDataDriver("006", 2028, "A")

    # print driver data
    print("=========================================")
    print("               Driver Data")
    print("=========================================")

    for i in range(5):
        dataDriver[i].printDriver()

if __name__ == "__main__":
    main()