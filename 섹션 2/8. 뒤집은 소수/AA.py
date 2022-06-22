import sys
#sys.stdin = open('input.txt')

def reverse(x) :
    res = 0
    #x 는 처음에는 오리지널 숫자이지만
    #while 문을 돌면서 x 를 10 으로 나눈
    #몫이된다.
    while x > 0 :
        #x 를 10 으로 나눈 나머지는
        #첫째자리 숫자를 추출하는 방법이다.
        t = x % 10
        #추출된 숫자들을 자릿수마다 채워준다.
        #뒤에서부터
        res = res* 10 + t
        #다음 자릿수 숫자를 추출 하기 위한 변형
        x = x // 10
    return res

def isPrime(x) :
    #1 은 소수가 아님.
    if x == 1 :
        return False
    #오오 이거 뭐냐
    #내 발상이 맞았잖아??
    #index 접근이 아니어도 맞다고??
    #거 검거한놈 풀어줘
    #약수는 자기 자신 나누기 2 한거 까지만 존재한다고 하셨어
    #그리고 그게 내 발상이기도 하고
    #헤헿
    for i in range(2, x // 2 + 1) :
        if x % i == 0 :
            return False
    else :
        return True

n = int(input())
a = list(map(int, input().split()))

for x in a :
    tmp = reverse(x)
    if isPrime(tmp) :
        print(tmp, end = " ")