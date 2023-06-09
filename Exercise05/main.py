'''
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод:   Вывод:
300     220 284
'''

def sum(_n):
    _sum = 0
    for _i in range(1, _n):
        if _n % _i == 0:
            _sum += _i
    return _sum

_k = int(input("Введите максимальное число, до которого программа будет искать дружественные числа: "))

_friendly_pairs = list()
for _n in range(1, _k):
    _a = sum(_n)
    if _a > _n and _a < _k:
        _b = sum(_a)
        if _b == _n:
            _friendly_pairs.append((_n, _a))
print(_friendly_pairs)