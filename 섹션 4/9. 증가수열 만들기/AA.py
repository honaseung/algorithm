import sys
sys.stdin = open('input.txt')

n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n - 1
#마지막에 출력한 숫자
last = 0
res = ''
tmp = []
#가운데 숫자까지 전부 탐색
while lt <= rt :
    #마지막 숫자보다 크다면
    if a[lt] > last :
        #튜플 형태로 담기.
        tmp.append((a[lt], 'L'))
    if a[rt] > last :
        tmp.append((a[rt], 'R'))
    #마지막 숫자보다 큰것들만 모아서
    #정렬해버림
    #이렇게 하면 tmp 의 길이는
    #0 또는 1 또는 2 가 됨.
    tmp.sort()
    #길이가 0 이라면
    #lt 와 rt 가 가르키는 숫자가
    #last 보다 작으니 증가수열을 만들 수
    #없음을 의미.
    if len(tmp) == 0 :
        break
    else :
        #문자 담기
        res = res + res[0][1]
        #마지막 숫자 변경
        last = tmp[0][0]
        #lt 와 rt 를 변경해줄 조건
        if tmp [0][1] == 'L' :
            lt += 1
        else :
            rt -= 1
    #리스트 초기화 함수
    tmp.clear()
#그냥 문자열의 길이를 출력해버림
print(len(res))
print(res)

#이 문제는 굳이 그리디로 바로보고
#처리할 필요는 없다.
#그렇지만 그리디로 보고 풀면
#더 간결하긴하다.