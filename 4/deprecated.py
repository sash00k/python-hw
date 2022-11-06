def deprecated(f=None, since=None, will_be_removed=None):

    import functools    

    if f is None:
        return functools.partial(deprecated, since=since, will_be_removed=will_be_removed)

    def inner(*args, **kwargs):
        warning = f'Warning: function {f.__name__} is deprecated'

        if since is not None:
            warning += f' since version {since}.'
        else:
            warning += f'.'

        if will_be_removed is not None:
            warning += f' It will be removed in version {will_be_removed}'
        else:
            warning += f' It will be removed in future versions'

        print(warning)

        return f(*args, **kwargs)

    return inner


@deprecated
def foo():
    print('since=None\nwill_be_removed=None\n')


@deprecated(since='1.13.1')
def bar():
    print('since=1.13.1\nwill_be_removed=None\n')


@deprecated(will_be_removed='2.1.0')
def pupa():
    print('since=None\nwill_be_removed=2.1.0\n')


@deprecated(since='1.13.1', will_be_removed='2.1.0')
def lupa():
    print('since=1.13.1\nwill_be_removed=2.1.0\n')


if __name__ == '__main__':
    foo()
    bar()
    pupa()
    lupa()
