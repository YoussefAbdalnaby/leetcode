def majority_element(arr):
    result,count=0,0
    for n in arr:
        if count==0:
            result = n
        count+=(1 if n==result else -1)
    return result

arr_input = input("Enter numbers separated by spaces: ")
arr = [int(x) for x in arr_input.split()]

print(majority_element(arr))