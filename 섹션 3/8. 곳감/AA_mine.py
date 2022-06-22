import sys
#sys.stdin = open('input.txt')

N = int(input())
#이제부터 Arr 이 아닌 List 로 명명규칙을 변경한다.
#파이선에 Array 가 있는지 없는지는 모르겠지만
#그래도 엄연히 Array 가 아닌 List 이기 때문이다.
#맞나?? ㅋㅋ
#마찬가지로 num 이 아닌 int 로 명명규칙을 변경한다.
gridIntList = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
gridRotateList = [list(map(int, input().split())) for _ in range(M)]

for i in range(M) :
    rotateTrg = gridRotateList[i][0] - 1
    rotateDrct = gridRotateList[i][1]
    rotateCnt = gridRotateList[i][2]
    for _ in range(rotateCnt) :
        if rotateDrct == 0 :
            gridIntList[rotateTrg].append(gridIntList[rotateTrg].pop(0))
        else :
            gridIntList[rotateTrg].insert(0, gridIntList[rotateTrg].pop())
step = 1
tot = 0
i = 0
#초기값을 뭘로 두냐에 따라서
#gridIntList[k][i: j + 1] 이냐
#gridIntList[k][i: j] 이냐로 갈림
#초기값이 N - 1 이면 위에꺼
#초기값이 N 이면 밑에꺼
j = N - 1
for k in range(N) :
    tot += sum(gridIntList[k][i: j + 1])
    i += step
    j -= step
    #중간 지점일때 step 을 변경
    #하지만 사실 이 코드는 슬라이스를 했기 때문에 사용하는 코드
    #만약 센세처럼 for 문으로 슬라이스를 대체한다면??
    #그래도 안돼.
    #왜냐하면 range 자체가 틀어져버려.
    #그래서 for 문을 안돌거야.
    if i == j :
        step = -1
print(tot)