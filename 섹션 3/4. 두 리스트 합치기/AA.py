import sys
#sys.stdin = open('input.txt')

#ㅋㅋ 야 그거 아니래
#배열을 합쳐서 다시 sort 하는건 8log8 이나 걸리는데
#이미 정렬이 되어 있는 배열을 합치는건 그냥 8 이면 끝난대
#다시 해보자

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1, p2 = 0, 0
c = []
#두 포인터 중 하나라도 끝까지 갔을경우 종료
#내 코드에서는 무한 반복문으로 만들고서 중간에 break 하지만
#여기서는 조건을 그냥 걸고 시작한다.
#조건은 p1 < n 이면서 p2 < m 일때이다.
#이렇게 두면 둘 중 하나라도 만족 안돼면 종료되니까.
while p1 < n and p2 < m :
    if a[p1] <= b[p2] :
        c.append(a[p1])
        p1 += 1
    else :
        c.append(b[p2])
        p2 += 1
if p1 < n :
    #extend 함수가 아닌 + 연산자로 리스트를 합치는게 가능한가보다.
    c = c + a[p1:]
if p2 < m :
    c = c + b[p2:]

for x in c :
    print(x, end = " ")