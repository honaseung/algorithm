import sys
sys.stdin = open('input.txt')

line = input()
pipesCnt = 0
piecesCnt = 0
stack = [line[0]]

for i in range(1, len(line)) :
    presentOrder =  line[i]
    lastOrder = stack[-1]
    if lastOrder == '(' :
        if presentOrder == '(' :
            pipesCnt += 1
        else :
            piecesCnt += pipesCnt
    else : 
        if presentOrder == ')' :
            pipesCnt -= 1
            piecesCnt += 1

    stack.append(presentOrder)
print(piecesCnt)
'''
stack = []
for x in line :
    if x == '(' :
        stack.append(x)
    else :
        stack.pop()
        if stack[-1] == '(' :
            piecesCnt += len(stack)
        else :
            piecesCnt += 1
print(piecesCnt)
'''