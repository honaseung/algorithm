import sys
# sys.stdin = open("4. 합이 같은 부분집합/in4.txt")

length = int(input())
targetlist = list(map(int, input().split()))
targetdict = {key: 'left' for key in targetlist}
istargetsumeven = not bool(sum(targetlist) % 2)

keyset = list(targetdict.keys())
isPossible = False

def findequalsumsubset(idx) :
    global isPossible
    if (idx == length) :
        leftsum = 0
        rightsum = 0
        for k, v in targetdict.items() :
            if (v == 'left') :
                leftsum = leftsum + k
            else :
                rightsum = rightsum + k
        if (leftsum == rightsum) :
            isPossible = True
    else :
        targetdict[keyset[idx]] = 'right'
        findequalsumsubset(idx+1)
        targetdict[keyset[idx]] = 'left'
        findequalsumsubset(idx+1)

if (istargetsumeven) :
    findequalsumsubset(0)
    if (isPossible) :
        print("YES")
    else :
        print("NO")
else :
    print("NO")