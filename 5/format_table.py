def format_table(benchmarks, algos, results):
    table = []
    for i in range(len(benchmarks)+1):
        if i == 0:
            table.append(['Benchmark'] + algos)
        else:
            table.append([benchmarks[i-1]] + results[i-1])

    max_lengths = [max(map(len, list(map(str, [table[i][j] for i in range(len(table))])))) for j in range(len(algos)+1)]

    for i in range(len(table)):
        print('|', end='')
        for j in range(len(table[0])):
            print(f' {table[i][j]:<{max_lengths[j]}} |', end='')

        if i == 0:
            print('\n|' + '-' * (sum(max_lengths) + 3 * (len(table[0])) - 1) + '|')
        else:
            print()


if __name__ == '__main__':

    format_table(['best case', 'worst case'],
                 ['quick sort', 'merge sort', 'bubble sort'],
                 [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])

    # | Benchmark  | quick sort | merge sort | bubble sort |
    # |----------------------------------------------------|
    # | best case  | 1.23       | 1.56       | 2.0         |
    # | worst case | 3.3        | 2.9        | 3.9         |

    format_table(['best case', 'the worst case'],
                 ['quick sort', 'merge sort', 'bubble sort'], [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])

    # | Benchmark      | quick sort | merge sort | bubble sort |
    # |--------------------------------------------------------|
    # | best case      | 1.23       | 1.56       | 2.0         |
    # | the worst case | 3.3        | 2.9        | 3.9         |
