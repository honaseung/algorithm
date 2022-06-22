from collections import deque
import sys
#sys.stdin = open('input.txt')

N = int(input())
numList = deque(map(int, input().split()))

#문제에서 주어지는 정보중에
#최소나 최대라는 문구가 있다.
#이것이 의미하는것이
#모든 경우를 전부 시도하고
#그 중에서 최대 또는 최소를
#구하라는 의미가 아닐때도 있다.
#그리디에서는 아무래도 그런것 같다.
#완전하게 끝까지 실행하지 않고
#최적의 답을 찾자마자 그만두니까
#그리디인거다.

now = float('-inf')
cnt = 0
msg = ''
while True :
    lt = numList[0]
    rt = numList[-1]

    if lt < rt and lt > now :
        cnt += 1
        msg += 'L'
        now = numList.popleft()
    elif rt < lt and rt > now :
        cnt += 1
        msg += 'R'
        now = numList.pop()
    else :
        if lt > now :
            cnt += 1
            msg += 'L'
            now = numList.popleft()
        elif rt > now :
            cnt += 1
            msg += 'R'
            now = numList.pop()
        else :
            break
print(cnt)
print(msg)