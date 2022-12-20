import sys
sys.stdin = open('5. 바둑이 승차/input.txt')

C, N = map(int, input().split())
list = []

for _ in range(N) :
    list.append(int(input()))

print(C, N, list)