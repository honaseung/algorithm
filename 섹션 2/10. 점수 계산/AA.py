import sys
#sys.stdin = open('input.txt')

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0

for x in a :
    if x == 1 :
        cnt += 1
        sum += cnt
    else :
        cnt = 0
print(sum)
#걍 뭐 소스가 복붙 수준으로 똑같은데
#특별한 발상도 없고
#뭐 이런 문제도 있는거지