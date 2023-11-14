#Find index of all the occurances of a number from sorted list
# numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
# number_to_find = 15

from util import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index,index_list=None):
    
    if index_list ==None:
        index_list = []
    if right_index < left_index:  
        return -1

    mid_index = (left_index + right_index) // 2  #mid index, we are checking it's associated value
    if mid_index >= len(numbers_list) or mid_index < 0:  
        return -1

    mid_number = numbers_list[mid_index]  #number to compare with the one to find

    if mid_number == number_to_find:  #found the number, keep counting recursively in both halves

        index_list.append(mid_index)  #improve the algorithm to make the least amount of steps possible
        binary_search_recursive(numbers_list, number_to_find, left_index, mid_index-1,index_list)
        binary_search_recursive(numbers_list, number_to_find, mid_index+1, right_index, index_list)
        
        
    if mid_number < number_to_find:  #the number may be on the right side of mid_number
        left_index = mid_index +1
        binary_search_recursive(numbers_list, number_to_find, mid_index + 1, right_index, index_list)
    else:                            #the number may be on the left side of mid_number
        right_index = mid_index -1
        binary_search_recursive(numbers_list, number_to_find, left_index, mid_index -1, index_list)
    return sorted(index_list) #recursive call, we did not find the number

if __name__ == '__main__':
    #numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    #numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    numbers_list = [0,5,5,5]   #it does not work well if all the elements are the same
    number_to_find = 5
    #number_to_find = 21

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list)-1)
    print(f"Number found at index(es) {index} using binary search")

    #thinking about the algorithm

    #we start with the middle number. If that number is the one we are looking for, we make a recursive call
    #if the actual number is lower than the number to be found, we increase the index and do a recursive call
    #if the actual number is higher than the number to be found, we decrease the index and do a recursive call