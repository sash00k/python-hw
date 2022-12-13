# Написать декоратор @coroutine, который избавляет от необходимости
# сначала вызывать один раз next перед вызовами send.
import functools

def coroutine(f, *args, **kwargs):
    @functools.wraps(f)
    def wrapper():
        called_f = f(*args, **kwargs)
        next(called_f)
        return called_f
    return wrapper

@coroutine
def storage():
    values = set()
    was_there = False
    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


if __name__ == '__main__':
    st = storage()
    print(st.send(42)) # False
    print(st.send(42)) # True
    print(st.send(28)) # False