import sys
#sys.stdin = open('input.txt')

N = int(input())

arr = list(map(int, input().split()))

def findRprsVal(avg: int = 0, arr: list = []) :
    sortedArr = sorted(arr, key = lambda x: abs(avg - x))
    
    #min 함수는 비교값이 있어야지 작동하는데 abs 함수는 리턴값이 하나라서 비교할 대상 없으니 에러가 나지.
    #sortedArr.sort(key = lambda x: min(abs(avg - x)))

    if abs(sortedArr[0] - avg) == abs(sortedArr[1] - avg) :
        return max(sortedArr[0], sortedArr[1])
    else :
        return sortedArr[0]

#파이썬 특성상 라운드는 그냥 사용하면 안된다.
#라운드 하려는 값이 정확히 x.5 로 끝난다면 up 이 아닌 down 이 된다.
#따라서 라운드 할때는 반드시 라운드 하려는 값에 0.5 를 더한 뒤 int 로 변환한다.
avg = int((sum(arr) / len(arr)) + 0.5)

rprsVal = findRprsVal(avg, arr)

print("%d %d" %(avg, arr.index(rprsVal) + 1))
