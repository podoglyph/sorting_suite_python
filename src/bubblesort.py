def bubbleSort(unsorted):
    for n in range(len(unsorted)-1, 0, -1):
        for i in range(n):
            if unsorted[i] > unsorted[i + 1]:
                p_temp = unsorted[i]
                unsorted[i] = unsorted[i + 1]
                unsorted[i + 1] = p_temp
    sorted_list = unsorted
    return sorted_list