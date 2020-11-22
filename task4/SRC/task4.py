import re
import sys


def compare(line1, line2):
    line2 = re.sub('[*]+', '.*', line2)
    if re.search(f'{line2}', line1) != None:
        if re.search(f'{line2}', line1).group(0) == line1:
            return print('OK')
        else:
            return print('KO')
    else:
        return print('KO')


def main():
    if len(sys.argv) > 3:
        print('Неверный набор входных данных.\n')
        print('Введите две строки.\n')
    else:
        a, b = str(sys.argv[1]), str(sys.argv[2])
        compare(a, b)


main()


