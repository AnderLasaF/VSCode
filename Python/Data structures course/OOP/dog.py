class Animal:
    def __init__(self, species:str):
        self.species = species

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    """
    A class representing a dog, which inherits from Animal.
    
    Attributes:
        breed (str): the breed of the dog
        age (int): the age of the dog
        species (str): the species of the dog
    """
    def __init__(self, breed:str, age:int, species:str ="Canine"):
        """
        Initializes a Dog object

        Parameters: 
            breed (str): the breed of the dog
            age (int): the age of the dog
             species (str): the species of the dog    
        """
        super().__init__(species)
        self._breed = breed
        self._age = age

    def make_sound(self):
        print("Woof!")

    def wag_tail(self):
        print("Dog is wagging its tail")

    @property
    def breed(self):
        return self._breed
    
    @property
    def age(self):
        """Getter method for age"""
        return self._age
    
    @age.setter
    def age(self,new_age:int):
        """Setter method for age. It is checked that the attribute new_age is a positive integer and greater than the actual age
        
        Args: 
            new_age: int

        Raises:
            TypeError: If the new age is not an integer
            ValueError: If the new age is not positive or before the previous age

        """
        if not isinstance(new_age,int):
            print("Im here")
            raise TypeError("Age has to be an integer")
        
        if new_age<0 or new_age<self._age:   
            raise ValueError("Age should be positive and higher than the previous one")
       
        self._age = new_age

# Create an instance of Dog
dog = Dog("Golden Retriever",4)
#dog.age = 3
#dog.age = 4
# Access attributes from both the parent class and the child class
print("Species:", dog.species)  # Output: Canine
print("Breed:", dog.breed)      # Output: Golden Retriever
help(Dog)  