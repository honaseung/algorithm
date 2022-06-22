import sys
#sys.stdin = open('input.txt')

#이 코드는 분명 센세의 코드가 맞지만
#센세의 코드를 생각나는대로 짜봤을뿐이니
#실제와는 다를수도있습니다.

n = int(input())
a = list(map(int, input().split()))
#나와는 다르게 그냥 0 으로 초기화했다.
#나는 최대값 또는 최소값을 항상 이용하는데
#나쁜 습관은 아니지만 덜 간결해보일 순 있다.
seq = [0] * n
for i in range(len(a)) :
    for j in range(len(a)) :
        if a[i] == 0 and seq[j] == 0 :
            seq[j] = i + 1
            break
        #그냥 else 가 아닌 elif 로
        #한번 더 조건을 걸어준다.
        #seq[j] == 0 이 True 라면
        #seq[j] 에는 아직 값이 할당되지않은.
        #즉, i + 1 보다 큰 임의의값을 의미한다.
        elif seq[j] == 0 :
            a[i] -= 1

for x in seq :
    print(x, end = " ")