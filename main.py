import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser("This is an argparse program.")
    """
    必传参数.
    """
    parser.add_argument("count", action="store", type=int)
    parser.add_argument("units", action="store")
    """
    可选参数.
    """
    parser.add_argument("-a",
                        action="store",
                        dest="a",
                        default="10000",
                        help='this is -a help message.')
    parser.add_argument("-b",
                        action="store_true",
                        dest="b",
                        default=False,
                        help='this is a boolean.')
    parser.add_argument("-c",
                        action="store",
                        dest="c",
                        type=int,
                        help='this is a int')
    #可以使用 -a=value来指定参数
    #可以使用 -cvalue来指定参数
    #args = parser.parse_args(['1000', 'test', '-a=20000', '-b', '-c3'])
    #pipenv run python main.py 1000 ABC -a=3000 -b -c10
    args = parser.parse_args(sys.argv[1:])
    print(args.count)
    print(args.units)
    print(args.a)
    print(args.b)
    print(args.c)
