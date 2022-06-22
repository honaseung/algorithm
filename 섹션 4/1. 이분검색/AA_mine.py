import sys
sys.stdin = open('in3.txt')

N, M = map(int, input().split())
sortedIntList = sorted(list(map(int, input().split())))

#i 의 초기값을 잘못 잡았었다.
#언제나 작은 값으로 먼저 시도해보고 큰 값으로도 해보길 바란다.
#idx 는 항상 0 부터 시작이고
#N 개의 숫자가 들어오면
#idx 최대값은 N - 1 이다.
#어려운거 같으면 중간 idx 값을 구하는 방법은
#(idx 최소값 + idx 최대값) // 2 라는 점을 기억하자
#중요한건 idx 의 최소값과 최대값이라는거다!!
#s, e, i = 0, N - 1, N // 2
s, e, i = 0, N - 1, (N - 1) // 2
while True :
    if sortedIntList[i] > M :
        e = i - 1
        #라인 7 에서 말했다시피
        #idx 중간값은
        #(idx 최소값 + idx 최대값) // 2 이다.
        #굳이 - 1 을 해줄 필요가 없다.
        #이미 윗 라인에서 최소값 또는 최대값을 맞추어 주었기때문이다.
        #i = (s + e - 1) // 2
        i = (s + e) // 2
    elif sortedIntList[i] < M :
        s = i + 1
        #라인 20 과 동일한 내용이다.
        #i = (s + e - 1) // 2
        i = (s + e) // 2
    else :
        #문제에서 주어지는 키워드
        #'몇 번째' 에 주의하자.
        #i 는 idx 를 의미한다.
        #'몇 번째' 가 아니다.
        print(i + 1)
        break