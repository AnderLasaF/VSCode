#include <iostream>
using namespace std;

class Coordinates {
public:
    int x, y;

    Coordinates(int xCoord, int yCoord) : x(xCoord), y(yCoord) {}

    void display() const {
        cout << "Coordinates: (" << x << ", " << y << ")" << endl;
    }
};

class PointGenerator {
public:
    // Function that returns a Coordinates object
    Coordinates generatePoint(int x, int y) const {
        return Coordinates(x, y);  // Creating and returning a Coordinates object
    }
};

int main() {
    PointGenerator generator;
    Coordinates point = generator.generatePoint(5, 10);  // PointGenerator object creates a Coordinates object

    point.display();

    return 0;
}
