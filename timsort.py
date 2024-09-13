def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(arr, left, mid, right):
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    left_index = right_index = 0
    for arr_index in range(left, right + 1):
        if left_index < len(left_arr) and (right_index == len(right_arr) or left_arr[left_index] <= right_arr[right_index]):
            arr[arr_index] = left_arr[left_index]
            left_index += 1
        else:
            arr[arr_index] = right_arr[right_index]
            right_index += 1

def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merge(arr, start, midpoint, end)
        size *= 2

    return arr

# Example usage
if __name__ == "__main__":
    import random

    # Generate a large random array
    arr = [random.randint(1, 1000) for _ in range(10000)]

    # Sort the array using Timsort
    sorted_arr = timsort(arr.copy())

    # Verify the sorting
    assert sorted_arr == sorted(arr), "Sorting failed!"
    print("Timsort implementation successful!")