def flatten(lst: list, depth: int = -1) -> list:
    was_smth_unpacked = False

    lst_unpacked = []
    for elem in lst:
        if isinstance(elem, list):
            was_smth_unpacked = True
            lst_unpacked.extend(elem)
        else:
            lst_unpacked.append(elem)

    depth -= 1
    if depth == 0 or not was_smth_unpacked:
        return lst_unpacked

    return flatten(lst_unpacked, depth)


if __name__ == '__main__':
    arr = [1, 2, [3, [4]], 5]
    print(flatten(arr))
    print(flatten(arr, depth=1))
    print(flatten(arr, depth=2))
