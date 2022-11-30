# Реализовать функциональность для объявления классов синглтонов.
# Singleton (одиночка) - паттерн проектирования, который позволяет создать только один экземпляр класса.
# При попытке создать еще один экземпляр, вы просто получаете уже созданный ранее экземпляр.

# decorator solution
def singleton_decorator(cls):
    instances = dict()

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton_decorator
class Foo:
    def __init__(self, value=1):
        self.value = value


# class solution
class SingletonClass:
    actual_instance = None

    def __new__(cls, *args, **kwargs):
        if cls.actual_instance is None:
            cls.actual_instance = object.__new__(cls)
        return cls.actual_instance


class Bar(SingletonClass):
    def __init__(self, value=1):
        self.value = value


if __name__ == '__main__':
    foo_1 = Foo(value=1)
    print(id(foo_1), foo_1.value)  # 139725593185344 1
    foo_2 = Foo(value=2)
    print(id(foo_2), foo_2.value)  # 139725593185344 1

    bar_1 = Bar(value=1)
    print(id(bar_1), bar_1.value)  # 139879821684848 1
    bar_2 = Bar(value=2)
    print(id(bar_2), bar_2.value)  # 139879821684848 2


