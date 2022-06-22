import sys
#sys.stdin = open('input.txt')

N = int(input())

arr = [0] * (N + 1)

cnt = 0

for i in range(2, N + 1) :
    #나의 코드중에서 arr[i] == 1 continue 의 반대 버전이다.
    #여기서는 오히려 == 0 일 경우 for 문을 진행하는 방식을 택했다.
    #나의 코드가 나쁘다고 할 순 없으나 아래 코드가 좀 더 깔끔해보이는건 사실이다.
    if arr[i] == 0 :
        cnt += 1
        #step 매개변수를 이용하여 배수만 접근하도록 하였다.
        #훨씬 효율적이다. 알아두자.
        for j in range(i, N + 1, i) :
            arr[j] = 1
print(cnt)