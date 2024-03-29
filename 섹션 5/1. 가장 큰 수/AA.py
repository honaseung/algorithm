import sys
#sys.stdin = open('input2.txt')

N , m = input().split()
N = list(map(int, N))
m = int(m)

#맨 앞자리가 될 수 있는 숫자중에서만
#숫자를 제거한다.
#여기서 맨 앞자리가 될 수 있는 숫자란
#다른 숫자를 제거하는 과정을 마쳤을때
#자신이 제일 앞자리가 될 수 있는 숫자를 말한다.
#그리고 임의의 숫자가 주어졌을때
#맨 앞자리가 될 수 있는 숫자들중에서
#제일 큰 숫자 하나만 남겼을때
#비로소 가장 큰 수가 된다.
#그래서 아래에서 할 작업은
#맨 앞자리가 될 수 있는 숫자중에서
#작은 숫자들은 계속 제거해 나간다.
#여기까지가 컴퓨터없이 문제를 푸는 과정이다.

#여기서부터는 컴퓨터로 문제를 푸는 과정이다.
#방법 1
#origin 숫자에서 제거 대상인 숫자들을 제거한 후에
#문자를 출력한다.
#실패했다.
'''
highest = N[0]
newNum = ''
for i in range(m + 1) :
    if int(N[i]) > int(highest) :
        newNum = N.replace(highest, '')
        highest = N[i]
    else :
        newNum = N.replace(N[i], '')
print(newNum)
'''

#방법 2
#origin 숫자에서 제거 대상인 숫자들을 슬라이스한 후에
#그중에서 최대값만을 살리고
#슬라이스 되지않은 숫자들과 합친다.
'''
print(N)
print(max(N[:m + 1]))
print(N[m + 1:])
print(max(N[:m + 1]) + N[m + 1:])
'''

#생각이 너무 많아서 잘못된 규칙을 찾았다.
#혹은 생각이 너무 짧았다거나

#방법3
#현제 포인터에 있는 숫자보다 큰 수가 앞에 있다면
#그 수를 제거하여 현제 포인터의 수를 제일 앞으로 보낸다.
#단, 제거 횟수가 남아있는 동안에만

stack = []
for x in N :
    #비어있지않으면
    #m 이 0 보다 크면
    #스택에 가장 최신자료가 나보다 작으면
    while stack and m > 0 and stack[-1] < x :
        #가장 최신자료를 제거
        stack.pop()
        #제거횟수 감소
        m -= 1
    #자신보다 작은 수는 전부 제거한 후에 자신을 추가
    stack.append(x)
#끝까지 돌았는데 제거 횟수가 남은 경우
if m != 0 :
    #제거 횟수만큼 스택의 뒤에서부터 제거
    #[시작:끝(이놈의뺀다):스텝]
    stack = stack[:-m]
#다른 방법이 있지않을까했는데 잘 모르겠고
#이런 방식으로 문자열을 이음.
print(''.join(map(str, stack)))