#include <iostream>
using namespace std;

/*Operator overloading allows custom definitions of operators for objects of different classes. 
The "Speed" class overloads the "*" operator to interact with a "Distance" object, allowing you to 
compute time based on speed and distance.*/

class Distance {
public:
    int meters;

    Distance(int m) : meters(m) {}
};

class Speed {
public:
    int kmph;

    Speed(int k) : kmph(k) {}

    // Overload * operator for Distance * Speed
    int operator*(const Distance& dist) const {
        return kmph * dist.meters;  // Interaction between Speed and Distance
    }
};

int main() {
    Distance d(10);  // Distance in meters
    Speed s(50);     // Speed in km per hour

    int time = s * d;  // Interacting using overloaded operator
    cout << "Time to travel: " << time << " hours" << endl;

    return 0;
}
