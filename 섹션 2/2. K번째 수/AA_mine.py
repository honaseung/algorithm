import sys
sys.stdin = open("input.txt")

T = int(input())

def sortAndFind(arr, s, e, k) :
    #슬라이스는 오리진 리스트를 변경하지 않는다.
    slicedArr = arr[s - 1 : e]
    #리스트 요소의 타입을 항상 주의하자
    #리스트 요소가 숫자일때와 문자일때의 정렬은 완전 다르다.
    #sort 는 오리진 리스트를 변경한다.
    slicedArr.sort()
    return slicedArr[k - 1]

for i in range(T) :
    #맵 형태로 떨어지는걸 갯수에 맞게 초기화 해주니 요소 하나하나씩 값으로 입력되네.
    N, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print("#", i + 1, " ", sortAndFind(arr, s, e, k), sep = "")