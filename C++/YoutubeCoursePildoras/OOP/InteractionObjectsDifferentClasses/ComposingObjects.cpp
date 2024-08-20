#include <iostream>
using namespace std;

/*Composition: Has-a relationship. A class can have objects of another class as its member variables, which allows the two classes to interact closely. 
The "Car" class contains an "Engine" object as a member, which represents a "has-a" relationship. The "Car" class interacts with the "Engine" object
b calling its "start" method*/

class Engine {
public:
    void start() const {
        cout << "Engine started" << endl;
    }
};

class Car {
private:
    Engine engine;  // Car has an Engine

public:
    void startCar() const {
        engine.start();  // Interacts with the Engine object
        cout << "Car is moving" << endl;
    }
};

int main() {
    Car myCar;
    myCar.startCar();  // Car object interacts with Engine object

    return 0;
}
