import sys
import heapq

#sys.stdin = open('input.txt')

test = []
x = 0

while x != -1 :
    x = int(input())
    if x == 0 :
        if test :
            #You should remind that you 'pushed' value as multiply -1
            print(-(heapq.heappop(test)))
        else :
            print(-1)
    else :
        #If you 'push' value as multiply -1, Max value goes min and min value goes max.
        #Metion it on HEAD RULES.
        heapq.heappush(test, -x)
