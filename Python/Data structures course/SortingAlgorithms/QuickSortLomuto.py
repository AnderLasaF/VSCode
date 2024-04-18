#Quick sort algorithm with Lomuto partition scheme. The idea is to choose the pivot as the last element in the array. The algorithm maintains index i as it scans the array using another index j such that the
#elements at start through end-1 (inclusive) are less than the pivot (last element = end), and the elements at i through j (inclusive) are equal to or greater than the pivot.  

#Sorts a (portion of an) array, divides it into partitions, then sorts those
def quicksort(elements,start,end):

    if start>=end or start<0:  #ensure indices are in correct order
        return 
    
    #partition array and get the pivot index
    pivot = partition(elements,start,end)

    #sort the partitions
    quicksort(elements,start,pivot-1)  #left side of the pivot
    quicksort(elements,pivot+1,end) #right side of the pivot

#Divides array into two partitions
def partition(elements,start,end):
    pivot = elements[end]  #choose last element as pivot

    #Temporary pivot index
    i = start -1

    for j in range(start,end-1):
        #if the current element is less than or equal to the pivot
        if elements[j] <= pivot:
           #move the temporary pivot index forward
           i = i+1
           #swap the current element with the element at the temporary pivot index
           tmp = elements[i]
           elements[i] = elements[j]
           elements[j] = tmp
    
    #move the pivot element to the correct pivot position (between the smaller and larger elements)
    i = i+1
    #swap the element at the temporary pivot index with the one in the end index
    tmp = elements[i]
    elements[i] = elements[end]
    elements[end] = tmp
    return i #the pivot index

elements = [3,7,1,8,0]
quicksort(elements,0,len(elements)-1)
print(elements)