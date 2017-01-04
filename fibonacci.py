import sys

# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
   
    return calc_fib(n - 1) + calc_fib(n - 2)
    
#n = int(input())
#print(calc_fib(n))

def fasterAlg(n  ):
    series = [1 , 1] 
    length = len(series)
 
    for i in range(length   , n + 1):
        series.append( series[i-1] + series[i-2])
    return series[n-1]
    

def main():
    count = 0
    if len(sys.argv) > 1: 
	count =  sys.argv[1]
    else: 
	count = input('Enter Fib. series count: ')

    print fasterAlg(int(count))
    print calc_fib(int(count))
    return 


if __name__ == '__main__':
    main()
