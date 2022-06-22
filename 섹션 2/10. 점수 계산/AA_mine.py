import sys
#sys.stdin = open('input.txt')

#뭐지??
#너무 쉬워서 주석 달 곳도 달 생각도 못했는데
#대충 생각하던거 적어보자면
#과연 알고리즘 코드를 짤때 파이선 제공 함수를
#적극 활용하는게 좋은가??
#정답만을 추구하는 코드가 좋은 코드인가??
N = int(input())
chkArr = list(map(int, input().split()))
chain = 0
score = 0
for i in range(N) :
    if chkArr[i] == 0 :
        chain = 0
        #얘 뭐니
        score += chain
    elif chkArr[i] == 1 :
        chain += 1
        score += chain
print(score)