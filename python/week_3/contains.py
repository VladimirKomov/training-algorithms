# 1. Проверка наличия элемента в списке
# Напишите функцию, которая проверяет, содержится ли элемент x в списке lst.
from collections import Counter


def contains(lst, x):
    return (x in lst)



# 2. Поиск пропущенного числа в диапазоне [1..100]
# Напишите функцию, которая возвращает пропущенное число из списка длиной 99, содержащего числа от 1 до 100.
def find_missing_number(lst):
    set_missing_number = set(lst)
    set_number = set(range(1, len(lst) + 1))
    return set_number - set_missing_number


list_for_search = list(range(1, 101))
list_for_search.remove(50)


# 3. Поиск повторяющихся элементов в списке
# Напишите функцию, которая возвращает список дубликатов из списка чисел.
def find_duplicates(lst):
    duplicates = set()
    seen = set()
    for num in lst:
        if num in duplicates:
            seen.add(num)
        duplicates.add(num)
    return list(seen)


list_for_duplicates = [1,1,2,3,4,5,5,6,7,8,9,3,3]

# 3.1 Поиск повторяющихся элементов в списке c количеством повторений
# Напишите функцию, которая возвращает сколько раз число встречается в списке
def find_duplicates_2(lst):
    count_number = {}
    for num in lst:
        count_number[num] = count_number.get(num, 0) + 1
    return count_number


# 4. Пересечение двух списков
# Напишите функцию, которая возвращает пересечение двух списков lst1 и lst2.
def intersect(lst1, lst2):
    seen = set(lst1) & set(lst2)
    return seen

list_intersect_1 = list(range(1, 101))
list_intersect_2 = [4, 55, 99]

# if __name__ == '__main__':
#     print(intersect(list_intersect_1, list_intersect_2))

# 5. Проверка анаграмм
# Напишите функцию, которая проверяет, являются ли строки s1 и s2 анаграммами.
def is_anagram(s1, s2):
    s1_normalized = Counter(i.lower() for i in s1 if i.isalpha())
    s2_normalized = Counter(i.lower() for i in s2 if i.isalpha())
    return s1_normalized == s2_normalized

s1 = "Hello"
s2 = "World"
s3 = "olleh"

# if __name__ == '__main__':
#     print(is_anagram(s1, s2))
#     print(is_anagram(s1, s3))
#     print(is_anagram(s2, s3))


# 6. Удаление дубликатов из списка
# Напишите функцию, которая удаляет все дубликаты из списка и возвращает его.
def remove_duplicates(lst):
    # return list(set(lst))
    seen = set()
    for num in lst:
        if num not in seen:
            seen.add(num)
    return list(seen)

list_remove_duplicates = list(range(1, 101))
list_remove_duplicates.append(4)
list_remove_duplicates.append(8)
list_remove_duplicates.append(99)

# if __name__ == "__main__":
#     print(remove_duplicates(list_remove_duplicates))


# 7. Реверс строки (рекурсия)
# Напишите функцию, которая возвращает строку в обратном порядке, используя рекурсию.
def reverse_string(s):
    if len(s) < 2:
        return s
    s_rev = reverse_string(''.join(s[1:])) + s[0]
    return s_rev

# if __name__ == '__main__':
#     print(reverse_string('list_intersect_1'))


# 8. Поиск пар чисел с заданной суммой
# Напишите функцию, которая находит все уникальные пары чисел из списка, сумма которых равна x.
def find_pairs_with_sum(lst, x):
    seen = set()
    pairs = set()
    for num in lst:
        i = x - num
        if i in seen:
            pairs.add((min(num, i), max(num, i)))
        seen.add(num)
    return list(pairs)

list_pairs = list(range(1, 101))

# if __name__ == '__main__':
#     print(find_pairs_with_sum(list_for_search, 50))

# 9. Генерация n чисел Фибоначчи
# Напишите функцию, которая генерирует первые n чисел Фибоначчи.
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    for i in range(2, n):
        next_one = result[i - 2] + result[i - 1]
        result.append(next_one)

    return result

# if __name__ == '__main__':
#     print(fibonacci(20))



# 10. Проверка палиндрома
# Напишите функцию, которая проверяет, является ли строка палиндромом.
def is_palindrome(s):
    s_normalized = [latter.lower() for latter in s if latter.isalpha()]
    print(s_normalized)
    s_reversed = s_normalized[::-1]
    return s_normalized == s_reversed


polindrome = 'А роза упала на лапу Азора'

# if __name__ == '__main__':
#     print(is_palindrome(polindrome))

# 11. Быстрая сортировка (quicksort)
# Реализуйте алгоритм быстрой сортировки.
def quicksort(lst):
    if len(lst) <= 1:
        return lst

    first = lst[0]
    left = [x for x in lst[1:] if x >= first]
    right = [x for x in lst[1:] if x < first]

    return quicksort(left) + [first] + quicksort(right)

# if __name__ == '__main__':
#     print(quicksort([1,7,3,9, 9,4]))

# 12. Все перестановки строки
# Напишите функцию, которая возвращает все уникальные перестановки символов строки.
def get_permutations(s):
    if len(s) <= 1:
        return [s]

    permutations = set()

    for i in range(len(s)):
        current = s[i]
        rest = s[:i] + s[i+1:]

        for p in get_permutations(rest):
            permutations.add(current + p)

    return sorted(permutations)


if __name__ == '__main__':
    print(get_permutations('привет'))


