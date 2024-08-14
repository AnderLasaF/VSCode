#Hey candidate! Welcome to your interview. Boilerplate is provided. Feel free to change the code as you see fit. To run the code at any time, please hit the run button located in the top left corner.
#Goals: Design a parking lot using object-oriented principles. Here are a few methods that you should be able to run:

#Tell us how many spots are remaining (check)
#Tell us how many total spots are in the parking lot (check)
#Tell us when the parking lot is full (check)
#Tell us when the parking lot is empty (check)
#Tell us when certain spots are full e.g. when all motorcycle spots are taken (check)
#Tell us how many spots vans are taking up

#Assumptions:

#The parking lot can hold motorcycles, cars and vans
#The parking lot has motorcycle spots, car spots and large spots
#A motorcycle can park in any spot
#A car can park in a single compact spot, or a regular spot
#A van can park, but it will take up 3 regular spots
#These are just a few assumptions. Feel free to ask your interviewer about more assumptions as needed

import datetime

class ParkingLot:

    def __init__(self,parking_lines:int,parking_spots_per_line:int,motorcycle_spots:int,car_spots:int, van_spots:int,motorbyke_parking_prices:float,car_parking_prices:float,van_parking_prices:float):
        
        
        #The number of motorcycles, cars and vans could vary depending on the parking lot type. But every parking lot object 
        #will have a specific number of total_spots


        #Validation of the received arguments
        assert parking_lines>0, f"The number of parking lines should be greater than 0"
        assert parking_spots_per_line>0, f"The number of parking spots per line should be greater than 0"
        assert motorcycle_spots >=0, f"Total motorcycle spots {motorcycle_spots} are not greater than 0"
        assert car_spots >=0, f"Total car spots {car_spots} are not greater than 0"
        assert van_spots >=0, f"Total van spots {van_spots} are not greater than 0"
        assert len(motorbyke_parking_prices) ==7, f"Parking prices for motorbykes should be defined for the whole week"
        assert len(car_parking_prices) ==7, f"Parking prices for cars should be defined for the whole week"
        assert len(van_parking_prices) ==7, f"Parking prices for vans should be defined for the whole week"
        assert all(val > 0 for val in motorbyke_parking_prices), f"Prices for motorbykes can't be negative"
        assert all(val > 0 for val in car_parking_prices), f"Prices for cars can't be negative"
        assert all(val > 0 for val in van_parking_prices), f"Prices for vans can't be negative"


        #Assign to self object
        self.__parking_lines = parking_lines
        self.__parking_spots_per_line = parking_spots_per_line
        self.__motorcycle_spots = motorcycle_spots #only for motorcycles
        self.__car_spots = car_spots  #both motorcycles and cars can park here
        self.__van_spots = van_spots  #3 times the size of a car spot
        self.__car_spots_occupied = 0  #interesting to make them able to change ONLY in the class itself. That is why is defined in the class itself
        self.__motorcycle_spots_occupied = 0
        self.__van_spots_occupied = 0
        self.__parkingspots = ["Motorcycle","Car","Van"]

        self.__motorbyke_parking_prices = motorbyke_parking_prices  #this is not working, it should be part of an instance from the class, and not the same for every instance of the class
        self.__car_parking_prices = car_parking_prices
        self.__van_parking_prices = van_parking_prices
        
    #first we initiate the parking lot as empty, so all the spots are green
    def determine_layout(self): #* stands for empty spot
        parking_matrix = [["*" for j in range(self.__parking_spots_per_line)] for i in range(self.__parking_lines)]  #list comprehension
        return parking_matrix
    
    #def modify_layout(self,parked_line,parked_spot):
    #    parking_matrix[sensor_data[0]][sensor_data[1]]

    #try encapsulation first with motorcycles, if it works, expand it to the rest of vehicles

    def get_motorbyke_parking_prices(self):

        return self.__motorbyke_parking_prices
    
    def get_car_parking_prices(self):

        return self.__car_parking_prices
    
    def get_van_parking_prices(self):
        
        return self.__van_parking_prices
    
    def get_ParkMotorcycle(self):
        return self.__motorcycle_spots_occupied
    
    def set_ParkMotorcycle(self,parking_spot):  #before trying to park we should check if there are free spots
        assert parking_spot in self.__parkingspots, f"The specificed parking spot does not exist"
        if parking_spot=="Motorcycle":
            assert self.__motorcycle_spots_occupied+1 <= self.__motorcycle_spots, f"Motorcycle spots are full"
            self.__motorcycle_spots_occupied+=1
            return 
        elif parking_spot=="Car":
            assert self.__car_spots_occupied+1 <= self.__car_spots, f"Car spots are full"
            #we need to fill a car spot in the matrix and 
            self.__car_spots_occupied+=1

        else: #van spot
            assert self.__van_spots_occupied+1 <= self.__van_spots, f"Van spots are full"
            self.__van_spots_occupied+=1
            #two car spots become available
            self.__car_spots +=2
    
    def get_ParkCar(self):
        return self.__car_spots_occupied
    
    def set_ParkCar(self,parking_spot):
        assert parking_spot in self.__parkingspots, f"The specificed parking spot does not exist"
        assert parking_spot!="Motorcycle", f"Not possible to park a car in a motorcycle spot"
        if parking_spot=="Car":
            assert self.__car_spots_occupied+1 <= self.__car_spots, f"Car spots are full"
            self.__car_spots_occupied+=1
        else: #parking_spot =="Van"
            assert self.__van_spots_occupied+1 <= self.__van_spots, f"Van spots are full"
            self.__van_spots_occupied+=1
            #two car spots become available
            self.__car_spots +=2       

    def get_ParkVan(self):
        return self.__van_spots_occupied
    
    def set_ParkVan(self,parking_spot):
        assert parking_spot =="Van", f"Vans can only be parked in van spots"
        assert self.__van_spots_occupied+1 <= self.__van_spots, f"Vans pots are full"
        self.__van_spots_occupied+=1

    def totalspots(self):
        return "Total spots in the parking are: ",self.__motorcycle_spots+self.__car_spots+self.__van_spots,"Motorcycle spots: ",self.__motorcycle_spots,"Car spots: ",self.__car_spots,"Van spots: ",self.__van_spots

    def isFull(self):
        return self.__motorcycle_spots == self.__motorcycle_spots_occupied and self.__car_spots == self.__car_spots_occupied and self.__van_spots == self.__van_spots_occupied

    def isEmpty(self):
        return self.__motorcycle_spots_occupied ==0 and self.__car_spots_occupied ==0 and self.__van_spots_occupied==0
    
    def remainingspots(self):
        return "Motorcycle spots left: ",self.__motorcycle_spots-self.__motorcycle_spots_occupied,"Car spots left: ",self.__car_spots-self.__car_spots_occupied,"Van spots left: ",self.__van_spots-self.__van_spots_occupied
    
class Vehicle(ParkingLot):   #A vehicle will not be allowed to leave the parking without paying. This will be done checking the license plate

    def __init__ (self,plate:str,type:str):   #data plate and type we get by the camera at the entrance of the parking

        #super().__init__(motorbyke_parking_prices,car_parking_prices,van_parking_prices)
        super().__init__(None,None,None,None,None,motorbyke_parking_prices,car_parking_prices,van_parking_prices)
        self.__data = {str(plate): type, "enter_time": datetime.datetime.now(), "leave_time":None,"discount":None,"cost":None}

    def car_parking_prices(self):

        return self.get_car_parking_prices()

    def park_cost(self,plate,leave_time,discount): #calculate parking costs

        time_difference = leave_time-self.__data["enter_time"]
        parked_minutes= time_difference.total_seconds()/60 

        if discount==0:
            if self.__data[plate]=="Motorbyke":
                return parked_minutes*(self.car_parking_prices()[0]/60)            
            elif self.__data[plate]=="Car":
                return parked_minutes*(super().car_parking_prices[0]/60)
            else:
                return parked_minutes*(super().van_parking_prices[0]/60)
        else:
            if self.__data[plate]=="Motorbyke":
                return parked_minutes*(super().motorbyke_parking_prices/60)-discount
            elif self.__data[plate]=="Car":
                return parked_minutes*(super().car_parking_prices/60)-discount
            else:
                return parked_minutes*(super().van_parking_prices[0]/60)-discount


    
if __name__ == "__main__":

    parking_lines = 6
    parking_spots_per_line = 5
    
    #think about what should be the best way to determine the number of parking spots for each vehicle
    motorcycle_spots = 10
    car_spots = 10
    van_spots = 10

    motorbyke_parking_prices = [1.20,1.20,1.20,1.20,1.80,1.80,1.80]  #this could be derived from a file
    car_parking_prices = [1.60,1.60,1.60,1.60,2.20,2.20,2.20]  #this could be derived from a file
    van_parking_prices = [2.40,2.40,2.40,2.40,3.00,3.00,3.00]  #this could be derived from a file
    ParkingLot1 = ParkingLot(parking_lines,parking_spots_per_line,motorcycle_spots,car_spots,van_spots,motorbyke_parking_prices,car_parking_prices,van_parking_prices)
    print("Parking is empty: ",ParkingLot1.isEmpty())
    print("Parking is full: ",ParkingLot1.isFull())
    print("Parked motorcycles: ",ParkingLot1.get_ParkMotorcycle())
    ParkingLot1.set_ParkMotorcycle("Motorcycle")
    ParkingLot1.__motorcycle_spots_occupied=0  #this does not work due to name mangling
    print("Parked motorcycles: ",ParkingLot1.get_ParkMotorcycle())
    print(ParkingLot1.totalspots())
    print(ParkingLot1.remainingspots())
    #ParkingLot1.set_ParkCar("Motorcycle")
    #print(ParkingLot1.pricelistcars.car_prices("Monday"))
    print(ParkingLot1.determine_layout())

    #lets create our first vehicle object
    car1 = Vehicle("R824ST","Car")
    print(car1._Vehicle__data)
    print(car1.park_cost("R824ST",datetime.datetime.now(),0))
    print(car1.get_car_parking_prices())

#create a discount method, in case there is a discount for whatever reason (for example for being disabled, retired, taking public transport, etc)
#it would be intersting to know which car, motorbyke or van has parked in which parking and then in which spot and for how long. This could be
#used to know how much to charge and the data should be saved in the cloud to have a register of cars, etc, which could be used for big data later or know
#which are the best fares to get the maximum profit, etc.
    
