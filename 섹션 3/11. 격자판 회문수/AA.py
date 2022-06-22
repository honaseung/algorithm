import sys
sys.stdin = open('input.txt')

board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(3) : 
    for j in range(7) :
        #아 맞네 슬라이스가 있었네
        tmp = board[j][i : i + 5]
        #리스트[::-1] 하면 역순된 리스트가 리턴되니까
        #tmp == tmp[::-1] 하면 오리지널 리스트와 역순 리스트를
        #비교하게 된다.
        if tmp == tmp[::-1] :
            cnt += 1
        #5 개를 두개씩 비교하니까
        for k in range(5 // 2) :
            if board[i + k][j] != board[i + 5 - k - 1][j] :
                break
        else :
            cnt += 1