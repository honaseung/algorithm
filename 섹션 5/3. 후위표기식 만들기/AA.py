import sys
#sys.stdin = open('in4.txt')

midExp = input()
bakExp = []
stack = []

mulDiv = ['*', '/']
pluSub = ['+', '-']

def chkPriority(exp: str, stk: list) :
    if len(stk) == 0 :
        stk.append(exp)
    elif exp in mulDiv :
        if stk[-1] in mulDiv :
            bakExp.append(stk.pop())
        stk.append(exp)
    elif exp in pluSub :
        while stk :
            bakExp.append(stk.pop())
        stk.append(exp)

def convertToPostFix(lst: list, stk: list) :
    i = 0
    while i < (len(lst)) :
        presentExp = lst[i]
        if presentExp.isnumeric() :
            bakExp.append(presentExp)
        else :
            if presentExp == '(' :
                closeExp = lst.index(')', i)
                newList = lst[i + 1 : closeExp]
                convertToPostFix(newList, [])
                i = closeExp
            else :
                chkPriority(presentExp, stk)
        i += 1
    bakExp.extend(reversed(stk))
    
convertToPostFix(midExp, stack)
print(''.join(bakExp))