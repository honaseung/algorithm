import sys
#sys.stdin = open('input.txt')

#함수명이나 매개변수나 맘에 안드는데 걍 하라니까 하는거임
def digit_sum(x: list) :
    maxIdx = 0
    maxSum = float('-inf')
    for i, x in enumerate(arr) :
        #다음 문자열이 들어올때 마다 초기화해주는것
        #절대 문자 더하고 또 초기화하고... 그르믄 안돼
        #그니깐 아래 for 문에 들가면 안된다는말이다.
        sum = 0
        for y in x :
            sum += int(y)
        if sum > maxSum :
            maxSum = sum
            maxIdx = i
    print(arr[maxIdx])
    #maxIdx 를 리턴해서 밖에서 출력해도 되지만
    #여기서는 리턴 없이 안에서 출력해버림.
    #사실 출력해야하는 값이 최대합을 가지는 값이기에
    #maxIdx 를 활용하는것이 아닌 그냥 x 를 활용해버려도 됨.
    #물론 그러려면 x 를 따로 저장해서 활용해야함.

#자릿수를 구하는 함수를 만들라고??
#굳이?
#일단 강의를 보자.

N = int(input())

#str 을 int 로 map 하지 않는것은 의도되었다.
#int 로 map 한 후에 각 자릿수에 접근하는것보다
#str 을 유지하여 각 요소에 리스트처럼 접근하는것이 더 쉽기 때문이다.
arr = list(input().split())

digit_sum(arr)

#이거 맞아?
#왤캐 시시해?
#내가... 강해진건가...?
#ㅋㅋ 그럴리가 없지

#문제와는 관련 없지만 검색하다가 발견한 사항들
#문자열에서 특정 문자 제거하기
#replace 활용
'''
대상 문자열
제거할 문자들(문자열)
for i in range(len(제거할 문자들)) :
    대상 문자열.raplace(제거할 문자들[i], "")
'''
#join 활용
#not in 이라는 구문에 대해 알아두자.
#!contains 와 같은 느낌인듯 하다.
#그럼 contains 는?
#그건 다음 시간에
'''
대상 문자열
제거할 문자들(문자열)
"".join(x for x in 대상 문자열 if x not in 제거할 문자들)
'''
#sub 활용
#re 라는 모듈을 활용한다.
'''
import re
re.sub(변경할 문자들을 정규식으로 표현하여 문자열로 입력, 변경할 문자(여기서는 제거이기에 ""), 대상 문자열, 변경 횟수)
*정규식은 '!? => \'|\!|\? 이렇게 말하는거 정규표현식 아님
'''