import sys
#sys.stdin = open('input.txt')

#헐 다중 for 문으로 처리했는데
#비효율적이라고 합니다.
#다시 해볼까요??

#미안합니다 ㅠㅠ
#못했어요 결국
#정답 공개합니다.

n = int(input())
body = []
for i in range(n) :
    a, b = map(int, input().split())
    body.append((a, b))
body.sort(reverse = True)
largest = 0
cnt = 0
#x 는 안쓰지만 y 를 받기 위해서 넣어둠.
for x, y in body :
    if y > largest :
        largest = y
        cnt += 1
print(cnt)