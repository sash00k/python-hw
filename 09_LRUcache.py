# Реализовать класс, представляющий собой кэш на заданное в конструкторе
# количество элементов. В любой момент времени в нем хранится не более, чем
# capacity элементов. Метод get возвращает по заданному ключу значение, если
# такая пара есть в кэше, None в противном случае.
#
# Если в данный момент в кэше хранится меньше, чем capacity элементов, то функция put
# добавит новую пару. В противном случае она также удалит ту пару элементов, от
# чьего ключа дольше всех не вызывали метод get

class LRUCache:
    def __init__(self, capacity=16):
        self._dict = dict()
        self._capacity = capacity
        self._usage_history = [] # keys sorted by time of last use (the last used at index 0)

    def put(self, key, value):

        if key in self._dict.keys():
            self._usage_history.remove(key)
            self._usage_history.insert(0, key)
        else:
            if len(self._dict) == self._capacity:
                rare_used_key = self._usage_history.pop()
                self._dict.pop(rare_used_key)
            self._usage_history.append(key)  # get() has never been called from this key, so it's the longest time

        self._dict[key] = value




    def get(self, key):
        if key in self._dict.keys():
            self._usage_history.remove(key)
            self._usage_history.insert(0, key)
            result = self._dict[key]
        else:
            result = None
        return result

    def __str__(self):
        return 'Cache:' + str(self._dict) + '\nHistory (long used on the right): ' + str(self._usage_history)


if __name__ == '__main__':
    cache = LRUCache(capacity=3)

    cache.put('a', 1)
    cache.put('b', 1)
    cache.put('c', 1)

    print(cache)
    # Cache:{'a': 1, 'b': 2, 'c': 3}
    # History (long used on the right): ['a', 'b', 'c']

    cache.put('d', 1)
    print(cache)
    # Cache:{'a': 1, 'b': 1, 'd': 1}
    # History (long used on the right): ['a', 'b', 'd']

    cache.put('d', -1)
    print(cache)
    # Cache:{'a': 1, 'b': 1, 'd': -1}
    # History (long used on the right): ['d', 'a', 'b']

    cache.get('d')
    print(cache)
    # Cache:{'a': 1, 'b': 1, 'd': -1}
    # History (long used on the right): ['d', 'a', 'b']
