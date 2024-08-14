#test

import OOPPrueba
import time


def test_create_parking():

    global Parking1
    Parking1 = OOPPrueba.Parking("Eindhoven",500,2)
    print(dir(Parking1))
def test_get_parked_vehicles():

    print("Parked vehicles are: ",Parking1.parked_vehicles)
    Vehicle1 = OOPPrueba.Vehicle(Parking1,"R824ST")
    Vehicle1.set_park()
    print(Vehicle1.get_park())  #check if we have parked the car
    print("Parked vehicles are: ",Parking1.parked_vehicles)
#def test_happy_flow_car():

#    Parking1 = OOPPrueba.Parking("Eindhoven",500,2) 
#    Car1 = OOPPrueba.Vehicle(Parking1,"R824ST")
#    Car1.set_park()  #parking the car
#    print(Car1.get_park())  #check if we have parked the car
#    print(Parking1.get_parked_vehicles)
#    time.sleep(60)   #we wait a minute 
#    print(Car1.get_parking_time())
#    print(Car1.get_parking_cost())
#    print(Car1.set_payment_executed)
