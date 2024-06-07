"""
    Есть упорядоченный массив целых чисел arr, нужно определить, есть ли в нём число X.
"""


def binary_search(arr, target):
    left_idx, right_idx = 0, len(arr)
    while left_idx < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if arr[mid_idx] == target:
            return mid_idx
        elif arr[mid_idx] < target:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx

    return False


my_arr = [i for i in range(1, 101)]
answer_binary = binary_search(my_arr, 60)
print(f"{answer_binary=}")

"""
    Пусть нам нужно найти решение уравнения x * log2(x) = Y
    Поскольку функция монотонно возрастает при x >= 1 можно применить
    бинарный поиск.
"""

# def solve_equation(value):
#     left, right = 1, value
#     for _ in range(100):
#         mid = (left + right) / 2
#         expr_result = mid * log2(mid)
#         if expr_result < value:
#             left = mid
#         else:
#             right = mid
#     return mid

"""
    Дана бинарная строка длины N, состоящая из 0 и 1. Гарантируется, что
    самый левый элемент 0 а самый правый 1
    Найти любое вхождение подстроки 01.
"""


def binary_substring(b_string):
    left_idx, right_idx = 0, len(b_string)
    while left_idx + 1 < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if b_string[mid_idx] == "0" and b_string[mid_idx + 1] == "1":
            return mid_idx, mid_idx + 1
        if b_string[mid_idx] == "0":
            left_idx = mid_idx
        else:
            right_idx = mid_idx

    return False


b_string = '01000011000001'
answer = binary_substring(b_string)
print(f"{answer=}")

"""
    Дан упорядоченный массив arr и число X, нужно найти индекс максимального элемента arr,
    не превосходящего X. Если такого элемента не существует, вернуть -1.
"""


def search_not_superior_el(arr, tar):
    if not arr or arr[0] >= tar:
        return -1

    left_idx, right_idx = 0, len(arr)
    while left_idx + 1 < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if arr[mid_idx] <= tar:
            left_idx = mid_idx
        else:
            right_idx = mid_idx

    return left_idx


my_arr2 = [i for i in range(1, 101)]
target = 60
answer_superior = search_not_superior_el(my_arr2, target)
print(f"{answer_superior=}")
