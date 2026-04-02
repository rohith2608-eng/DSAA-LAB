def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []

        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])

        return quickSort(left) + [pivot] + quickSort(right)


# Driver Code
arr = [10, 7, 8, 9, 1, 5]

print("Original array is:")
print(arr)

sorted_arr = quickSort(arr)

print("Sorted array is:")
print(sorted_arr)
