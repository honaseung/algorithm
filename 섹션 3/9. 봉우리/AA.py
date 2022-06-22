import sys
#뭐야 자동완성 되자너 ㅋㅋ
#이제껏 굳이 손수 import 해왔네.
#여러분 ~~ 여기 수제로 만들어진 input.txt 랑
#그걸 또 수제로 import 한 맛있는 input 이 있어용
#sys.stdin = open('input.txt')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * n)
a.append([0] * n)
#커버를 만드는중
#나는 뚜껑이랑 밑바닥을 포장다하고 붙였는데
#센세는 붙이고 포장했네
for x in a :
    x.insert(0, 0)
    x.append(0)

#포장끝 풀이시작
#상하좌우에 접근하기 위한 step?? flag?? 리스트
#중요한 방식!!
#일종의 포인터 컨트롤 방식이다.
#['좌', '-', '우', '-']
dx = [-1, 0, 1, 0]
#['-', '하', '-', '상']
dy = [0, 1, 0, -1]
cnt = 0
for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        #ㅋㅋ all 까먹었었지??
        #이 참에 다시 외워두자.
        #all 이랑 any!!
        #아래 코드와 step 리스트를 이용하여
        #상하좌우 전부 컨트롤하기!!
        #for k in range(len(dx)) -> for k in range(4)
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)) :
            cnt += 1
print(cnt)

#dx, dy 방식 외워두자!!
#내 방식도 엄청 훌륭하지만
#포인터 컨트롤은 굉장히 중요한 스킬인거같아!!
#그러니 익숙해지자!!