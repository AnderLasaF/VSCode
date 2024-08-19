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

class ParkingLot:

    def __init__(self,motorcycle_spots:int,car_spots:int, van_spots:int):
        
        
        #The number of motorcycles, cars and vans could vary depending on the parking lot type. But every parking lot object 
        #will have a specific number of total_spots


        #Validation of the received arguments
        assert motorcycle_spots >=0, f"Total motorcycle spots {motorcycle_spots} are not greater than 0"
        assert car_spots >=0, f"Total car spots {car_spots} are not greater than 0"
        assert van_spots >=0, f"Total van spots {van_spots} are not greater than 0"

        #Assign to self object
        self.__motorcycle_spots = motorcycle_spots #only for motorcycles
        self.__car_spots = car_spots  #both motorcycles and cars can park here
        self.__van_spots = van_spots  #3 times the size of a car spot
        self.__large_to_regular_spot_ratio = 3
        self.__car_spots_occupied = 0  #interesting to make them able to change ONLY in the class itself. That is why is defined in the class itself
        self.__motorcycle_spots_occupied = 0
        self.__van_spots_occupied = 0


    @property
    #Property decorador = read-only attribute
    #We should not be able to modify this attribute outside the class
    def NumberOfMotorcycleSpots(self):
        return self.__motorcycle_spots
    
    def ParkingIsFull(self):
        return (self.__motorcycle_spots ==0 and self.__car_spots==0 and self.__van_spots ==0)
    
    def ParkingIsEmpty(self):
        return (self.__car_spots_occupied==0 and self.__motorcycle_spots_occupied==0 and self.__van_spots_occupied==0)

    def TotalNumberOfSpots(self):
        assert self.__large_to_regular_spot_ratio>1, f"The ratio between a large and a regular spot, {self.__large_to_regular_spot_ratio}, is not greater than 1"
        return "The total number of spots are ",self.__motorcycle_spots+self.__car_spots+self.__van_spots*self.__large_to_regular_spot_ratio
    
    def SpotsRemaining(self):
        return "There are ",self.__motorcycle_spots,"motorcycle spots remaining.\n There are ",self.__car_spots,"car spots remaining.\n There are ",self.__van_spots,"van spots remaining."

    def CarSpotsAreFull(self):
        return self.__car_spots==self.__car_spots_occupied
    
    def MotorcycleSpotsAreFull(self):
        return self.__motorcycle_spots==self.__motorcycle_spots_occupied
       
    def VanSpotsAreFull(self):
        return self.__van_spots==self.__van_spots_occupied
    
    def ParkMotorcycle(self, parking_spot):

        assert parking_spot in ["MotorcycleSpot","CarSpot","VanSpot"], f"Please, introduce a possible parking spot to park a motorcycle"
        
        if parking_spot=="MotorcycleSpot":
            assert self.__motorcycle_spots-1 >=0, f"There are no free motorcycle spots to park a new motorcycle"
            self.__motorcycle_spots-=1 
            self.__motorcycle_spots_occupied+=1 
            return "Motorcycle spots free: ",self.__motorcycle_spots-self.__motorcycle_spots_occupied

        elif parking_spot=="CarSpot":
            assert self.__car_spots-1 >=0, f"There are no free car spots to park a new motorcycle"
            self.__car_spots-=1
            self.__car_spots_occupied+=1
            return "Car spots free: ",self.__car_spots-self.__car_spots_occupied

        else: #parking spot =="VanSpot"
            #if we park a motorcycle in a van spot we lose a van spot but we "gain" three car spots, later we need to subtract the parked motorcycle
            assert self.__van_spots-1 >=0, f"There are no free van spots to park a new motorcycle"
            self.__van_spots-=1
            self.__car_spots+=self.__large_to_regular_spot_ratio
            self.__car_spots_occupied+=1
        
        return "Motorcycle successfully parked"

    
    def ParkCar(self, parking_spot):

        assert parking_spot in ["CarSpot","VanSpot"], f"Please, introduce a possible parking spot to park a car"

        if parking_spot=="CarSpot":
            assert self.__car_spots-1 >=0, f"There are no free car spots to park a new car"
            self.__car_spots-=1
            self.__car_spots_occupied+=1

        else: #parking spot =="VanSpot":
            assert self.__van_spots-1 >=0, f"There are no free van spots to park a new car"
            self.__van_spots-=1
            self.__car_spots+=self.__large_to_regular_spot_ratio
            self.__car_spots_occupied+=1
        
        return "Car succesfully parked"
        
    
    def ParkVan(self, parking_spot):

        assert parking_spot == "VanSpot", f"Please, introduce a possible parking spot to park a van"

        assert self.__van_spots-1 >=0, f"There are no free van spots to park a new van"
        self.__van_spots-=1
        self.__van_spots_occupied+=1

        return "Van succesfully parked"

#BONUS
        
    def LeaveVan(self):

        assert self.__van_spots_occupied>0, f"There are no vans left in the parking"
        self.__van_spots_occupied-=1
    
#BONUS    
    def LeaveCar(self): #I need to manage in how to know if a car is parked in a van spot or a car spot

        pass

#BONUS
    def LeaveMotorcycle(self):  #I need to manage in how to know if a motorcycle is parked in a van spot, car spot or a motorcycle spot. A tuple could word

        pass


if __name__ == "__main__":
    motorcycle_spots = 10 #total number of motorbyke spots
    regular_spots = 10 #total number of regular spots
    large_spots = 10 #total number of large spots (3 regular spots each)


    Parking1 = ParkingLot(motorcycle_spots,regular_spots,large_spots)
    print(Parking1.TotalNumberOfSpots())
    print(Parking1.ParkingIsEmpty())
    print(Parking1.ParkCar("CarSpot"))
    print(Parking1.ParkingIsEmpty())
    print(Parking1.ParkMotorcycle("MotorcycleSpot"))
    print(Parking1.SpotsRemaining())
    #print("Motorcycle spots occupied: ",Parking1.__motorcycle_spots_occupied)  #we get an error trying to modify this attribute
    Parking1.__motorcycle_spots_occupied= 0 #I should get an error here trying to modify it. Use getters and setters or decorators??
    Parking1.__motorcycle_spots= 0  #I should get an error here trying to modify it. Use getters and setters or decorators??
    print("Motorcycle spots occupied: ",Parking1.__motorcycle_spots_occupied)
    print("Total motorcycle spots: ",Parking1.__motorcycle_spots)
    #print(Parking1.LeaveVan())
    Parking1.motorcycle_spots=9
    print(Parking1.motorcycle_spots)