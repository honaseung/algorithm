import sys
#sys.stdin = open('in1.txt')

postFix = input()
stack = []
currentValue = float('-inf')

def calculate(operation, *operand) :
    #Operand's type is tuple. Should mention it on discussion.
    match operation :
        case '*' :
            return operand[0] * operand[1]
        case '/' :
            return operand[0] / operand[1]
        case '+' :
            return operand[0] + operand[1]
        case '-' :
            return operand[0] - operand[1]
        case _ :
            print('wrong operation')
            return 0

for x in postFix :
    if x.isnumeric() :
        stack.append(int(x))
    else :
        currentValue = stack.pop()
        #I tried to use eval python's function. But i failed. Mention it on issue.
        currentValue = calculate(x, stack.pop(), currentValue)
        stack.append(currentValue)

print(currentValue)
        
            

