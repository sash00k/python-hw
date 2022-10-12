# Реализовать функцию specialize, которая принимает
# функцию f и набор значений, а возвращает частично
# примененную к этим значениям функцию f.
#
# Пример:
# def sum(x, y):
#   return x + y
#
# plus_one = specialize(sum, y=1)
# print(pluse_one(10)) # 11
#
# just_two = specialize(sum, 1, 1)
# print(just_two()) # 2

def summa(x, y):
    return x + y


def specialize(func, *args, **kwargs):
    def helper(*_args, **_kwargs):
        return func(*args, *_args, **kwargs, **_kwargs)
    return helper


if __name__ == '__main__':

    plus_one = specialize(summa, y=1)
    print(plus_one(10))

    just_two = specialize(summa, 1, y=2)
    print(just_two())
