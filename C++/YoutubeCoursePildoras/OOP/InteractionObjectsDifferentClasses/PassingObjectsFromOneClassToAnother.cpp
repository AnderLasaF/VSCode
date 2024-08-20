#include <iostream>
using namespace std;

//The Printer class interacts with a Rectangle object by taking it as a parameter. It calls the "area()" function of the "Rectangle" object to print the area
 
class Rectangle {
private:
    int width, height;

public:
    Rectangle(const int w, int h) : width(w), height(h) {}

    int area() const {
        return width * height;
    }
    
    const int getWidth() const{
        return width;
    }
    
    int getHeight() const{
        return height;
    }
    
    void setWidth(int w){
        width = w;
    }
};

class Printer {
public:
    // Function that takes a Rectangle object
    void printArea(const Rectangle& rect) const {
        cout << "Area of the rectangle: " << rect.area() << endl;
    }
    //Another function that takes a Rectangle object
    void printWidth(const Rectangle& rect) const{
        cout << "Width of the rectangle: " << rect.getWidth() << endl;
    }
    //Another function that takes a Rectangle object
    void printHeight(const Rectangle& rect) const{
        cout << "Height of the rectangle: " << rect.getHeight() << endl;
    }
};

int main() {
    Rectangle rect(10, 20);
    Printer printer;

    printer.printArea(rect);  // Rectangle object passed to Printer object
    printer.printWidth(rect);
    printer.printHeight(rect);
    
    rect.setWidth(20); //Trying to modify the width of the rectangle
    cout << "New width of the rectangle " << rect.getWidth() << endl;
    return 0;
}