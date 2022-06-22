import sys
#sys.stdin = open('input.txt')

N, K = map(int, input().split())

arr = list(map(int, input().split()))

res = set()
#for 문이 3중이기는 하지만 index 를 컨트롤하는데 있어서는 훌륭한 방법이다.
for i in range(N) :
    for j in range(i + 1, N) :
        for m in range(j + 1, N) :
            res.add(arr[i] + arr[j] + arr[m])
res = list(res)
res.sort(reverse = True)
print(res[K - 1])