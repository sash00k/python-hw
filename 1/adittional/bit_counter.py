# Написать программу, считающую количество
# выставленных битов в произвольном целом числе.
#
# Использовать приведение к строке и bin нельзя.
#
# Замечание: программа должна корректно работать с
# отрицательными числами, с учетом представления в
# дополнительном коде. signed бит считать один раз.
#
# Пример: 10 -> 2 (т.к. 10 - это 0…1010)
# -123 -> 3 (т.к. -123 - это 1…0000101)

def count_slow(num: int) -> int:
    counter = 0

    if num < 0:
        counter += 1
        num = -num

        i = 0 # тут я рассчитываю на то, что правильно понял смысл инвертирования бит в двоичном представлении
        while True:
            if 2**i >= num:
                num = 2**i - num
                break
            i += 1

    while num > 0:
        if num % 2 == 1:
            counter += 1
        num //= 2

    return counter


def count_low(num: int) -> int:
    pass


def limited_bin(x):
  print(bin(x & 0xffffffff))


if __name__ == '__main__':
    for number in (1, 3, 10, -123, -9, -7, -128, -16):
        print(number, '->', count_slow(number))
