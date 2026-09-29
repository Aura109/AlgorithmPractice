def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for i in arr[1:]:
            if i < pivot:
                less.append(i)
            else:
                greater.append(i)
        return quick_sort(less) + [pivot] + quick_sort(greater)


example = [1, 3, 2, 4, 5, 6, 45,243,4567,234,456,568,769,234,124,345,7578,579,3645,562245,4567,87658]
print(quick_sort(example))