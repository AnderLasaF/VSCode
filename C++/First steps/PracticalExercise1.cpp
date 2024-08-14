#include <iostream>    
#include <math.h>
using namespace std;

int main(){ 

    const double IVA{0.21}; 
    const int valid_days_offer{30};
    const double price_medium_quality_metres{35.5};
    const double price_high_quality_metres{55.3};

    int medium_quality_metres{0};  //introduced by user, initialized with 0
    int high_quality_metres{0}; //introduced by user
    
    double offer;


    cout << "Introduce the amount of medium quality metres: "; 
    cin >> medium_quality_metres;

    cout << "Introduce the amount of high quality metres: ";
    cin >> high_quality_metres;

    cout << "-----------------------------------------------------" << endl;

    cout << "Amount without taxes: ";
    cout << round(((medium_quality_metres*price_medium_quality_metres)+(high_quality_metres*price_high_quality_metres))) << "€" << endl;

    cout << "Taxes: ";
    cout << round(((medium_quality_metres*price_medium_quality_metres)+(high_quality_metres*price_high_quality_metres))*(IVA)) << "€" <<endl;

    cout << "The total amount of the offer is: " << round(((medium_quality_metres*price_medium_quality_metres)+(high_quality_metres*price_high_quality_metres))*IVA+
    ((medium_quality_metres*price_medium_quality_metres)+(high_quality_metres*price_high_quality_metres))) << "€" << endl;
    cout << "This offer is valid for " << valid_days_offer << " days"; 
}
 