# Реализовать функциональность для объявления классов синглтонов.
# Singleton (одиночка) - паттерн проектирования, который позволяет создать только один экземпляр класса.
# При попытке создать еще один экземпляр, вы просто получаете уже созданный ранее экземпляр.
import functools


class Sample:
    # does_instance_exist = False
    actual_instance = None

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.actual_instance = instance
        return instance

    def __init__(self, value: int = 1):
        self.value = value

# def singleton(cls):
#
#     @functools.wraps
#     def init(self):
#         if cls.does_instance_exist
#         old_init = cls.__init__
#
#     cls.__init__ = init
#     return cls


if __name__ == '__main__':
    sample1 = Sample(value=1)
    print(id(sample1.actual_instance))
    sample2 = Sample(value=2)
    print(id(sample2.actual_instance))
    # print(sample1.actual_instance)
    # print(Sample.actual_instance)
