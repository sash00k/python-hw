# Реализовать функцию flatten, распаковывающую
# список, элементы которого могут являться
# списками. Опционален параметр глубины распаковки
from functools import reduce


def flatten(lst: list, depth: int = -1) -> list:
    was_smth_unpacked = False

    lst_unpacked = []
    for elem in lst:
        if isinstance(elem, list):
            was_smth_unpacked = True
            lst_unpacked.extend(elem)
        else:
            lst_unpacked.append(elem)

    depth -= 1
    if depth == 0 or not was_smth_unpacked:
        return lst_unpacked

    return flatten(lst_unpacked, depth)


def func(x, y) -> list:

    return [x, y]


if __name__ == '__main__':
    arr = [1, 2, [3, [4]], 5]
    # print(flatten(arr)) # [1, 2, 3, 4, 5]
    print(reduce(func, arr))
    # print(flatten(arr, depth=1)) # [1, 2, 3, [4], 5]
    # print(flatten(arr, depth=2)) # [1, 2, 3, 4, 5]
