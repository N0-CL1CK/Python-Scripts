def getGap(gap): 
    return 1 if ((gap/1.3) < 1) else (int(gap/1.3))

def sort(array):
    length = len(array)
    gap = length
    is_swapped = True

    while gap != 1 or is_swapped == True:
        gap = getGap(gap)
        is_swapped = False
        for i in range(0, length-gap):
            if (array[i] > array[i+gap]):
                array[i], array[i+gap] = array[i+gap], array[i]
                is_swapped = True
    return array