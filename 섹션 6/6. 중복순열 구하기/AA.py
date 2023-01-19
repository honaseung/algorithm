import sys
# sys.stdin = open('input.txt')

N, M = map(int, input().split())


def printallduplicatedpermutation(permutation:list, lev: int) :
    global cnt
    if (lev == M) :
        for n in permutation :
            print(n, end=' ')
        cnt = cnt + 1
        print()
    else :
        for n in range(1, N + 1) :
            permutation[lev] = n
            printallduplicatedpermutation(permutation, lev + 1)

if __name__ == '__main__' :
    cnt = 0
    printallduplicatedpermutation([0] * M, 0)
    print(cnt)