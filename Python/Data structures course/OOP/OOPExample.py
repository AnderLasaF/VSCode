class Parent:
    def __init__(self, attribute1, attribute2):
        self.__attribute1 = attribute1
        self.__attribute2 = attribute2

    def get_attribute1(self):
        return self.__attribute1

    def get_attribute2(self):
        return self.__attribute2

class Child:
    def __init__(self, parent_instance, attribute3):
        self.parent_instance = parent_instance  # Store the parent instance
        self.__attribute3 = attribute3

    def get_attribute3(self):
        return self.__attribute3

    def combined_attributes(self):
        return self.parent_instance.get_attribute1(), self.parent_instance.get_attribute2(), self.__attribute3

# Create an instance of the Parent class
parent_obj = Parent("Value 1", "Value 2")

# Create an instance of the Child class and pass the parent instance
child_obj = Child(parent_obj, "Value 3")

# Example usage
print(child_obj.combined_attributes())  # Output: ('Value 1', 'Value 2', 'Value 3')

