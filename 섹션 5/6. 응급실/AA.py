import sys
#sys.stdin = open('input2.txt')

'''
첫 줄에 자연수 N(5<=N<=100)과 M(0<=M<N) 주어집니다.
두 번째 줄에 접수한 순서대로 환자의 위험도(50<=위험도<=100)가 주어집니다.
위험도는 값이 높을 수록 더 위험하다는 뜻입니다. 같은 값의 위험도가 존재할 수 있습니다.
'''

N, M = map(int, input().split())
cnt = 0
emgInfo = list(map(int, input().split()))

for i in range(len(emgInfo)) :
    #Make an issue if there is how to make tuple easlier in lecture.
    emgInfo[i] = (emgInfo[i], i)

while True :
    #Always choose an action by first patient in a line. Should go in Section5 questions discussion.
    emg  = emgInfo[0]
    if emg[0] >= max(emgInfo)[0] :
        emgInfo.pop(0)
        cnt += 1
        if emg[1] == M :
            print(cnt)
            break
    else :
        #Pop & append at same time makes broken index while for statement
        emgInfo.append(emgInfo.pop(0))

    