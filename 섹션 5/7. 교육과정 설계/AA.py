import sys
from collections import deque

#sys.stdin = open('in2.txt')

'''
첫 줄에 한 줄에 필수과목의 순서가 주어집니다. 모든 과목은 영문 대문자입니다.
두 번째 줄에 N(1<=N<=10)이 주어집니다.
세 번 째 줄부터 현수가 짠 N개의 수업설계가 주어집니다.(수업설계의 길이는 30이하이다)
수업설계는 같은 과목을 여러 번 이수하도록 설계해도 됩니다.
'''

requiredSubList = deque(input())
N = int(input())

for i in range(N) :
    courses = input()
    #Should use copy function. Without copy, it could change all variables value. Mention it on an issue.
    requiredSubListCopy = requiredSubList.copy()
    for x in courses :
        #No need to pop before check. Check first and pop is right. Write it down on the HEAD RULES.
        if x == requiredSubListCopy[0] :
            requiredSubListCopy.popleft()
            #'not' keyword replace '!'. Mention it on an issue.
            if not requiredSubListCopy :
                #No need to check whole element. It's already satisfy condition.
                #Besides, Without break, it could occur an error without break.
                break
        #If take a follow-up course first, It's wrong coureses. Teacher let me know.
        elif x in requiredSubListCopy :
            break
    if requiredSubListCopy :
        print('#%d NO' % (i + 1))
    else :
        print('#%d YES' % (i + 1))
            