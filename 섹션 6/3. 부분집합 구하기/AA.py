import sys
sys.stdin=open("in1.txt", "r")
# def DFS(v):
#     if v==n+1:
#         for i in range(1, n+1):
#             if ch[i]==1:
#                 print(i, end=' ')
#         print()
#     else:
#         ch[v]=1
#         DFS(v+1)
#         ch[v]=0
#         DFS(v+1)

#downsidal
def printsubset_down(key: int) :
    if (key == 0) :
        for k, v in switchdict.items() :
            if (v == 'off') :
                continue
            else :
                print(k, end=' ')
        print()
    else :
        switchdict.update({key: 'on'})
        printsubset_down(key - 1)
        switchdict.update({key: 'off'})
        printsubset_down(key - 1)

#upsidal
def printsubset_up(key: int) :
    if (key == target + 1) :
        for k, v in switchdict.items() :
            if (v == 'off') :
                continue
            else :
                print(k, end=' ')
        print()
    else :
        #dictionary.update have to give 1 argument
        switchdict.update({key: 'on'})
        printsubset_up(key + 1)
        switchdict.update({key: 'off'})
        printsubset_up(key + 1)

if __name__=="__main__":
    # n=int(input())
    # ch=[0]*(n+1)
    # DFS(1)

    target = int(input())
    switchdict = {k: 'off' for k in range(target)}
    #it's correct but the lecture want to upsidal answer.
    # printsubset_down(target)
    printsubset_up(1)
    