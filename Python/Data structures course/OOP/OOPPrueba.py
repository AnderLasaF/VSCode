import datetime

class Parking:

    def __init__(self,location:str,total_spots:int,price_per_hour:float):
        
        self._location = location
        self._total_spots = total_spots
        self._parked_vehicles = 0
        self._price_per_hour = price_per_hour
        self._free_spots = self._total_spots - self._parked_vehicles

    @classmethod  
    #class methods have access to the class itself through the 'cls' parameter
    def validate_parking_arguments(cls,location:str,total_spots:int,price_per_hour:float):
        #Perform validation to object creation
        if not isinstance(location,str):
            raise TypeError("Location must be a string")
        if total_spots<=0:
            raise ValueError("Total spots must be greater than 0")
        if price_per_hour<=0:
            raise ValueError("Price per hour must be greater than 0")
        return cls(location,total_spots,price_per_hour)  #create and return an instance of Parking
    
    @property
    def parked_vehicles(self):
        return self._parked_vehicles
    
    @parked_vehicles.setter
    def parked_vehicles(self):
        if self.free_spots>0:
            self._parked_vehicles+=1
        else:
            raise ValueError("There are no more free spots")

    @property
    def free_spots(self):
        return self._free_spots
    
    def location(self):
        return self._location
    
    @property
    def price_per_hour(self):
        return self._price_per_hour
    
    @price_per_hour.setter
    def price_per_hour(self,new_price_per_hour):
        assert new_price_per_hour>0, f"Price should be greater than 0"
        self._price_per_hour = new_price_per_hour

    @property
    def total_spots(self):
        return self.total_spots

    @total_spots.setter
    def total_spots(self,new_total_spots):
        assert new_total_spots >0, f"Total spots should be greater than 0"
        self._total_spots = new_total_spots
    
    

class Vehicle:
    #when a license plate is detected in the entrance of a specific parking then the vehicle has entered the parking, so a new vehicle object should be created
    def __init__(self,parking_instance,plate:str,parked=False,enter_time=None,leave_time=None,payment_amount=None,payment_executed=None):

        self.parking_instance = parking_instance #store the Parking instance, since we are going to interact with the parking where the vehicle is parked
        self._license_plate = plate
        self._parked = parked
        self._enter_time = enter_time
        self._leave_time = leave_time
        self._payment_amount = payment_amount
        self._payment_executed = payment_executed

    
    def park(self):
        if self.parking_instance.free_spots>0:
            self.parking_instance.parked_vehicles+=1
            self._parked = True
            self._enter_time = datetime.datetime.now()
            print("The vehicle is parked")
        else:
            raise ValueError("Free spots have to be greater than 0")
          

    def isParked(self):
        return self._parked
    
    def parking_time(self):  
        if self.isParked():
            self._leave_time = datetime.datetime.now()
            return (self._leave_time - self._enter_time).total_seconds()/60  #return parking time in minutes
        else:
            raise ValueError("The car is not parked")
    
    def parking_cost(self):
        self._payment_amount = self.parking_time()*self.parking_instance.price_per_hour()
        return self._payment_amount

    def pay_parking(self, payment_approved):  #this function should be called when the payment has been approved from the bank 
        assert payment_approved ==True, f"Please try again, the payment has not been approved"
        self._payment_executed = True

    def payment_executed(self):
        return self._payment_executed

    def leave(self):
        if self.payment_executed() and self.isParked():
            self._parked=False

if __name__=='__main__':
    Parking1=Parking("Eindhoven",100,2.5)
    Vehicle1=Vehicle(Parking1,"R824ST")
    Vehicle1.park()
    Parking1.total_spots
