random_list = [1,2,3,4,5,6,7,8,9,10,12,234,344,45,456,56,756,4645,23,42,3443,65,464576,457,23,4523,424,5354,243]

sorted_list = sorted(random_list)
counter = 0

def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    print(sorted_list)
    mid = (high + low) // 2
    global counter
    counter += 1

    if mid == 0:
        if sorted_list[low] == target:
            return low + counter*2 - 1
        if sorted_list[high] == target:
            return high + counter*2 - 1
    if sorted_list[mid] == target:
        return mid + counter*2 + 1
    elif sorted_list[mid] > target:
        return binary_search(sorted_list[:mid], target)
    elif sorted_list[mid] < target:
        return binary_search(sorted_list[mid:], target)
    else:
        return -1

# print(binary_search(random_list, 10))

def binarySearch(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (high + low) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


print(binarySearch(random_list, 234))