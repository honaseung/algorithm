import sys
#sys.stdin = open('input.txt')

N = int(input())
#바로 연습해버리기!!
gridArr = [list(map(int, input().split())) for _ in range(N)]

#이번에는 순순하게 범용성 제로의 알고리즘용 코드를 짜보자.
#포인터도 활용해보자!!

#바로 연습해버리기2!!
i = j = N // 2
#0 으로 초기화 시키는거 참 좋아하는거 잘 알아.
#근데 0 이 능사는 아니야.
#오히려 독이 되는 경우가 더 많은거같아. 지금보면.
#너가 말했듯이 초기값이 중요하다며
#자꾸 0 으로 하려고 하지마.
#그리고 변수가 하는 역할에 대해서도
#다시 한번 잘 생각해
#여기서 flag 는 idx 가 변화하는 폭이라고 보면돼.
#문제를 잘 보면 idx 는 유동적으로 변화하고 있고
#그 폭은 1 이야.
#그래서 변수명도 이거 쓰고서 바꿀거야.
#flag -> step
step = 1
diamondSum = 0
#j < N 도 가능하다.
#i < N 이라면 위에서 아래로 또는 아래에서 위로
#행 기준이 된다.
#j < N 이라면 왼쪽에서 오른쪽으로 또는 오른쪽에서 왼쪽으로
#열 기준이 된다.
for k in range(N) :
    #슬라이스 연습
    #슬라이스에서 끝 인덱스는
    #포함되어서 슬라이스 되지 않는다.
    #내장 함수 사용!!
    #diamondSum += sum(gridArr[k][i: j + 1])
    #내장 함수 안사용!!
    for x in gridArr[k][i: j + 1]: diamondSum += x 
    if i == 0 :
        step = -1
    i = i - step
    j = j + step 
print(diamondSum)