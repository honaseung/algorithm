import sys
#sys.stdin = open('input.txt')

N = int(input())

arr = list(map(int, input().split()))

def digit_sum_int(x) :
    sum = 0
    #x 의 각 자릿수를 다 처리 할때까지 반복하기 위함
    while x > 0 :
        #x 를 10 으로 나눈 나머지
        #10 으로 나누는 것은 각 자릿수의 합을 구하기 위함
        sum += x % 10
        #x 를 10 으로 나눈 몫
        #x 를 변경해서 자릿수를 뒤에서 부터 하나씩 줄여준다.
        x = x // 10
    return sum

#이것도 가능
#이럴거면 map, int 는 할 필요가 없지.
def digit_sum_str(x) :
    sum = 0
    for i in str(x) :
        sum += int(i)
    return sum

max = float('-inf')
for x in arr :
    tot = digit_sum_str(x)
    if tot > max :
        max = tot
        #인덱스나 다른 값을 활용하는 것이 아닌 x 를 바로 활용하였다.
        res = x
print(res)

#지금 보면 나는 결과값에 접근하는 가장 빠른 방법(결과값을 도출하자마자 프로그램 종료)을 간과하거나
#결과값을 도출했음에도 출력하지 않고 한번 거쳐서 출력하는 경향이 있다.
#주의바람!