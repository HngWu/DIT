def SortedSequentialSearch(theValues, target):
    n = len(theValues)

    #theValues.sort()
    for i in range(n):
        if theValues[i] == target:
            return True
        elif theValues[i] > target:
            return False
    return False


def BinarySearch(theValues, target):
    low = 0
    high = len(theValues) - 1
    while low <= high:
        mid = (low + high) // 2
        if theValues[mid] == target:
            return mid
        elif theValues[mid] < target:
            low = mid + 1
        elif theValues[mid] > target:
            high = mid - 1
        else:
            return - 1


print(BinarySearch([1,2,3,4,5,7,9,32,67,89,90], 32))