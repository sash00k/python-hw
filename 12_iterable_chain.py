# Написать функцию chain, которая бы принимала
# множество iterable, а возвращала новый iterable, который:
# 1. Сначала возвращает все элементы первого iterable по запросу
# 2. Затем переходит к следующему и так далее

def chain(*iterable_objects):
    for iterable_object in iterable_objects:
        for elem in iterable_object:
            yield elem

if __name__ == '__main__':
    print(list(chain([1, 2, 3], [4, 5])))
