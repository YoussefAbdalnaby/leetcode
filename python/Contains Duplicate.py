def has_duplicates(arr):
    hashset = set()

    for n in arr:
        if n in hashset:
            return True
        hashset.add(n)

    return False
arr_input = input("Enter numbers separated by spaces: ")
arr = [int(x) for x in arr_input.split()]

print(has_duplicates(arr))
