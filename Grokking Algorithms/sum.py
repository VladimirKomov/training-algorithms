
def sum_arr(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_arr(arr[1:])

def count_elements(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_elements(arr[1:])

def find_max_number(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        sub_arr = arr[1:]
        return arr[0] if arr[0] > arr[1] else find_max_number(sub_arr)

def binary_search(arr, number):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == number:
            return mid
        if arr[mid] < number:
            left = mid + 1
        if arr[mid] > number:
            right = mid - 1
    return -1

def rec_binary_search(arr, number, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == number:
        return mid
    if arr[mid] < number:
        return rec_binary_search(arr, number, mid + 1, right)
    if arr[mid] > number:
        return rec_binary_search(arr, number, left, mid - 1)


if __name__ == '__main__':
    print(sum_arr([2, 4, 1]))
    print(count_elements([2, 4, 1]))
    print(find_max_number([9, 4, 7]))
    print(binary_search([1, 2, 3, 4, 5], 4))
    print(rec_binary_search([1, 2, 3, 4, 5], 5))