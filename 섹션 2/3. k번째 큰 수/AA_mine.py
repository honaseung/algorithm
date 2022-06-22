import sys
#sys.stdin = open("input.txt")

#리스트에서 얻을 수 있는 중복없는 모든 합계를 구한다.
#
def sumSet(arr: list = []) :
    m, n, l = 0, 1, 2
    '''
    리스트에서 얻을 수 있는 중복없는 모든 합계를 구하지 않고
    원하는 정답만을 가장 빠르게 찾기 위해 새로운 리스트를 만들어
    정렬한 후에 이용하기위한 구문 arr 대신 sortedArr 을 이용하면 된다.
    sortedArr = arr.copy()
    sortedArr.sort(reverse = True)
    '''
    resultSet = set()
    while True:
        #sum = sortedArr[m] + sortedArr[n] + sortedArr[l]
        sum = arr[m] + arr[n] + arr[l]
        resultSet.add(sum)
        '''
        리스트에서 얻을 수 있는 중복없는 모든 합계를 구하지 않고
        원하는 정답만을 가장 빠르게 찾기 위한 구문이나 의도된 방향
        으로 작동 하지 않음
        if K == len(resultSet) :
            return sum
        '''
        l = l + 1
        if l == len(arr) :
            n = n + 1
            l = n + 1
        if n == len(arr) - 1 :
            m = m + 1
            n = m + 1
            l = n + 1
        if m == len(arr) - 2 :
            resultArr = list(resultSet)
            resultArr.sort(reverse = True)
            return resultArr

N, K = map(int, input().split())

arr = list(map(int, input().split()))

print(sumSet(arr)[K - 1])