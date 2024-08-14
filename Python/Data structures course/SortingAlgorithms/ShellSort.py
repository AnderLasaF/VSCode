#Remove all the repeating occurances of elements while sorting. If compared values are the same, we will delete one of the two elements we are comparing before starting the next pass for the reduced gap
#For example, given the unsorted list [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3], after sorting using shell sort without duplicates, the sorted list would be: [0, 1, 2, 3, 5, 7, 8, 9]

def shell_sort(arr):
    size = len(arr)
    gap = size//2
    count=0

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
            if arr[j]==arr[j-gap]:
                del arr[j-gap]   #the problem deleting is that the index i will go up to the original size of the list -1, so that needs to be tackled
                size-=1
                count+=1  #auxiliar variable for stopping the for loop and don't go out of range
            if i==abs(size-count) or i==size:  #we have reached the maximum size of the array after deleting duplicate element(s)
                break   #this way does not work, I need to make it generic
        gap = gap // 2

if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [5,5,5,5,5],
        [1,2,1,4,6],
        [234,3,1,56,34,12,9,12,1300],
        [5]
    ]
    elements = [89,78,61,53,23,21,17,12,9,7,6,2,1]
    for elements in tests:
        shell_sort(elements)
        print(elements)