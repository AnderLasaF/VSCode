# you can use this to sort strings too

#Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,

#elements = [
#        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#    ]

#bubble_sort function should take key from a transaction record and sort the list as per that key. For example,

#bubble_sort(elements, key='transaction_amount')
#This will sort elements by transaction_amount and your sorted list will look like,

#elements = [
#        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#    ]

#But if you call it like this,

#bubble_sort(elements, key='name')
#output will be,

#elements = [
#        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#    ]



def bubble_sort(elements,key_in=None):  #adding the None allows to have the normal bubble sort if no argument is parsed
    size = len(elements)

    for i in range(size-1):  #number of "lines" in elements
        swapped = False
        for j in range(size-i-1):
            #for key in elements[j]:  #iterate the keys of every line in elements. THIS IS VERY INNEFICIENT!!!!
                #if key==key_in and elements[j][key] > elements[j+1][key]: #we only do the check if the key is the one we want
                if elements[j][key_in] > elements[j+1][key_in]:   #we only check the specified key, no more no less 
                    tmp = elements[j]
                    elements[j] = elements[j+1]
                    elements[j+1] = tmp
                    swapped = True

        if not swapped:  #we have to check if they've been swapped after a whole inner for (outer = i, inner = j)
            break
    
    return elements

if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3,4,2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    elements_dict = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    print(bubble_sort(elements_dict,'name'))
    print(bubble_sort(elements))
    #print(elements[0])