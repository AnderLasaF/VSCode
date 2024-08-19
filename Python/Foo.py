class C(object):
    def __init__(self):
        self.a = 123    # OK to access directly
        self._a = 123   # should be considered private
        self.__a = 123  # considered private, name mangled

c = C()
c.a
c._a
#print(c.__a) #this raises an error. However, it's possible to redefine c.__a with the next line
c.__a=1
#print(c.__a)
