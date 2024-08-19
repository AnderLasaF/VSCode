#include <iostream>
using namespace std;

int main(){

    char idioma, categoria;

    cout << "Selecciona el idioma, por favor (E : Espanol, I: Ingles)";

    cin >> idioma;

    switch (idioma){

        case 'E':  //both cases are taken into account
        case 'e':

            cout << "Selecciona la categoria (L: Libros, R: Ropa, T: Tecnologia)";
            cin >> categoria;

            switch(categoria){ //nested switch

                case 'L':
                case 'l':

                    cout <<"Has escogido la categoria Libros";
                    break;
    
                case 'R':
                case 'r':

                    cout <<"Has escogido la categoria Ropa";
                    break;

                case 'T':
                case 't':

                    cout <<"Has escogido la categoria Tecnologia";
                    break;
                    
                default:

                    cout <<"Categoria no valida";
            }
        break;

        case 'I':  //both cases are taken into account
        case 'i':

            cout << "Select a category (B: Books, C: Clothing, T: Technology)";
            cin >> categoria;

            switch(categoria){ //nested switch

                case 'B':
                case 'b':

                    cout <<"You have selected Books category";
                    break;
    
                case 'C':
                case 'c':

                    cout <<"You have selected Clothing category";
                    break;

                case 'T':
                case 't':

                    cout <<"You have selected Technology category";
                    break;
                    
                default:

                    cout <<"Invalid category";
            }
        break;

        default:
                cout << "Idioma no valido";
    }
}