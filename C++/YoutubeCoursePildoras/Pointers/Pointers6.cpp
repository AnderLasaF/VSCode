/*
Return of pointers by functions. Use cases:

1. Access to data estructures or Classes. Returning a pointer allows to other parts of the program to interact with it
2. Efficiency on memory management. When a pointer is returned, an unnecessary copy is avoided since the memory address of the data is returned
3. Control the life time of objects. When a pointer related to a dynamically created object (for example, using "new"), it's possible to control how long does
the object exist. The object can still exist after the function that created it has ended its execution.
4. Functions that return multiple values. Return a pointer to a data structure or array can be a more efficient way to return multiple values, especially if the size of the result is unknown in advance
5. Interface of polymorfic functions. It allows that the function returns objects from any of the derived classes, maintaining the flexibility and allowing the code that
calls treating those objects in a uniform way through pointers to the base class. 

*/

#include <iostream>
#include <string>
using namespace std;

// Definition of the car class

class Coche{

    //property model of Coche
    private:  //private properties
        string modelo;
    
    //the constructor has to be accessible from outside the class. Must have same name as the class
    public: 
        Coche (String mod): modelo(mod){}

    //method to obtain the model of the car
    string getModelo() const{  //string specifies the return data type. Const means that nothing is going to change when calling getModelo

        return modelo;
    }


};


//Function that creates a new Coche and returns a pointer to it 

Coche* crearCoche(string modelo){     //returns a pointer of type Coche

    Coche* nuevoCoche=new Coche(modelo); //creation of the pointer nuevoCoche

    return nuevoCoche;   //return the pointer
}                  

int main(){

    //Create Coche calling the function crearCoche

    Coche* miCoche=crearCoche("Mazda MX5");   //creation of a Coche, which is a pointer and needs to be saved in a pointer

    //Access to the model of the car through the pointer

    cout << "Modelo del coche: " << miCoche->getModelo() << endl; 

    //It's important to free the memory when we don't need the object anymore

    delete miCoche;
}