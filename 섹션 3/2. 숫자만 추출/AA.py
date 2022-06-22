import sys
#sys.stdin = open('input.txt')

s = input()
res = 0
for x in s :
    #isdecimal 와 isdigit 는 다르다.
    #isdigit 는 숫자가 될 수 있으면 다 가져오고
    #isdecimal 은 숫자(0 ~ 9)만 가져온다.
    #이 함수는 알아두자
    #솔직히 이 함수 몰라서 나는 그냥
    #아스키 코드 이용할라캣다.
    #단어 하나하나가 숫자가 된들해도 두 자리가 될리가 없으니
    #걍 두자리 넘어가면 숫자가 아닌걸로 취급해서 처리하려했다.
    #좋은 발상이다.
    #근데 왜 강의가 재생이 안돼지.
    if x.isdecimal() :
        res = res * 10 + int(x)
print(res)
cnt = 0
#그냥 진짜 정석적인 약수 갯수 구하기
#1 부터 자기자신 까지 다 돈다.
#솔직히 for 문 2 번 안돌게 하기 위해
#2 부터 자기 자신 // 2 까지 도는건 훌륭한데
#실수할 가능성은 있다.
#뭐 그럼에도 해보는건 당연히 좋다.
for i in range(1, res + 1) :
    if res % i == 0 :
        cnt += 1
print(cnt)