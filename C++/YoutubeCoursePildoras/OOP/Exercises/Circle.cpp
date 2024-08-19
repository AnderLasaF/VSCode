/*Write a C++ program to implement a class called Circle that has private member variables for radius. 
Include member functions to calculate the circle's area and circumference*/
#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
using namespace std;

//class that creates circles with a specific radius and allows the calculation of circumference and area given a radius
class Circle{ 
    
    private:
        double radius;  //private to store the radius. It's initialized in the constructor but modified and accessed through setter and getter
    
    public:
        //Constructor to initialize the Circle object with a radius
        Circle(double r){
            if (r<=0){
                throw invalid_argument("Radius has to be greater than 0");}  //throw exception if the radius is not >0
            radius = r;
        }  

    void setRadius(double r){  //In case we want to change the radius of the circle anytime
        if (r>0){
            radius = r;
        }
        else{
            throw invalid_argument("Radius has to be greater than 0");}  //throw exception if the radius is not >0; 
        }
    }
    double getRadius(){  //Returns the value of the radius for the specific instance of the class
        return radius;
    }
    
    double calculateCircumference(double r){  //Method that calculates the circumference of the specific object
        return 2*M_PI*r;
    }
    
    double calculateArea(double r){  //Method that calculates the area of the specific object
        return M_PI*pow(r,2);
    }
};

int main(void){
    //initial radius of the circle is given by the user
    double radius;
    cout << "Input the radius of the circle: " << endl;
    cin >> radius;

    //Call to the constructor with the radius given by the user
    Circle myCircle(radius); //object myCircle
    cout << "The radius of the circle is " << myCircle.getRadius() << endl;
    cout << "The circumference of the circle is " << myCircle.calculateCircumference(radius) << endl;
    cout << "The area of the circle is: " << myCircle.calculateArea(radius) << endl;

    //set a new radius to the existing object
    myCircle.setRadius(6);
    cout << "The new radius of the circle is: " << myCircle.getRadius() << endl;
    cout << "The new circumference of the circle is " << myCircle.calculateCircumference(radius) << endl;
    cout << "The new area of the circle is " << myCircle.calculateArea(radius) << endl;

    //Set deliberately an invalid radius
    myCircle.setRadius(-5);

    return 0; //end of execution
}
