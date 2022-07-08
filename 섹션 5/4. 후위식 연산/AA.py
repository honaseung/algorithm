import sys
sys.stdin = open('input.txt')

postFix = input()
stack = []
#Change confused variable name.
lastValue = 0

def calculate(operation, *operand) :
    #Operand's type is tuple. Should mention it on issue.
    #Mention how to make switch statement 
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
        lastValue = stack.pop()
        #I tried to use eval python's function. But i failed. Mention it on issue.
        #It's important to pass parameters in the right order.
        lastValue = calculate(x, stack.pop(), lastValue)
        stack.append(lastValue)

print(lastValue)
        
            

