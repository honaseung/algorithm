import sys
#sys.stdin = open('in5.txt')

N = int(input())
gridArr = []
for _ in range(N) :
    gridArr.append(list(map(int, input().split())))

#내장 함수를 이용한 합 구하기
def getMaxRowSum(grid: list) :
    maxSum = float('-inf')
    for x in grid :
        maxSum = max(sum(x), maxSum)
    return maxSum

#이중 for 문을 이용한 합 구하기
def getMaxColSum(grid: list) :
    maxSum = float('-inf')
    for i in range(len(grid)) :
        sum = 0
        for j in range(len(grid)) :
            sum += grid[j][i]
        maxSum = max(sum, maxSum)
    return maxSum

#역 idx 를 이용한 합 구하기
def getMaxDiagonalSum(grid: list) :
    sum1 = 0
    sum2 = 0
    for i in range(len(grid)) :
        sum1 += grid[i][i]
        sum2 += grid[i][-(i + 1)]
    return max(sum1, sum2)

#포인터 연습 좀 할라했는데 솔직히 이건 좀 너무 시시해서;;
#그냥 하나 덧붙여보자
#포인터는 내 생각에는 연속된 idx 에 접근할때 주로 사용할거 같아.
#음 그냥 내 생각이야.
#그렇다고 연속된 idx 를 사용하지 않는 문제라고 해서
#무조건 포인터를 배제하고 접근할건 당연히 아니야!!

print(
    max(getMaxRowSum(gridArr)
        , getMaxColSum(gridArr)
        , getMaxDiagonalSum(gridArr)
    )
)
#이거 뭐야??
#왜 금방 풀리고 시간 제한에도 안걸려??
#나 너무 무서워 ~~
#너무 쉬워서 ㅋㅋ

#범용성 있는 코드를 짜는건 훌륭해.
#칭찬받을만해.
#다만 알고리즘 짤때에는 아닐수도 있다는거야.
#항상 생각하면서 문제에 접근하자.