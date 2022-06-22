import sys
#sys.stdin = open('input.txt')

def toInt(str: str) :
    num = 0
    #j = 0
    for x in str :
        #try, except 구문
        #알고리즘 코딩에 타당한가??
        #근데 아무리 생각해도 try, except 는 레전드다.

        #* 10 하고 더하는거 센세방식
        #0 이 들어와도 끄떡없다.
        #알아두면 되게 좋은 방식이라고 생각한다.
        #아 물론 내 방식도!!
        #말 나온김에 내 방식도 해보자.
        try: num = num * 10 + int(x)
        #그냥 해본거라 당근 빠따로 i 는 없다.
        #i 를 만드는건 어렵지 않기에 설명은 생략한다.
        #try :
        #num = (10 ** j) + int(str[i])
        #j = j + 1
        except: continue
    return num

def cntAliquot(num: int) :
    #모든 정수가 1 과 자기 자신은 약수로 가지며
    #제일 큰 약수는 자기 자신을 2 로 나눈 값이기에
    #작성된 코드
    cnt = 2
    for i in range(2, num // 2 + 1) :
        if num % i == 0 :
            cnt += 1
    return cnt

str = input()

tarNum = toInt(str)
print(tarNum)
print(cntAliquot(tarNum))