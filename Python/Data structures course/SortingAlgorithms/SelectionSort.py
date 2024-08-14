def selection_sort(arr,A,B):
    size = len(arr)
    for i in range(size-1):
        min_index = i  #fix the pivot
        for j in range(min_index+1,size): #iterate over the array except for the last element, eventually it will be sorted 
            if arr[j][A] < arr[min_index][A] or (arr[j][A] == arr[min_index][A] and arr[j][B]<arr[min_index][B]):  
                #if the first name is lower than the pivot or they are the same but the last name is lower than the one of the pivot
                min_index = j
        if i != min_index:  #we proceed to swap since we found a lower element
            arr[i][A], arr[min_index][A] = arr[min_index][A], arr[i][A]
            arr[i][B], arr[min_index][B] = arr[min_index][B], arr[i][B]


if __name__ == '__main__':

    keys_list = []
    sequence_list_to_sort =[
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]    
    for key in sequence_list_to_sort[0].keys():
            keys_list.append(key)

#RAJ: print(sequence_list_to_sort[0][keys_list[0]])
#NAYYAR: print(sequence_list_to_sort[0][keys_list[1]])

#IT IS WORKING BUT I HAVE TO TAKE INTO ACCOUNT THE SORTING ON THE LAST NAME. ARMAAN DADRA SHOULD BE BEFORE THAN ARMAAN KUMAR.

selection_sort(sequence_list_to_sort,keys_list[0],keys_list[1])
print(sequence_list_to_sort)