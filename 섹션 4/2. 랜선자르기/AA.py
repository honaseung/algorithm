import sys
#sys.stdin = open('input.txt')

#결정 알고리즘이래!!
#앞선 문제에서 했었던 이분검색을
#활용해서 결정 알고리즘에 적용한다고 하신다.
#귀를 기울여라.
#결정 알고리즘의 특징은
#특정 범위내에 있다는것을 바로 알 수가 있다.
#물론 조금만 생각해보면
#범위를 정해놓고 특정 숫자를 가지고 이분검색을
#실행한다. 그리고 답을 찾았다면
#더 좋은 답이 있는지 찾아가는 알고리즘이다.

#line 을 변형시키지 않았으니
#여기서 접근해도 무방해보인다.
#그래도 항상 유의하자.
def count(len: int) :
    cnt = 0
    for x in line :
        cnt += (x // len)
    return cnt

k, n = map(int, input().split())
line = []
res = 0
largest = 0
for _ in range(k) :
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt <= rt :
    mid = (lt + rt) // 2
    #몇 개의 랜선을 만들 수 있는지 구하는 함수
    if count(mid) >= n :
        #결론적으로 항상 마지막 값이
        #랜선의 최대 길이가 되기 때문에
        #굳이 저장할 필요가 없다.
        #흠 역시 훌륭해.
        res = mid
        lt = mid + 1
    else :
        rt = mid - 1
print(res)