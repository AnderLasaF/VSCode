class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car "has-a" Engine

    def start(self):
        print("Car starting...")
        self.engine.start()

    def stop(self):
        print("Car stopping...")
        self.engine.stop()

# Create a Car object
my_car = Car()

# Start and stop the car
my_car.start()
my_car.stop()