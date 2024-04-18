#test

import OOPPrueba

def test_parking_negative_price(): #this test should fail, negative price
    Parking1 = OOPPrueba.Parking.validate_parking_arguments("Eindhoven",-2,3) 

#def test_parking_negative_spots(): #this test should fail, negative amount of spots
    #Parking1 = OOPPrueba.Parking("Eindhoven",-34,2) 