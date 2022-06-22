import sys
#sys.stdin = open('input.txt')

N, M = map(int, input().split())
#굳이 더 큰 리스트를 만들 필요없이 나올 수 있는 최대 합계 만큼만 초기화 해도 된다.
#단 주의 해야할것은 지금 인덱스를 두 값의 합으로 활용하고 있기 때문에
#단순히 (N + M) 이라고 한다면 마지막 인덱스는
#N + M - 1 이 된다. 그래서 N + M 은 카운트할 수 가 없게 된다.
cnt = [0] * (N + M + 1)
max = float('-inf')
#1 부터 시작해서 N + 1 전까지 하는것은
#최소값인 1 부터 최대값인 N 까지 이용하기 위함이다.
for i in range(1 , N + 1) :
    for j in range(1, M + 1) :
        cnt[i + j] += 1
#위와 마찬가치로 사실 0 부터 시작할 필요가 없다.
#최소값은 2 이고 최대값은 N + M 이기 때문이다.
#또한 이보다도 cnt 는 이미 리스트이고 내장 함수인 max 를 사용가능하기에
#아래처럼 코드를 짤 필요는 없다. 작동 원리만 이해하자.
for i in range(N + M + 1) :
    if cnt[i] > max :
        max = cnt[i]
#여기 또한 0 부터 시작할 필요는 없다.
#물론 인덱스이기에 보통은 0 부터가 맞지만 이 문제에서
#0 과 1 의 인덱스가 사용될 이유는 없다.
for i in range(N + M + 1) :
    if cnt[i] == max :
        print(i, end = " ")