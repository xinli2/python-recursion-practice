"""
    File: annoying_recursion.py
    Author: Xin Li
    Purpose: In this project i will write several recursive function.

"""
def annoying_factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n == 4:
        return 4 * annoying_factorial(3)
    if n == 5:
        return 5 * annoying_factorial(4)
    if n == 6:
        return 6 * annoying_factorial(5)
    else:
        return n*annoying_factorial(n-1)

def annoying_fibonacci(n):
    if n ==1:
        return 1
    if n ==0:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return annoying_fibonacci(3)+ annoying_fibonacci(2)
    if n == 5:
        return annoying_fibonacci(4)+ annoying_fibonacci(3)
    if n == 6:
        return annoying_fibonacci(5)+ annoying_fibonacci(4)
    return annoying_fibonacci(n-1)+annoying_fibonacci(n-2)

def annoying_valley(n):
    #TODO: draw the down part!
    if n == 0:
        return
    if n == 1:
        print('*')
        return
    if n == 2:
        print('./')
        print('*')
        print('.\\')
        return
    if n == 3:
        print('../')
        print('./')
        print('*')
        print('.\\')
        print('..\\')
        return
    if n == 4:
        print('.'*3,'/',sep='')
        annoying_valley(3)
        print('.'*3,'\\',sep='')
        return
    if n == 5:
        print('.'*4,'/',sep='')
        annoying_valley(4)
        print('.'*4,'\\',sep='')
        return
    if n == 6:
        print('.'*5,'/',sep='')
        annoying_valley(5)
        print('.'*5,'\\',sep='')
        return
    else:
        print('.'*(n-1),'/',sep='')
        annoying_valley(n-1)
        print('.'*(n-1),'\\',sep='')
        return

def annoying_int_sequence(n):
    s = []
    if n ==0:
        return []
    if n ==1:
        return [1]
    if n == 2:
        return [1,2,1]
    if n == 3:
        return [1,2,1,3,1,2,1,3,1,2,1]
    if n == 4:
        s+=annoying_int_sequence(3)
        s+=[4]
        s = s * (3)
        s+=annoying_int_sequence(3)
        return s
    if n == 5:
        s+=annoying_int_sequence(4)
        s+=[5]
        s = s * (4)
        s+=annoying_int_sequence(4)
        return s
    if n == 6:
        s+=annoying_int_sequence(5)
        s+=[6]
        s = s * (5)
        s+=annoying_int_sequence(5)
        return s
    s+=annoying_int_sequence(n-1)
    s+=[n]
    s = s * (n-1)
    s+=annoying_int_sequence(n-1)

    return s
