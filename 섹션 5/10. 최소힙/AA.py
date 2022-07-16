import sys
import heapq

#sys.stdin = open('in1.txt')

test = []

x = 0

while x != -1 :
    x = int(input())
    if x == 0 :
        if test :
            print(heapq.heappop(test))
        else :
            print(-1)
    else :
        heapq.heappush(test, x)
        