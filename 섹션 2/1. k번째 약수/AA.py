import sys
#sys.stdin = open("input.txt")

n, k = map(int, input().split())

#내풀이
#주어진 숫자의 약수들을 찾아서 리스트로 만드는 함수를 생성
#리스트는 1부터 시작해서 1씩 증가해 주어진 숫자까지 접근하기때문에
#반드시 오름차순으로 생성된다.
#생성된 약수들의 리스트를 리턴하여 k 번째 숫자를 출력한다.
def findAliquot(n) :
    a = []
    for i in range(1, n + 1) :
        if n % i == 0 :
            a.append(i)
    return a


aliquot = findAliquot(n)
if len(aliquot) < k :
    print(-1)
else :
    print(findAliquot(n)[k - 1])
'''
#선생님풀이
#k번째 약수 출력에 집중한 함수
#k번째 약수를 찾았으면 출력하고 후의 약수들은 구하지 않는다.
cnt = 0
for i in range(1, n + 1) :
    if n % i == 0 :
        cnt = cnt + 1
    if cnt == k :
        print(i)
        break
else :
    print(-1)
'''