import sys
#sys.stdin = open('input.txt')

L = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
for _ in range(m) :
    #a[0] = a[0] + 1 이 보다
    #코드를 더 쉽게 정리
    a[0] += 1
    a[L - 1] -= 1
    #작업후에는 정렬이 변경될 수 있기 때문에
    #매번 재정렬
    #이번 문제에서는 항상 제일 큰 높은곳에서
    #제일 낮은 곳으로 가야하기에 있는 코드
    a.sort()
print(a[L - 1] - a[0])