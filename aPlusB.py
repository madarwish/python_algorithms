# Uses python2
# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt
# edited by mdarwish
import sys

def main():
    input = sys.stdin.read()
    tokens = input.split()
    a = int(tokens[0])
    b = int(tokens[1])
    print(a + b)

if __name__ == '__main__':
    main()
