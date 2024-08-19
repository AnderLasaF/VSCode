//Classes are a mechanism to build our own types and blueprints to create objects

//As an example we are going to define a cylinder.

//The cylinder is defined by the radius and height

#include <iostream>
using namespace std;
const double PI {3.1415926};

class Cylinder{

public:  
    double volume(){
        return PI * base_radius * base_radius * height;
    }

private:   //NOT accessible from outside the class. If we don't specify "public", they will be private by default
    //everyting after this "private" will be not accessible
    double base_radius{1.0};
    double height{1.0};
};

int main(int argc, char **argv{

    Cylinder cylinder1; //declaring cylinder1 object from Cylinder class
    cout << "Volume c1: " << cylinder1.volume() << endl;

    cyclinder1.base_radius = 3.0 //modyfing the attribute base_radius
    cylinder.height = 2; //modyfing the attribute height
    "volume c1: " << cylinder1.volume() << endl;

    Cylinder cylinder2;
    cout << "Volume c2:  " << cylinder2.volume() << endl;

    return 0;
})

//CONTINUE AT 20:31:00