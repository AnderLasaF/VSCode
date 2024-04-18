class EncapsulatedClass:
    def __init__(self, name, age):
        self.__name = name  # Encapsulated attribute with double leading underscores
        self.__age = age    # Encapsulated attribute with double leading underscores

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, new_name):
        self.__name = new_name

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Age cannot be negative.")

# Test cases
if __name__ == "__main__":
    # Create an instance of the EncapsulatedClass
    person = EncapsulatedClass(name="John", age=25)

    # Test getters
    assert person.get_name() == "John"
    assert person.get_age() == 25

    # Test setters
    person.set_name("Jane")
    person.set_age(30)

    # Verify that the attributes have been updated
    assert person.get_name() == "Jane"
    assert person.get_age() == 30

    # Try setting a negative age (should print a message and not update the age)
    person.set_age(-5)

    # Verify that the age remains unchanged
    assert person.get_age() == 30
    person.__age = 0  #Trying to modify the age attribute. Not possible due to name mangling
    person.age=0
    #person._EncapsulatedClass__age = 0 #In this way is possible to modify the attribute, making use of the mangled name
    print("The age of",person.get_name(),"is",person.get_age())

    print("All test cases passed!")