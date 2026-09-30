""" Юркевич И.А. ЗКИ25-18Б. Вариант 26. """
import math
import sys


def main(args):
    """ Main Function """
    if len(args) < 2:
        print("Usage: python main.py [arguments]")
        return

    for arg in args[1:]:
        try:
            v26(float(arg))
        except ValueError:
            print(f"{arg} не является числом")

def v26(x):
    """ calculate and print 7x^5 - 2 * 2/sqrt(2x) """
    y = 7 * (x ** 5) - 2 * (2/(math.sqrt(2*x)))
    print(f"|x = {x}")
    print(f"|y = 7x\N{SUPERSCRIPT FIVE} - 2 * 2/\u221a(2x) = {y}\n")

if __name__ == "__main__":
    main(sys.argv)
