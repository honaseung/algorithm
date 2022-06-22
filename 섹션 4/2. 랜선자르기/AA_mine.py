import sys
#sys.stdin = open('input.txt')

K, N = map(int, input().split())
#이거 input 받을때 조심해.
#아까 어떤 미친놈이 모든 값을 map 으로 받는걸 for 문 돌린담에
#리스트 담아서 분위기 싸해졌었어.
#증거가 안남았는데 암튼 미친놈이었어.
lanLenList = list(int(input()) for _ in range(K))

#시작값이 1 인 이유는
#만들 수 있는 랜선의 최소 길이는 1 이기 때문이다.
#또한 마지막값이 주어진 랜선들중 가장 큰 값인 이유는
#만들 수 있는 랜선의 최대 길이는 주어진 랜선들중 가장 큰 값이기 때문이다.
#그리고 이 값들은 idx 가 아니라 자연수이라는 점에 주의하자.
s, e, m = 1, max(lanLenList), 0
#딕셔너리로 만드는데에는 다아아아아 이유가 있지.
#문제에서 주어진대로 정확히 N 개의 랜선이 만들어지는 경우와
#N 개보다 많은 랜선이 만들어지는 경우 둘 다 정답이 될 수 있다.
#그러기에 우리가 해야할 것은 몇개의 랜선이 만들어졌는가
#그리고 그렇게 만들어진 랜선은 길이가 얼마나 되는가이다.
#그렇기에 두가지 정보를 이어서 저장하고 있어야한다.
#따라서 리스트가 아닌 딕셔너리를 사용하였다.
availableCm = {}
while s <= e :
    #idx 가 아닌 자연수의 중간값이기에 이렇게 표현된다.
    #모르겠으면 간단하게 1 부터 10 까지
    #그리고 다시 1 부터 9 까지 해보면 된다.
    #m 은 mid 라는 의미에서 m 썼다.
    m = (s + e) // 2
    cnt = 0
    for i in range(K) :
        cnt += lanLenList[i] // m
    if cnt > N :
        #파이선에서는 자바스크립트처럼
        #.key 로 접근이 안됀다.
        #반드시 [key] 로 접근 바란당.
        #availableCm.cnt = m
        availableCm[cnt] = m
        s = m + 1
    elif cnt < N :
        e = m - 1
    else :
        #바로 결과값을 출력하지않는 이유는
        #문제에서 주어진대로 11 개로 자를 수 있는 길이가
        #여러개일 수도 있다. 이런 경우 그 중 가장 큰 길이가
        #정답이 되기 때문이다.
        availableCm[cnt] = m
        s = m + 1
#분명 lambda 를 사용한다면
#이보다 좋은 풀이가 있을지도 모른다.
#하지만 지금은 모르니 그냥 이대로 해두었다.
#어쩌면 이게 최선일지도 모르지만...
maxCnt = float('inf')
for k in availableCm.keys() :
    maxCnt = min(k, maxCnt)
print(availableCm.get(maxCnt))
