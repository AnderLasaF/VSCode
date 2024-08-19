#include <iostream>
using namespace std;

/*Situations where it's needed to access to properties and methods through pointers:
    - Dynamic memory management (creation of objects during execution time)
    - Inheritage and polymorphism
    - Dynamic data structures (trees, nodes, dynamic lists)
    - Parsing objects as arguments to functions
    - Design patterns
    - Etc.
*/

class Coche{

    //attributes or properties
    
    //all the attributes are encapulated, since they are defined as private by default
    string modelo;
    int cilindrada;
    int potencia;
    string color;
    double precio;


    //methods or behavior
    //by default the methods are private on C++. If we want to use them outside the class we have to define them as public

    public:
    void setPrecio(double p){  //method to modify the property precio so we don't access the property precio directly

        if (p>0){
            precio = p;
        }
        else{
            precio = 15000;
        }  
    }

    double getPrecio(){

        return precio   
    }
    public:
    //below the word "public" all the methods will now be public. If we want some of them to be private, we should type private:. All the methods after private will be private
    void arrancar(){

        cout << "El coche esta arrancado." << endl;
    }

    void acelerar(){

        cout << "El coche esta acelerando." << endl;
    }

    void frenar(){

        cout << "El coche esta frenando." << endl;
    }

    void girar(){

        cout << "El coche esta girando." << endl;
    }

    bool enMarcha(){

        return True;
    }

};

int main(){

    Coche coche_Maria; //first object of the Coche class

    Coche coche_Juan; 


    /*coche_Juan.arrancar(); //accessible from outside the class since it has been defined as a public method

    coche_Juan.setPrecio = 18000;  //modify the attribute precio through the method setPrecio

    cout << "El precio del coche es: " << coche_Juan.getPrecio << " euros" << endl;  //access the value precio*/

    //Create pointers to objects

    Coche* ptrCocheMaria = &coche_Maria;

    Coche* ptrCocheJuan = &coche_Juan;

    //Use the pointer to access the methods of the object coche_Juan

    ptrCocheJuan->setPrecio(37000); 

    cout << "El precio del coche es: " << ptrCocheJuan->getPrecio() << " euros" << endl;  //access the value precio*/
    
    //Using the pointer to access the methods of coche_Maria

    ptrCocheMaria->acelerar();

    return 0;
}