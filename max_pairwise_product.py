# Uses python2
import datetime
import random
import time


def limitedSoln(lst):
   result = 0
   arayLength = len(lst)
   for i in range(0, arayLength):
       for j in range(i+1, arayLength):
           if lst[i]*lst[j] > result:
               result = lst[i]*lst[j]
   return result



def betterSoln(lis):
    biggest = 0
    big = 0
    for  n in lis:
        if n > biggest:
            big = biggest
            biggest = n
        elif n > big:
            big = n
    return biggest * big


def main():
    a = []
    mode = int(input('Choose running mode: Stress(1) , Test(2) '))
    if mode == 1:
        n = int(input('Insert the count of items in the list '))
        for i in range (0, n):
            a.append(random.randrange(1,10000))
    elif mode == 2:
        a = [int(x) for x in raw_input('Give me the list').split()]
    else:
        print 'Wrong input'
        return
    # Run first soln
    startDate =  time.time() #datetime.datetime.now()
    limitedSoln(a)
    firstSolTime = time.time() - startDate # datetime.datetime.now() - startDate
    print  firstSolTime

    # run second solution
    startDate = time.time() #datetime.datetime.now()
    betterSoln(a)
    secondSolTime = time.time() - startDate
    print secondSolTime #datetime.datetime.now() - startDate

    if secondSolTime != 0.0:
        print 'the first soln taskes as %f as the second soln' % (firstSolTime/secondSolTime)
if __name__ == '__main__':
    main()





