class Dog:
    species = 'mammal'

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @property
    def name(self) -> str:
        """Getter for name."""
        return self.__name
    
    @name.setter
    def name(self, value: str):
        """Setter for name. Check if the input value is a non-empty string."""
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value

    @property
    def age(self) -> int:
        """Getter for age."""
        return self.__age
    
    @age.setter
    def age(self, value: int):
        """Setter for age. Check if the input value is positive."""
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("Age must be greater than or equal to 0")
        self.__age = value

if __name__ == '__main__':
    try:
        my_dog = Dog("", -3)
    except ValueError as e:
        print(f"Error: {e}")

