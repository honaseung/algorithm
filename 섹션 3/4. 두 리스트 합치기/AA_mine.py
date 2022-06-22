import sys
#sys.stdin = open('in1.txt')

#파이선 join 에는 sep 같은게 없네

#명심하자 아무리 같은 숫자라도
#str 을 정렬할때와 int 를 정렬할때는 정렬이 달라진다는걸!!

N = int(input())
numArrN = list(map(int, input().split()))

M = int(input())
numArrM = list(map(int, input().split()))

'''
numArrN.extend(numArrM)
numArrN.sort()

for x in numArrN :
    print(x, end = " ")
'''

#??????
#진심이에요??
#아니 전 문제는 어려운거 주더니
#이거...뭐야??
#주석 뭐라고해야해??
#심지어 N, M 은 쓰지도 않았어.

#ㅋㅋㅋㅋ 이거 하라는게 아니었어 역시
#다시 해보자

res = []
#i 안쓸거야
#응 써야돼 ~~
#for i in range(N + M) :
    #or 연산자 연습용
    #if i == N - 1 or i == M - 1 :
    #    if i == N - 1 :
    #        res.extend(numArrN)
    #    else :
    #        res.extend(numArrM)
    #    break
    #else :
    #    res.append(min(numArrN.pop(0), numArrM.pop(0)))

    #파이선은 삼항 연산자를 지원하지 않는다.
    #len(numArrN) > 0 ? numN = numArrN.pop(0) : 0

    #아래 형태의 삼항 연산자만 지원한다.
    #numN = numArrN.pop(0) if len(numArrN) > 0 else float('inf')
    #numM = numArrM.pop(0) if len(numArrM) > 0 else float('inf')
    
    #아 둘 다 뽑았는데 하나만 넣었으니 하나는 들고 있거나 따로 넣어야하는데 하나만 넣고 하나는 버렸구나
    #res.append(min(numN, numM))
    #그래서 추가했지렁 ~~
    #근데 일케하면 inf 가 들어가버림 ㅋㅋ
    #지금 또 너무 복잡하게 생각하는중 ㅋㅋ
    #쉬었다가 다시 가자.
    #지금 너무 빡공했어 벌써 6 문제 째야.
    #이따가 처음부터 다시하는게 좋을거같어.
    #res.append(max(numN, numM))
#for x in res :
    #print(x, end = " ")

#pop 에 목메이지말자
#pop 을 없애고 포이터를 두 개 두어서 오리지날 리스트를 훼손하지않는 방향으로 진행해보자.
res = []
#역시 idx 두 개를 동시에 쓸 쑨 없나보군.
#for i, j in range(N + M) :
#초기화할때는 각각 넣어줘야해.
i, j = 0, 0
#간과한것 한가지
#N + M 보다 작은 동안이 아니다.
#N 과 M 은 리스트의 길이이기 때문에
#둘 중에 더 긴 리스트 만큼만 돌면 된다.
#두 개를 합친 만큼 돌면 오히려 안됀다.
#이 생각도 잘못되었다. 둘 중에 더 긴 리스트 만큼이 아니다!!
#지금 보면 각각의 리스트에 접근하는 idx 가 너무 명확하다!!
#그러니 각각의 idx 에 해당하는 리스트 길이와 비교해주자!!
#추가로 접근하려는 것은 idx 이기 때문에 - 1 해준 값으로 조건을 걸어주거나
#접근시에 - 1 을 해줘야 한다.
#여기서는 접근이 많기 때문에 조건에서 - 1 을 해주었다.
#이 녀석은 or 이라 앞조건이 False 인데도 뒤가 True 라서 그냥 타고 들어가서
#idx 를 또 올려버린다.
#while i < max(N, M) - 1 or j < max(N, M) - 1 :
#while i < N - 1 or j < M - 1:
#    val = min(numArrN[i], numArrM[j])
#    if val == numArrN[i] and i < N - 1: i += 1
#    #간과한것 두가지
#    #if 그리고 if 문을 쓴다면 당연하게도 두개 동시에 탈 수 있다.
#    #그래서 if 와 elif 를 사용한다.
#    #if 와 elif 를 사용하는 기준은 이 문제에서는 굳이 고려하지 않아도 된다.
#    #만약 문제에서 두 값이 동일하다면 N 리스트의 값만 넣어 달라거나 하지 않는이상
#    #신경쓰지 않아도 된다.
#    elif val == numArrM[j] and j < M - 1: j += 1
#    res.append(val)
#for x in res :
#    print(x, end = " ")

#아오 진짜 한끝차이인데 아숩다.
#정답 공개!!

#나의 문제점은
#기존의 함수에 너무 의존하려고 하거나 혹은
#너무 지나치게 깊이 생각한다는것
#때로는 그저 그냥 단순한 코드가 더 좋다.(심플이 아닌 허접?? 한 코드)
while True :
    if numArrN[i] < numArrM[j] :
        res.append(numArrN[i])
        i += 1
    else :
        res.append(numArrM[j])
        j += 1
    if i == N :
        #리스트 슬라이스
        #리스트[시작idx: 끝idx: 스텝]

        #이번에야말로 extend 니??
        res.extend(numArrM[j:])
        break
    if j == M :
        res.extend(numArrN[i:])
        break
for x in res :
    print(x, end = " ")

#두개의 포인터를 사용한다는 발상 자체는 너무 훌륭했다.
#그러나 조건에 대한 기준을 세우는데에는 많이 부족했다.
#또한 슬라이스 기능에 대해서도 부족했다.
#그리고 리스트는 extend 함수가 아니더라도 + 연산자로 합칠 수 있다.