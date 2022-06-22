import sys
sys.stdin = open('input.txt')

n = int(input())
res = 0
for i in range(n) :
    tmp = input().split()
    #오 뭐야 정렬 왜하는데 그건 내껀뎅??
    tmp.sort()
    a, b, c = map(int, tmp)
    #조건의 순서에 대해서 주의해야한다.
    if a == b and b == c :
        money = 10000 + a * 1000
    #a == b or b == c 로 해도 되지만
    #그냥 가독성 좋으라고 한듯
    #그런데 조건이 이해가 안가는게
    #정렬을 했는데 a 와 c 가 같을수가 있나??
    #그런 경우는 숫자 3 개가 전부 같아야하는거아닌가??
    elif a == b or a == c :
        money = 1000 + a * 100
    #결국 a == b, a == c, b == c 이렇게
    #두개가 같을 경우 3 가지 다 체크해야한다.
    #위에서 2 가지를 먼저 체크한건 아래 조건일때는
    #a 가 b 나 c 와 다르기 때문이다.
    elif b == c :
        money = 1000 + b * 100
    else :
        money = c * 100
    if money > res :
        res = money
print(res)