def SumList(arr):

    if len(arr)==0:   #corner case, try catch could tackle it better
        return 0
    
    if len(arr)==1:   #base case
        return arr[0]
    
    return arr[0] + SumList(arr[1:])  #in the recursive call we supress the first element of the array until we reach the base case: array of 1 element

if __name__ == '__main__':
    print("The sum of",[-5,1,3,7],"is:",SumList([-5,1,3,7]))
