# circle.py

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  #we are calling the setter method, that is why the getter returns a float value, because first it entered the setter method

    @property
    def radius(self):
        return self._radius  

    @radius.setter
    def radius(self, value):
        if value<=0:
            raise ValueError('Radius should be an integer greater than 0')
        try:
            self._radius = float(value)  #defined as private. Not to be used outside the class
        except Exception as error:  
            print("An error occurred:", type(error).__name__) #An error occurred: NameError

    @property
    def diameter(self):
        return self.radius * 2    #we are calling the getter method

    @diameter.setter
    def diameter(self, value):
        if value>0:
            self.radius = value / 2 #we are calling the setter method