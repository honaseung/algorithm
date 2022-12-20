import sys
#sys.stdin=open("input.txt", "r")
# def DFS(L, sum):
#     if sum>total//2:
#         return
#     if L==n:
#         if sum==(total-sum):
#             print("YES")
#             sys.exit(0)
#     else:
#         DFS(L+1, sum+a[L])
#         DFS(L+1, sum)


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


if __name__=="__main__":
    # n=int(input())
    # a=list(map(int, input().split()))
    # total=sum(a)
    # DFS(0, 0)
    # print("NO")

    length = int(input())
    targetlist = list(map(int, input().split()))
    targetdict = {key: 'left' for key in targetlist}
    istargetsumeven = not bool(sum(targetlist) % 2)

    keyset = list(targetdict.keys())
    #global variable
    isPossible = False

    if (istargetsumeven) :
        findequalsumsubset(0)
        if (isPossible) :
            print("YES")
        else :
            print("NO")
    else :
        print("NO")