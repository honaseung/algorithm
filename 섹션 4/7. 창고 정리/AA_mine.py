import sys
#sys.stdin = open('input.txt')

#이 문제는 왜 그리디일까??
#항상 이런 질문에서부터 문제를 시작해보자.
#가장 높은곳에서 가장 낮은곳으로...
#비교를 하는구나??
#그렇다면 그리디이다.
#음... 문제를 더 많이 풀다보면 아무래도
#더 많은 근거들이 있겠지만
#지금은 이정도를 근거로 가지고 가자.

L = int(input())
storage = list(map(int, input().split()))
M = int(input())
#오름차순 정렬
storage.sort()

for i in range(M) :
    storage[0] = storage[0] + 1
    storage[L - 1] = storage[L - 1] - 1
    storage.sort()
print(storage[L - 1] - storage[0])

#으잉??
#너무 쉬운데 이번건??
#사실 이전 문제도 쉽긴했어.
#다만 다중 for 문을 사용하지 않고 풀려고하니
#어려웠을뿐이지.
#이번 문제도 뭐가 있으려나??

#아무것도 없었다. ㅋㅋ
#걍 끝이네??
#다만 +=, -= 가
#리스트의 요소 각각에도 적용가능하다는 사실만 알아두자.