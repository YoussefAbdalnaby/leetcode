arr_input = input("Enter numbers separated by spaces: ")
arr = [int(x) for x in arr_input.split()]

target = int(input("Enter target sum: "))

arr.sort()

l = 0
r = len(arr) - 1
found = False

print(f"Looking for pairs that sum to {target} in array: {arr}")

while l < r:
    current = arr[l] + arr[r]
    if current < target:
        l += 1
    elif current > target:
        r -= 1
    else:
        print(f"Found pair: {arr[l]} + {arr[r]} = {target} (indices {l}, {r})")
        found = True
        l += 1

if not found:
    print("No pair found that sums to the target.")
