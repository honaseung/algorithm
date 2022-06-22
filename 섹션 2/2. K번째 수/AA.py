import sys
#sys.stdin = open("input.txt")

T = int(input())

for i in range(T) :
    N, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s - 1 : e]
    a.sort()
    #파이썬에서 프린트 출력 포멧 기억하기
    print("#%d %d" %(i + 1, a[k - 1]))