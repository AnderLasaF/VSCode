#We can see properties as a hybrid between attributes and methods
#More accurately, methods that behave like attributes

#If we convert two attributes into properties (x,y) we can still continue to access them as attributes
#Also a method that will allow internal modification of x and y
#Actions can be taken on the attributes before the user access to them

#Main advantage of properties is that they allow exposure of attributes in Public API
#If the implementation needs to be changed, then the attribute can be converted into a property

#property() is a class designed to work a function

#obj.attr : fget() is called
#obj.attr = value: fset(value) is called
#del obj.attr: fdel() is called

# circle.py

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):  #method
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(  #we have defined radius as a property
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )

