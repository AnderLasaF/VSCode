/*Write a C++ program to create a class called Rectangle that has private member variables for length and width. 
Implement member functions to calculate the rectangle's area and perimeter*/

#include <iostream>
using namespace std;

class Rectangle{

    private:
        double length;
        double width;

    public:
        Rectangle(double l, double w){
            //Constructor
            if((l <=0) or (w <=0)){
                throw invalid_argument("Length and width have to be greater than 0");}  //throw exception if the length or width are not >0
            length = l;
            width = w;
        }
    
    void setLength(double l){  //change the length anytime is desired with the setter
        if(l<=0){
            throw invalid_argument("Length has to be greater than 0");}  //throw exception if the length is not >0
        length = l;
    }

    double getLength(){ //getter for length
        return length;
    }

    void setWidth(double w){
        if(w<=0){
            throw invalid_argument("Width has to be greater than 0");}  //throw exception if the width is not >0
        
        width = w;
    }

    double getWidth(){ //getter for width
        return width;
    }

    double calculateArea(double w,double l){
        return w*l;
    }

    double calculatePerimeter(double w,double l){
        return 2*w+2*l;
    }
};

int main(){

    //create object and initialize it calling the constructor
    double width;
    double length;
    cout << "Introduce the width: " << endl;
    cin >> width;

    cout << "Introduce the length: " << endl;
    cin >> length;

    Rectangle myRectangle(length,width);
    cout << "The width and lenght of the rectangle are: " << myRectangle.getWidth() << " and " << myRectangle.getLength() << endl;
    
    //Calculate the area
    cout << "The area of the rectangle is " << myRectangle.calculateArea(width,length) << endl;

    //Calculate the perimeter
    cout << "The perimeter of the rectangle is " << myRectangle.calculatePerimeter(width,length);

    return 0;

}

    
    