#include <iostream>    
using namespace std;

int main(){ 

    const string name = "Juan"; //defined as constant, we have to declare and define it in the same sentence 

    //list initialization for the variable age
    int age{21};

    double salary;

    cout << "Introduce the salary of the employee: "; //console out
    cin >> salary; //console in 

    cout << "Introduce the age of the employee: ";
    cin >> age;

    cout << "-----------------------------------------------------" << endl;

    cout << "Employee data: " <<endl;
    cout << "Name: " << name << ". Age: " << age << ". Salary: " << salary; //string concatenation
}
 