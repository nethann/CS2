def selection_sort(str, isAscending=True):
    input_list = list(str)
    n = len(input_list)
    swap_count = 0

    for i in range(n - 1):
        index_of_min_max = i
        for j in range(i + 1, n):
            if (isAscending and input_list[j] < input_list[index_of_min_max]) or (not isAscending and input_list[j] > input_list[index_of_min_max]):
                index_of_min_max = j
        if index_of_min_max != i:
            input_list[i], input_list[index_of_min_max] = input_list[index_of_min_max], input_list[i]
            swap_count += 1

    return ''.join(input_list), swap_count

input_string = "Nethan"

# Ascending order
sorted_string, swaps = selection_sort(input_string, True)
print(f"Ascending: {sorted_string}, Swaps: {swaps}")

# Descending order
sorted_string, swaps = selection_sort(input_string, False)
print(f"Descending: {sorted_string}, Swaps: {swaps}")

sorted_string, swaps = selection_sort(input_string)
print(f"Default (Ascending): {sorted_string}, Swaps: {swaps}")




