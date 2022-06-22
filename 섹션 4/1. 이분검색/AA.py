import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n - 1
#lt 가 rt 보다 크거나
#rt 가 lt 보다 작으면
#탐색이 끝났음을 의미한다.
#두 값이 같을때도 동일하다.
while lt <= rt :
    #나는 각 조건안에서 mid 를 바꾸어주었는데
    #센세 방식으로는 매번 일단 바꿔주고 비교한다.
    #공통된 코드를 빼서 끌어올린것 뿐이지만
    #내가 실전에서 좋아하는 방식이기도하지.
    mid = (lt + rt) // 2
    if a[mid] == m :
        print(mid + 1)
        break
    elif a[mid] > m :
        rt = mid - 1
    else :
        lt = mid + 1