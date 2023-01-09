import sys
sys.stdin = open('6. 중복순열 구하기/in2.txt')

N, M = map(int, input().split())


def printallduplicatedpermutation(permutation:list, num:int, lev: int) :
    global cnt
    if (lev == M) :
        for n in permutation :
            print(n, end=' ')
        cnt = cnt + 1
        print()
    else :
        for n in range(1, N + 1) :
            permutation.append(n)
            for m in range(1, N + 1) :
                permutation.append(m)
                printallduplicatedpermutation(permutation.copy(), m, lev + 1)

if __name__ == '__main__' :
    cnt = 0
    printallduplicatedpermutation([], 1, 1)
    print(cnt)