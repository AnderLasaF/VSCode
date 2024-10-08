def shell_sort_original(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

def shell_sort(arr):
    n = len(arr)
    div = 2
    gap = n//div
    while gap > 0:
        index_to_delete = []
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >= temp:
                if arr[j-gap] == temp:
                    index_to_delete.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        index_to_delete=list(set(index_to_delete))
        index_to_delete.sort()
        if index_to_delete:
            for i in index_to_delete[-1::-1]:
                del arr[i]
        div *= 2
        n = len(arr)
        gap = n//div

def foo(arr):
    size = len(arr)
    gap = size // 2
    gap = 3
    for i in range(gap, size):
        anchor = arr[i]
        j = i
        while j>=gap and arr[j-gap]>anchor:
            arr[j] = arr[j-gap]
            j -= gap
        arr[j] = anchor

if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [5]
    ]
    elements = [89,78,61,53,23,21,17,12,9,7,6,2,1]
    for elements in tests:
        shell_sort(elements)
        print(elements)