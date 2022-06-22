import sys
sys.stdin = open('input.txt')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n // 2
#코드의 순서가 매우 중요하다는건
#뭐 잘알테지만 그래도 한번 더 강조하자.
#합을 미리 구하고 포인터를 이동했기 때문에
#초기값 세팅이 위와 같아진다.
for i in range(n) :
    #각 행의 합을 구하기 위한 코드
    #슬라이스를 이용하지 않았기에
    #합의 시작점과 끝점을 range 로 잡아준다.
    for j in range(s, e + 1) : 
        res += a[i][j]
    #다이아몬드 꼭지점이 아니라
    #i(행) 가(이) 중간 지점에 도달하기 전까지
    if i < n //2 :
        s -= 1
        e += 1
    #i(행) 가(이) 중간 지점에 도달했을때부터
    else :
        s += 1
        e -= 1
print(res)