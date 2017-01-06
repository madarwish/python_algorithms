# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_better(a,b):
    temp = b
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def lcm ( a , b ):
    return a * b / gcd_better(a , b)

if __name__ == "__main__":
    #a , b = 10 , 6
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_better(a, b))
    print ( lcm ( a , b))
