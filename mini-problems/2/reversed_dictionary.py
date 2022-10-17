# Написать программу, которая по заданном словарю
# составляет обратный словарь, в котором значения и ключи
# поменялись местами. При этом:
#
# 1. Если значения оказались не hashable, то создания
# обратного словаря прерывается с TypeError
# 2. Если разным ключам соответствовало одно и тоже
# значение, то в качестве значения в обратном
# словаре использовать tuple из ключей
#
# Пример: {'Ivanov': 97832, 'Petrov': 55521, 'Kuznecov': 97832}
# -> {97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'}

def reversed_dict(input_dict: dict) -> dict:
    output_dict = dict()

    for key, value in input_dict.items():
        if value in output_dict:
            output_dict[value] = (output_dict[value],) + (key,)
        else:
            output_dict[value] = key
    return output_dict


if __name__ == '__main__':
    dictionary = {'Ivanov': 97832, 'Petrov': 55521, 'Kuznecov': 97832}
    # dictionary = {'a': 1, 'b': 2, 'c': 2, 'd': (1, 2), 'e': (1, 2), 'f': 5}
    # dictionary = {'a': []}

    print(dictionary)
    print(reversed_dict(dictionary))
