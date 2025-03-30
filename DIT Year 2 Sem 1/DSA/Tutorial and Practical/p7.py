def mergeSort( theList ):
# Check the base case - the list contains a single item
    if len(theList) <= 1:
        return theList
    else:
        # Compute the midpoint
        mid = len(theList) // 2
        # Split the list and perform the recursive step
        leftHalf = mergeSort( theList[ :mid ] )
        rightHalf = mergeSort( theList[ mid: ] )
        # Merge the two sorted sublists
        newList = mergeSortedLists( leftHalf, rightHalf)
        return newList


,

list_of_numbers = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]
print('Input List:', list_of_numbers)
merge_list = mergeSort(list_of_numbers)
print('Sorted List:', merge_list)

