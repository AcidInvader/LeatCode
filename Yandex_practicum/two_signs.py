"""
    Учитывая свойство монотонности задачу можно было бы решить так: допустим,
    у нас есть два указателя — left и right. Если сумма подмассива [left; right) равна X — ответ найден.
    Если она меньше X, попробуем добавить элемент right к сумме, а если больше — уберём left.
    Изначально left = right = 0. Таким образом, мы для каждого left посмотрим указателем right
    на соответствующую потенциальную правую границу полуинтервала и не пропустим ответ, если он существует.
    Поскольку при смещении указателя мы можем быстро пересчитать сумму, общее время работы будет линейным.
    Запишем это в коде.
"""

def subarray_sum(non_negative_arr, target):
    right, current_sum = 0, 0
    for left in range(len(non_negative_arr)):
        # пересчитываем сумму
        if left > 0:
            current_sum -= non_negative_arr[left - 1]

        # при необходимости двигаем правую границу
        while right < len(non_negative_arr) and current_sum < target:
            current_sum += non_negative_arr[right]
            right += 1

        if current_sum == target:
            return True

    return False