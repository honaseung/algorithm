import sys
#sys.stdin = open('in3.txt')

numList = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7) :
    for j in range(7) :
        if j < 3 :
            for k in range(5 // 2) :
                if numList[i][j + k] != numList[i][j - (3 + k)] :
                    break
            else : 
                cnt += 1
        if i < 3 :
            for k in range(5 // 2) :
                if numList[i + k][j] != numList[i - (3 + k)][j] :
                    break
            else :
                cnt += 1
print(cnt)

#직접 적으면서 문제를 풀면 확실히 눈에 보이지않던것들이 보인다.
#예를들면 포인터, idx 컨트롤의 규칙 같은 부분이다.
#그런데도 불구하고 놓치는 부분들이 생기기마련이다.
#이런 부분들은 솔직히 경험으로 때려 부어서 풀어야하니 조급해하지말자.