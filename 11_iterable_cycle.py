# my implementation of itertools.cycle()
def cycle(iterable_object):
    while True:
        yield from iterable_object


if __name__ == '__main__':
    counter = 0
    for elem in cycle([1, 2, 3]):
        if counter == 10:
            break
        print(elem, end=' ')  # 1 2 3 1 2 3 1 2 3 1
        counter += 1
