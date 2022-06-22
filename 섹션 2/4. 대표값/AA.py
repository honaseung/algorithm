import sys
#sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

#파이썬 특성상 라운드는 그냥 사용하면 안된다.
#라운드 하려는 값이 정확히 x.5 로 끝난다면 up 이 아닌 down 이 된다.
#따라서 라운드 할때는 반드시 라운드 하려는 값에 0.5 를 더한 뒤 int 로 변환한다.
avg = int((sum(arr) / N) + 0.5)
#최소값을 구하기 위해서 우선 최대값을 심어준 뒤 비교해가면서 최소값을 새로 할당해준다.
min = float('inf')

for i, x in enumerate(arr) :
    gap = abs(avg - x)
    if gap < min :
        min = gap
        score = x
        index = i + 1
    elif gap == min :
        #> 이면 스코어가 같아도 앞번호
        #>= 이면 스코어가 같으면 뒷번호
        if x > score :
            score = x
            index = i + 1
print(avg, index)