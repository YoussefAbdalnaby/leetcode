arr = [1, 4, 5, 6, 7, 10, 11]
l = 0
r = len(arr) - 1
target = 9

while l < r:
    current = arr[l] + arr[r]
    if current < target:
        l += 1
    elif current > target:
        r -= 1
    else:
        print(l, r)
        l += 1
