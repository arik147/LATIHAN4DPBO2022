# include files
from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane

# main
def main():
    # initiate classes data
    dataVehicle = [Vehicle() for i in range(5)]
    dataShip = [Ship() for i in range(5)]
    dataAirplane = [Airplane() for i in range(5)]

    # input ship data
    dataShip[0].setDataShip(46, "Blue Marine 7 Tanker Ship", "German")
    dataShip[0].setDataVehicle("Diesel", 200)

    dataShip[1].setDataShip(6, "OOCL Hong Kong Container Ship", "South Korea")
    dataShip[1].setDataVehicle("Low Sulphur", 100)

    dataShip[2].setDataShip(10, "COSCO Shipping Container Ship", "China")
    dataShip[2].setDataVehicle("Oil", 140)

    dataShip[3].setDataShip(5, "MOL Triumph Container Ship", "South Korea")
    dataShip[3].setDataVehicle("Low Sulphur", 300)

    dataShip[4].setDataShip(23, "MS Volendam Cruise Ship", "Italy")
    dataShip[4].setDataVehicle("Diesel", 1432)

    # print ship data
    print("==================================================")
    print("                     Ship Data")
    print("==================================================")

    for i in range(5):
        dataShip[i].printShip()

    # input airplane data
    dataAirplane[0].setDataAirplane(11, "Boeing 747", 68)
    dataAirplane[0].setDataVehicle("Kerosene", 467)

    dataAirplane[1].setDataAirplane(35, "Antonov AN-255", 88)
    dataAirplane[1].setDataVehicle("Avgas", 868)

    dataAirplane[2].setDataAirplane(49, "A-10 Thunderbolt II", 17.42)
    dataAirplane[2].setDataVehicle("Hydrogen", 1)

    dataAirplane[3].setDataAirplane(92, "Junkers Ju 87", 30)
    dataAirplane[3].setDataVehicle("Kerosene", 2)

    dataAirplane[4].setDataAirplane(23, "Northrop Grumman B-2 Spirit", 52)
    dataAirplane[4].setDataVehicle("Kerosene", 2)

    # print airplane data
    print("==================================================")
    print("                  Airplane Data")
    print("==================================================")

    for i in range(5):
        dataAirplane[i].printAirplane()

    # input vehicle data
    dataVehicle[0].setDataVehicle("Kerosene" , 467)
    dataVehicle[0].setName("Boeing 747")

    dataVehicle[1].setDataVehicle("Avgas" , 868)
    dataVehicle[1].setName("Antonov AN-255")

    dataVehicle[2].setDataVehicle("Hydrogen" , 1)
    dataVehicle[2].setName("A-10 Thunderbolt II")

    dataVehicle[3].setDataVehicle("Kerosene" , 2)
    dataVehicle[3].setName("Junkers Ju 87")

    dataVehicle[4].setDataVehicle("Kerosene" , 2)
    dataVehicle[4].setName("Northrop Grumman B-2 Spirit")
    
    # print vehicle data
    print("==================================================")
    print("                 Vehicle Data")
    print("==================================================")

    for i in range(5):
        print("Name                   : ", dataVehicle[i].getName())
        dataVehicle[i].printVehicle()
        print("------------------------------------------------------")

if __name__ == "__main__":
    main()