import sys
#sys.stdin = open('in3.txt')

N, M = map(int, input().split())
pWeight = list(map(int, input().split()))
pWeight.sort(reverse = True)
cnt = 0

#절반으로 나누면 안돼.
#이유는 아마도 한번에 두명 타는 경우와
#한번에 한명 타는 두 가지의 경우가 발생하기 때문인것 같아.
#for 구문은 횟수를 정확히 알때 사용하자.
#for i in range(len(pWeight) // 2) :
lt = 0
rt = N - 1

#while 구문은 ~ 동안에 라는 사실을 기억하자.
#마지막에 남아있는 한명까지 배에 태우기 위해서는
#반드시 두개의 포인터가 같은 상황까지 처리를 해줘야만 한다.
#while lt < rt :
while lt <= rt :
    #무조건 무게가 큰 두명을 한꺼번에 태우려는것은
    #옳지않다. 왜냐하면
    #제일 무거운 사람과 제일 가벼운 사람이
    #한꺼번에 탈 수도 있기 때문이고
    #문제에서는 보트를 최소한으로 사용하려고 하기 때문이다.
    #if pWeight[i] + pWeight[i + 1] > M :

    #문제가 있다.
    #두 사람을 태우면 맨 앞과 맨 뒤를 태운다. 매번
    #이 사실은 변함이 없다. 그래서 맨 앞과 맨 뒤를
    #pop 시켜버리면 된다.
    #그런데 한사람만 태우면 맨 앞만 pop 시킨다.
    #여기서 문제가 발생한다.
    #사실 꼭 여기서만 발생하는 문제는 아닐것같은데
    #pop 을 시켜버리면 idx 가 변한다.
    #따라서 단순히 N 과 i 를 이요해서 idx 를 잡아줄 순 없다.
    #새로운 변수가 필요하거나 맨 뒤를 접근하는 새로운 방식이 필요하다.
    #예를 들면 -1 같은거... 어??

    #흠 잘 안되네...
    #결국엔 두개의 포인터를 활용해서
    #끝에서부터 안쪽으로 접근하는 방식을 활용해야할 것 같다.
    #pop 은 역시 아무리 생각해도 리스트를 변경하기때문에
    #위험한 방식이야.

    #pop 은 하지 않기로 했어.
    #위험한 방식이라는걸 잘아니까.
    #그런데도 오답이 나오는 이유는 이거야.
    #lt 와 rt 두 포인터가 끝에서부터 점점 가운데로 움직이고 있어.
    #그런데 마지막에 승객이 한명 남았을때가 문제가 되는거야.
    #즉 두 포인터가 한명을 가르키고 있을때가 문제가 되는거야.
    #왜냐하면 마지막 한명의 몸무게는 * 2 로 계산되어서
    #이상현상이 발생하는것 같아.
    #음 그렇지만... 이걸 안다고 하더라도 문제가 발생할
    #이유는 없다고 보는데...
    #내 생각이 맞는지부터 체크해야하는데 체크가 쉽지가 않아.
    #흐음 일단은 conditinal break 가 어떻게 작동하는지 확인하자.
    if pWeight[lt] + pWeight[rt] > M :
        lt += 1
        cnt += 1
    else :
        lt += 1
        rt -= 1
        cnt += 1
print(cnt)