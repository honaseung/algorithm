import sys
#sys.stdin = open('input.txt')

n = int(input())
meeting = []
for i in range(n) :
    s, e = map(int, input().split())
    #튜플로??
    #뭐 사실 관계는 없지.
    #튜플로 하면 값 변경이 어려운데
    #여기서는 값 변경이 없으니까!!
    meeting.append((s, e))
#람다 정답!!
#신난당 ㅎㅎ
#오 근데 이건 몰랐다.
#key 에 들어갈 리턴값을
#() 에 담아서 정렬기준 순서를 정해줄 수 있다.
meeting.sort(key = lambda x: (x[1], x[0]))

#endTime
et = 0
cnt = 0
#튜플을 활용한 이유
#명심하자.
for s, e in meeting :
    #초기값이 0 이니까
    #첫 회의는 반드시 진행
    if s >= et :
        et = e
        cnt += 1
print(cnt)