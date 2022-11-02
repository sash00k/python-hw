def format_table(benchmarks, algos, results):
    max_bench_length = max(map(len, benchmarks + ['Benchmark']))
    max_algos_lengths = [max(map(len, list(map(str, (results[j][i] for j in range(len(benchmarks)))))+[algos[i]]))
                         for i in range(len(algos))]

    # вот этого костыля, конечно, хотелось бы избежать
    benchmark = 'Benchmark'

    print(f'| {benchmark:<{max_bench_length}} |', end='')
    for i in range(len(algos)):
        print(f' {algos[i]:<{max_algos_lengths[i]}} |', end='')
    print()

    print('|' + '-' * (max_bench_length + sum(max_algos_lengths) + 3 * (len(algos) + 1) - 1) + '|')

    for i in range(len(benchmarks)):
        print(f'| {benchmarks[i]:<{max_bench_length}} |', end='')
        for j in range(len(algos)):
            print(f' {results[i][j]:<{max_algos_lengths[j]}} |', end='')
        print()


if __name__ == '__main__':

    format_table(['best case', 'worst case'],
                 ['quick sort', 'merge sort', 'bubble sort'],
                 [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])

    # | Benchmark  | quick sort | merge sort | bubble sort |
    # |----------------------------------------------------|
    # | best case  | 1.23       | 1.56       | 2.0         |
    # | worst case | 3.3        | 2.9        | 3.9         |

    print()

    format_table(['best case', 'the worst case'],
                 ['quick sort', 'merge sort', 'bubble sort'], [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])

    # | Benchmark      | quick sort | merge sort | bubble sort |
    # |--------------------------------------------------------|
    # | best case      | 1.23       | 1.56       | 2.0         |
    # | the worst case | 3.3        | 2.9        | 3.9         |
