def linear_search(arr, target):
    steps = 0
    for i, value in enumerate(arr):
        steps += 1
        if value == target:
            return i, steps
    return -1, steps

def binary_search(arr, target):
    steps = 0
    low, high = 0, len(arr) - 1

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid, steps
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps

def print_trace(search_type, target_index, steps):
    print(f"{search_type} search:")
    print(f"Target index: {target_index}")
    print(f"Total steps: {steps}")
    print()

# Example usage:
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
target_value = 7

# Perform linear search
linear_search_result, linear_search_steps = linear_search(my_tuple, target_value)
print_trace("Linear", linear_search_result, linear_search_steps)

# Perform binary search
binary_search_result, binary_search_steps = binary_search(my_tuple, target_value)
print_trace("Binary", binary_search_result, binary_search_steps)
