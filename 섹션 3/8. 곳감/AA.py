import sys
sys.stdin = open('input.txt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m) :
    h, t, k = map(int, input().split())
    if t == 0 :
        for _ in range(k) :
            a[h - 1].append(a[h - 1].pop(0))
    else :
        for _ in range(k) :
            a[h - 1].insert(0, a[h - 1].pop())
res = 0
#시작포인터
s = 0
#끝포인터
e = n - 1
for i in range(n) :
    for j in range(s, e + 1) :
        res += a[i][j]
    #중간지점에 도달하기 전 포인터 컨트롤
    if i < n // 2 :
        s += 1
        e -= 1
    #중간지점서부터 포인터 컨트롤
    else :
        s -= 1
        e += 1
print(res)

#으으 지금 시각 새벽 2 시
#정리는 내일 할래용.

#포인터 컨트롤하는 부분에대해서는 어느 정도 숙지를 하고 지나가자.
#내가 하는 step 을 이용한 포인터 컨트롤 방법도 당연히 훌륭하지만
#센세가 사용하는 지점을 잡아서 포인터를 컨트롤 하는 방식도 알고 있어야한다.