import datetime
from enum import Enum
import projectconstants
import pandas as pd


price_per_day = {
        "Monday":projectconstants.MONDAY, 
        "Tuesday":projectconstants.TUESDAY, 
        "Wednesday":projectconstants.WEDNESDAY, 
        "Thursday":projectconstants.THURSDAY, 
        "Friday":projectconstants.FRIDAY, 
        "Saturday":projectconstants.SATURDAY, 
        "Sunday":projectconstants.SUNDAY
        }
#ITS A BETTER IDEA TO READ FROM AN EXCEL FILE, WE READ IN THE INIT OF THE CLASS ONCE THE OBJECT IS CREATED (PARKING)
date = datetime.datetime.today()
def current_day(date): #determine the price per hour for the parking based on the day of the week
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dayNumber=date.weekday()
    return days[dayNumber]

today=date.weekday()
#today = current_day(date)
#print(type(today))
#price_today = projectconstants.today

def price_today(price_per_day, today):
    return price_per_day[today]

#print("Today,"+today+",the parking price per hour is:",price_today(price_per_day,today))

#think about how to read the specific parking from a city once the object is created
dataframe1 = pd.read_excel('ParkingPrices/Eindhoven/QPark.xlsx','Mathildelaan2A',engine='openpyxl')
print(dataframe1)
print("The price per hour for today is "+str(dataframe1.Price_per_hour[today])+"€")  #this is price per hour today
print("The maximum price for today is "+str(dataframe1.Max_price_per_day[today])+"€") #this is maximum price per day