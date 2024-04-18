#Please check the attached txt file for a more detailed explanation of the problem

#Brief explanation: Santa has a limited budget to deliver presents in Christmas time in The Netherlands. He wants to make sure that
#each kid of the cities where he will deliver gets one present, otherwise he should try in a different city. Since checking all the 
#options will be time consuming, he gives the chance to check five times over the limit with the algorithm to be designed. 

#His employees are 100, divided in one Centurion, 9 Decurions and 90 elfs. The elfs are responsible for delivering the presents to 
#the kids, but each of them can only deliver a present per round. Each employee has a different salary, so this should be taken 
#into account. It is assumed a population of 12% of kids per city for the algorithm. The data is imported from an Excel file containing
#the population for each city/village in the country. 

#Every round will be composed of 90 elfs, therefore, the children populations that are a multiple of 90 or as close as possible,
#will be picked up the first ones, since they have a cost per-present lower. (Further explain in a function at the bottom of this file)

import math
from openpyxl import load_workbook #library to read/write excel file in python
from collections import Counter  #container that holds the count of each of the elements in the container. Sub-class in the dictionary class

#Constants
budget = 3000000 #available budget to deliver presents. The edge case of cost is 22919910
cost_centurion = 100 #cost of a centurion per round 
cost_decurion = 50  #cost of a decurion per round 
cost_elf = 10 #cost of an elf per round
totalcost=0  #store the total cost of the delivery
check=False  #check for the cost every round when we are close to the budget 
over_budget=False   #boolean to check if we crossed the budget limit
over_budget_times=0  #check how many times we went over the budget limit
over_budget_times_limit=5  #check up to five times over the limit in order to get closer to the budget

#Lists/dictionaries
delivered_cities=[]  #placeholder for the cities that have been fully delivered
cities_dict = {}  #dictionary to save the pair key value for city and children population from the excel file
cities_dict_multipleof90 = {} #dictionary to save the pair key value for a city and children population multiple of 90


def ChildrenPopulationRounded(filename): #function returns a pair key value with the city and population of children (12%, assumed value) floored
    workbook = load_workbook(filename) #open the Excel file
    worksheet = workbook.worksheets[0] #get the first sheet
    for row in worksheet:
        if row[0].value =="city": #skip the first row since it has no relevant data
            continue
        cities_dict[row[0].value]=(row[7].value*12)//100 #round floor, any rounding in this case is fine. Row 0 constains the city and row 7 the population
        cities_dict_multipleof90[row[0].value]=(cities_dict[row[0].value]%90) #modulus gives us the "distance" to a full round (90 elfs) for the last round of every city
    return cities_dict,cities_dict_multipleof90


def get_keys_from_value(dict, val): #returns a list with the keys that matches a specific value
    return [k for k, v in dict.items() if v == val]


def fullroundscost(totalcost,rounds): #function that calculates the cost of all full rounds
    global over_budget
    global over_budget_times
    cost_of_rounds=rounds*(cost_centurion+cost_decurion*9+cost_elf*90)  #total cost of full rounds
    if totalcost+cost_of_rounds>budget:  #budget exceeded
                        over_budget=True  #we jump to the next city
                        over_budget_times+=1
    return cost_of_rounds


def notfullroundcost(totalcost,costfullrounds,elfs):
        global over_budget
        global over_budget_times
        cost=cost_centurion+cost_decurion*min(math.ceil(elfs/9),9)+elfs*10  #the min expression is used to cap the number of decurions for a value >=81 for the elfs
        if cost+costfullrounds+totalcost>budget:  #budget exceeded
            over_budget=True  #jump to next city
            over_budget_times+=1
        return cost


def cost(totalcost,index,cities_dict,dict_sorted):  #function that calculates the cost
    global over_budget
    global over_budget_times
    global delivered_cities

    if totalcost==0:  #first round
        citieslist=get_keys_from_value(dict_sorted,0) #cities that only have full rounds
        for city in citieslist:
            rounds=cities_dict[city]//90  #number of full rounds
            totalcost=fullroundscost(totalcost,rounds)  #cost of all the full rounds
            if over_budget:
                  over_budget=False  #reset boolean value
                  continue   #check next city
            delivered_cities.append(city)  #add delivered city to the list
        return cost(totalcost,89,cities_dict,dict_sorted)  #start recursive calls with the populations closest to the most efficient ones price-per-present wise
    else: 
        citieslist=get_keys_from_value(dict_sorted,index)     #list of cities associated to a specific index
        for city in citieslist:   #if the list is empty we jump to the next index
            if index>0:  #we are still iterating over the list, first value has been 0
                rounds=cities_dict[city]//90  #number of full rounds  
                cost_full_rounds=fullroundscost(totalcost,rounds) #cost of all the fullrounds
                cost_non_full_rounds=notfullroundcost(totalcost,cost_full_rounds,cities_dict_multipleof90[city]) #cost of the non-full round
                if over_budget==False: #as long as we're not over the limit, we increase the cost
                    totalcost=totalcost+cost_full_rounds+cost_non_full_rounds  #this value is going over the limit
                    delivered_cities.append(city)  #city delivered, to the list
                else:   
                    over_budget=False  #reset the boolean
                    continue #jump to the next city
            else:
                break
        if over_budget_times>over_budget_times_limit:  #we are not trying to check for a new city
            over_budget=True
            return totalcost
        else:
            if index>0:  #still going through cities, 0 was the first attempt (best case)
                index-=1 
                return cost(totalcost,index,cities_dict,dict_sorted) #recursive call for the next index
             

def main():

    cities_dicts=ChildrenPopulationRounded("nl.xlsx")  #place the xlsx file in the same location the py file
    cities_dict=cities_dicts[0]  #split the dicts from the tuple
    cities_dict_multipleof90=cities_dicts[1]
    dict_sorted=Counter(cities_dict_multipleof90)  #we sort the dictionary in order to start from the cases closer to the ideal scenario (higher modulus with 90) 
    #first we check the cities that are a perfect match for the algorithm (the ones whose children population is multiple of 90)
    print("The total cost is: ",cost(totalcost,0,cities_dict,dict_sorted),"and the fully delivered cities have been: ",delivered_cities)

if __name__=="__main__":
    main()    



"""
This function calculates the optimal number of elfs for non complete rounds (<90 elfs). The return value is 89, the value we start looking from 
when we don't have a complete round. Another approach is to see the cost as a limit when the number of elfs increases.

def Costperpresent():
    costoptimal =1450 #cost per round
    for i in range(1,90,1):
        cost = (cost_centurion+math.ceil(cost_decurion*i/9)+i)/i
        print("cost per present for ",i,"elfs is: ",cost)
        if cost<costoptimal:
            optimalelfs=i
            costoptimal=cost  #update the optimal cost

    return costoptimal,optimalelfs
Costperpresent()
"""