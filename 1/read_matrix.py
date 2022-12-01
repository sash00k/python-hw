# Пусть входные данные имеют вид:
#
# a_00 a_01 a_02 … | a_10 a_11 a_12 … | … | a_n0 a_n1 … |
#
# И описывают матрицу из значений типа float. Символ |
# отделяет описание элементов очередной строки матрицы
#
# По этим данным необходимо создать список из списков
# значений типа float, соответствующий этой матрице
#
# Пример: "1 2 | 3 4" -> получаем список a ->
# print(a[0][1]) выведет 2

def read_matrix(input_str: str) -> list:
    matrix = []
    for string in input_str.split('|'):
        matrix.append(list(map(float, string.split())))

    return matrix


if __name__ == '__main__':
    a = read_matrix('1 2 | 3 4')
    print(a)
    print(a[0][1])
