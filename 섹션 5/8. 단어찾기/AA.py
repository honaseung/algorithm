import sys
#sys.stdin = open('input.txt')

'''
첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다.
두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 이어 바로 다음 줄부터 시에
쓰인 N-1개의 단어가 주어진다.
'''

N = int(input())

originalDic = { input(): 1 for _ in range(N)}
usedDic = [ input() for _ in range(N - 1) ]

#Why dictionary has an update function?

for x in usedDic :
    originalDic[x] = 0

for x in originalDic.keys() :
    if originalDic[x] == 1 :
        print(x)
        break