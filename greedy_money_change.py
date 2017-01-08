# Uses python3
import sys

def get_change(m):
    n = 0
    if m - 10 >= 0:
        n = n + 1 + get_change(m - 10)
    elif m - 5 >= 0:
        print ' its 5'
        n = n + 1 + get_change( m -5 )
    else:
        print 'its' , m
        n = m + n
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
