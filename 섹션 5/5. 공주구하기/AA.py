import sys
#sys.stdin = open('input.txt')

N, K = map(int, input().split())

line = list(range(1, N + 1))

deatCnt = 0

while len(line) > 1 :
    #It's important to put this sentence in right line.
    deatCnt += 1
    if deatCnt == K :
        line.pop(0)
        deatCnt = 0
    else :
        line.append(line.pop(0))

print(line.pop())