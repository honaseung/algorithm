import sys
from collections import deque
#sys.stdin = open('input.txt')

n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
cnt = 0

#p 가 비어있지 않는동안
#isEmpty 같은 느낌
while p :
    #마지막 한명일때의
    #에러를 방지하기위한 연산
    #내가 너무 깊게 생각했나.
    #일단 논리적으로 마지막 한명을
    #두번 계산하는것 자체가 오류니까
    #그냥 계산안하도록 막아버림.
    if len(p) == 1 :
        cnt += 1
        break
    if p[0] + p[-1] > limit :
        #맨 뒷자리 pop
        p.pop()
        cnt += 1
    else :
        p.pop(0)
        #내가 겪었던 문제랑 동일하게
        #pop 을 동시에 두번하면
        #마지막에 한명에 대한 연산에서
        #에러가 발생한다.
        p.pop()
        cnt += 1
print(cnt)


#덱 자료구로를 활용한 풀이
#덱 구조는 포인터를 떙기는 연산이
#필요없이 pop 시키면 알아서 포인터가
#이동한다고 함. 잘은 모르겠음.
q = deque(p)

while q :
    if len(q) == 1 :
        cnt += 1
        break
    if q[0] + q[-1] > limit :
        q.pop()
        cnt += 1
    else :
        #기존에는 pop(0) 인것을
        #popleft 로 표현가능
        #그게 끝??
        #모름 ㅋㅋ
        q.popleft()
        q.pop()
        cnt += 1
#print(cnt)