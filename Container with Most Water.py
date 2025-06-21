def max_area(arr):
    r = len(arr) - 1
    l = 0
    maximum_area = 0
    while l < r:
        new_area = (r - l) * min(arr[l], arr[r])
        maximum_area = max(maximum_area, new_area)
        if arr[r] > arr[l]:
            l += 1
        elif arr[r] < arr[l]:
            r -= 1
        else:
            r -= 1
    return maximum_area


arr_input = input("Enter numbers separated by spaces: ")
arr = [int(x) for x in arr_input.split()]

print(max_area(arr))