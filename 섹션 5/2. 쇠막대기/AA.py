import sys
sys.stdin = open('input.txt')

line = input()
pipesCnt = 0
piecesCnt = 0
stack = []

for presentOrder in line :
    if presentOrder == '(' :
        pipesCnt += 1
    else :
        lastOrder = stack[-1]
        if lastOrder == '(' :
            pipesCnt -= 1
            piecesCnt += pipesCnt
        else :
            pipesCnt -= 1
    stack.append(presentOrder)
print(piecesCnt)