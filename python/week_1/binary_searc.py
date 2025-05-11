def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError("value not in array")

    left_index = 0
    right_index = len(search_list) - 1

    while left_index <= right_index:
        mid = (left_index + right_index) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] > value:
            right_index = mid - 1
        elif search_list[mid] < value:
            left_index = mid + 1

    raise ValueError("value not in array")

def print_result():
    #search_list = [4, 8, 12, 16, 23, 28, 32]
    search_list = [4, 8, 12, 23, 28, 32]
    search_list = [1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634]
    search_list = [144]
    #search_list = []
    value = 144
    print(find(search_list, value))

if __name__ == '__main__':
    print_result()