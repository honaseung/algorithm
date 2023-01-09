import sys
# sys.stdin = open('5. 바둑이 승차/in5.txt')

C, N = map(int, input().split())
weights = []

for _ in range(N) :
    weights.append(int(input()))

def maximumweight(lev: int, maximumlevsumweight: int, sumweight: int) :
    global maxsumweight
    #on the tree, if you use all node(means go leftest), sumweight is going to be same as totalsumweight.
    #so 'maximumlevsumweight' is always biggest weight(leftest) you get while in processing.
    #it's different with 'sumweight'. 'Sumweight' is real sumweight, 'Maximumlevsumweight' is an assumed sumweight.
    #'totalsumweight - maximumlevsumweight' means all nodes(not proceeded) are going to left.
    #in the end 'totalsumweight - maximumlevsumweight + sumweight' means maximum sum as possible as from now on.
    #you don't need to go down if there is no possibility of chainging maxsumweight.
    if (maxsumweight > totalsumweight - maximumlevsumweight + sumweight) :
        return
    #it can be good cut condition.
    #because there is no assurance of using whole remaining nodes.
    # if (C < totalsumweight - maximumlevsumweight + sumweight) :
    #     return
    if (sumweight > C) :
        return
    if (sumweight == C) :
        print(sumweight)
        sys.exit(0)
    if (lev == N) :
        if (sumweight > maxsumweight) :
            maxsumweight = sumweight
    else :
        maximumweight(lev + 1, sumweight + weights[lev], sumweight + weights[lev])
        maximumweight(lev + 1, sumweight + weights[lev], sumweight)

if __name__ == '__main__' :
    maxsumweight = float('-inf')
    totalsumweight = sum(weights)
    maximumweight(0, 0, 0)
    print(maxsumweight)