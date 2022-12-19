import sys
from collections import deque
#make sure the path. The path isn't start from this file's location. It's start from where you are.
sys.stdin = open('1. 재귀함수란(이진수출력)/in1.txt')

N = int(input())
res = deque()

'''
def decimalToBinary(x: int) :
    if x == 1 :
        return x % 2
    else :
        res.append(decimalToBinary(x // 2))
        return x % 2

#How can i change this line to append last number automatically?
res.append(decimalToBinary(N))
'''

#Answer of line 16. This way.
def decimalToBinary(x: int) :
    #When 'append' goes before calling itself, The result goes reversed.
    #res.append(x % 2)
    if x != 1 :
        decimalToBinary(x // 2)
    print(x % 2, end='')
    #res.append(x % 2)

    #if x == 0 :
    #    return
    #else :
    #    decimalToBinary(x // 2)
    #    res.append(x % 2)

decimalToBinary(N)

#print(''.join(list(map(str, res))))

for x in res :
    print(x, end = '')

