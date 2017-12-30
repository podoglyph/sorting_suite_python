def insertionSort(unsorted):
    sorted_list = []
    sorted_list.append(unsorted.pop(0))
    
    while len(unsorted) > 0:
        sorted_list.append(unsorted.pop(0))
        for i in range(len(sorted_list) - 1, 0, -1):
            if sorted_list[i] < sorted_list[i - 1]:
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[i - 1]
                sorted_list[i - 1] = temp
            
    return sorted_list

unsorted = [1, 0, 4, 3, 2, 22, 33, 14, 9, 45, 30]
print(insertionSort(unsorted))