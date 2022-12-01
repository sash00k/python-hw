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


# mixins solution
class SingletonClass:
    actual_instance = None

    def __new__(cls, *args, **kwargs):
        def __empty_init__(*a, **b):
            pass

        if cls.actual_instance is None:
            cls.actual_instance = super().__new__(cls)
        elif cls.__init__ is not __empty_init__:
            cls.__init__ = __empty_init__
        return cls.actual_instance


class Bar(SingletonClass):
    def __init__(self, value=1):
        self.value = value


if __name__ == '__main__':
    # decorator solution
    foo_1 = Foo(value=1)
    print(foo_1.value)     # 1
    foo_2 = Foo(value=2)
    print(foo_2.value)     # 1
    print(foo_1 is foo_2)  # True

    # class solution
    bar_1 = Bar(value=1)
    print(bar_1.value)     # 1
    bar_2 = Bar(value=2)
    print(bar_2.value)     # 1
    print(bar_1 is bar_2)  # True


