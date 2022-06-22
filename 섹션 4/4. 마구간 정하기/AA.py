import sys
sys.stdin = open('input.txt')

n, c = map(int, input().split())
Line = []
for _ in range(n) :
    Line.append(int(input()))
Line.sort()

def Count(len) :
    cnt = 1
    #마지막 말의 지점
    ep = Line[0]
    for i in range(1, n) :
        if Line[i] - ep >= len :
            cnt += 1
            ep = Line[i]
    return cnt

lt = 1
rt = Line[n - 1]
while lt <= rt :
    mid = (lt + rt) // 2
    if Count(mid) >= c :
        res = mid
        lt = mid + 1
    else :
        rt = mid - 1
print(res)
