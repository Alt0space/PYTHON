import sys

def convert(number, base):
    num_dict = {10: 'a',
                11: 'b',
                12: 'c',
                13: 'd',
                14: 'e',
                15: 'f',
                16: 'g',
                17: 'h',
                18: 'i',
                19: 'j',
                20: 'k',
                21: 'l',
                22: 'm',
                23: 'n',
                24: 'o',
                25: 'p',
                26: 'q',
                27: 'r',
                28: 's',
                29: 't',
                30: 'u',
                31: 'v',
                32: 'w',
                33: 'x',
                34: 'y',
                35: 'z'}
    result = ''
    l = len(base)
    current = number
    while current != 0:
        remainder = current % l
        if 36 > remainder > 9:
            remainder_string = num_dict[remainder]
        elif remainder >= 36:
            remainder_string = '(' + str(remainder) + ')'
        else:
            remainder_string = str(remainder)
        result = remainder_string + result
        current = current // l
    return result


def main():

    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print('Неверный ввод данных.\n')
        print('В качестве первого аргумента следует указать десятичное число.\n')
        print('В качестве второго аргумента необходимо указать систему счисления, в которую необходимо перевести число.\n')
        print('Пример: python task1.py 10 01')
    elif any(c.isalpha() for c in sys.argv[1]):
        print('Неверный ввод данных.\n')
        print('В качестве первого аргумента следует указать десятичное число.\n')
        print('В качестве второго аргумента необходимо указать систему счисления, в которую необходимо перевести число.\n')
        print('Пример: python task1.py 10 01')
    else:
        n = int(sys.argv[1])
        b = str(sys.argv[2])
        print(convert(n, b))


main()

