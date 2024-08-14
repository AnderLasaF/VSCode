#include <iostream>
using namespace std;

int main(){

    int number_prime;
    bool is_number_prime=true;
    int aux=number_prime;

    cout << "Number (positive) to be checked if it's prime or not: ";
    cin >> number_prime;

    while(is_number_prime){
            if (number_prime%(aux-1)!=0 && aux>=1){
                aux-=1; 
            }
            else{
                is_number_prime=false;
                break;
            }

    }
    if (is_number_prime){
        cout << "True";
    }
    else{
        cout << "False";
    }
        
}