def partition(array, low, high):
    center = (low + high)//2
    loc = (low + center)//2
    roc = (high + center)//2

    nums = [array[low], array[high], array[center], array[loc], array[roc]]
    indices = [low, high, center, loc, roc]

    sortedNums = sorted(nums)
    print("5 Numbers : "+str(sortedNums))

    pivot = sortedNums[2]
    pivotIndex = indices[nums.index(pivot)]

    print("Pivot =", pivot)

    array[pivotIndex],array[high] = array[high], array[pivotIndex]
    
    i = low - 1

    for j in range(low, high+1):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        print(f'{array[low:pi]} , {array[pi:high+1]}\n')

        quickSort(array, low, pi - 1)

        quickSort(array, pi, high)


# data = [1, 7, 4, 1, 10, 9, -2]
data = [10, 80, 30, 90, 40, 40, 70]

# data = [90, 80, 70, 60, 50, 30, 20]

print("Unsorted Array")
print(data)
print()

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)