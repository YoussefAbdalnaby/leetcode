arr_input = input("Enter numbers separated by spaces: ")
arr = [int(x) for x in arr_input.split()]
ans = []
start = 0
end = 0
i = 0
n = len(arr)
s=set(arr)

while i < n:
    start = i
    while arr[i] + 1 in s:
        i += 1
    end = i
    if start-end == 0:
        ans.append(str(arr[start]))
    else:
        ans.append(str(arr[start]) + '--->' + str(arr[end]))
    i += 1

print(ans)
