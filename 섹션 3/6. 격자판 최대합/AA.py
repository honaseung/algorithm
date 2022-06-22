import sys
#sys.stdin = open('input.txt')
n = int(input())
#오호 이거 초반에 배운 파이선 기본 지식을 활용하면 나올법한 코드네
#솔직히 쓸 일이 없어서 까먹었던것 같다.
#이 기회에 다시 한번 상기해두자.
#아 물론 [list...] 는 까먹었다고 용서하진 않을거야 ㅋㅋ
#다른 언어(javascript)에서도 가능하니까.
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n) :
    #??
    #sum1, sum2 = 0 과 같은듯
    sum1 = sum2 = 0
    #솔직히 시간제한이 좀만 더 짧았어도
    #이 문제는 틀렸을수도 있다.
    #센세 방식에서는 rowSum 과 colSum 을
    #동시에 구하는 방식이라서
    #더 안전하다.
    #나는 좀 더 범용성 있는 코드를 만들었다.
    #실전에서는 좋을지 몰라도
    #알고리즘에서는 안좋은 습관이 될 수도 있다.
    #주의하자.
    #결국 2 중 for 문에서는 센세도 벗어날 수 없었나보다.
    for j in range(n) :
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest :
        largest = sum1
    if sum2 > largest :
        largest = sum2
    #최대값은 이미 저장했으니 초기화 해버렸.
    sum1 = sum2 = 0
#이걸 n 번할 필요가 있을까??
#응 당연히 있지
#n 은 i 가 변화할 값이니까
#물론 대각선 합은 경우의 수가 2 개 밖에 없지.
#근데 대각선 각각의 요소들은 n 개가 있으니까.
for i in range(n) :
    sum1 += a[i][i]
    sum2 += a[i][n - i - 1]
    if sum1 > largest :
        largest = sum1
    if sum2 > largest :
        largest = sum2
print(largest)