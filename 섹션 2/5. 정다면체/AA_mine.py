import sys
#sys.stdin = open('input.txt')

#N, M = map(int, input().split())

#사실 할 필요가 없다.
#리스트를 합치는 함수
#그냥 좀 더 좋은 코드를 만들순없을까 하다가 만들어봤다.
#다만 가변매개변수와 extend 만 알고 가자.
def concatDice(*nums: tuple) :
    newDice = list()
    for x in nums :
        dice = list(range(1, x + 1))
        newDice.extend(dice)
    return newDice

#주사위 두개를 합쳐놨기 때문에 6 + 6 같은 현상도 발생한다.
#포인터를 두개 두는것은 좋은데 이런 코드로는 컨트롤 할 수 없다.
#4 와 6 이면 포인터의 시작점을 하나는 0 하나는 5에 두고
#포인터의 끝지점을 하나는 3 하나는 9 에 둬야 하는 번거로움이 있다.
'''
dice = concatDice(N, M)
sumArr = []
for i in range(len(dice)) :
    for j in range(len(dice)) :
        sum = dice[i] + dice[j]
        sumArr.append(sum)
print(sumArr)
'''

#사실 할 필요가 없다.
#갯수를 세는 함수
#갯수를 세어 dictionary 로 반환한다.
#dictionary 는 JSON, MAP 과 유사해 보인다.
#try 와 except 구문을 반드시 알아두자.
def getCountDic(arr: list) :
    count = {}
    for x in arr :
        try: count[x] += 1
        except: count[x] = 1
    return count

#이번 문제와는 관계 없지만 그래도 잘 짠 코드라고 생각해서 넣어봤다.
#갯수가 많은 순으로 리스트화 되어 리턴된다.
#x 는 dictionary 의 key 값이며 value 는 바로 가져오지 못하는듯하다.
#물론 위의 코드들과 함께 사용해야한다.
'''
sorted(count, key = lambda x: count[x], reverse = True)
'''

#합계 리스트를 구하는 함수
#위의 함수를 토대로 만들었다.
def getSumArr(*nums: tuple) :
    sumArr = []
    for x in nums :
        for i in range(1, N + 1) :
            for j in range(1, M + 1) :
                sum = i + j
                sumArr.append(sum)
    return sumArr


#갯수가 제일 많은 값을 구하는 함수
#enumerate 를 사용하지 않아도 되지만 연습삼아 사용하였다.
#원리는 합의 리스트를 정렬하면 중복되는 요소값들이 있는데
#그 갯수가 산모양처럼 점점 늘어났다가 줄어든다는 점이다.
#ex) 
# [2, 2,
#  3, 3, 3, 3,
#  4, 4, 4, 4, 4, 4,
#  5, 5, 5, 5, 5, 5, 5, 5,
#  6, 6, 6, 6, 6, 6, 6, 6,
#  7, 7, 7, 7, 7, 7, 7, 7,
#  8, 8, 8, 8, 8, 8,
#  9, 9, 9, 9,
#  10, 10]
def getMaxCount(arr) :
    #그 어떤 값 보다도 무조건 작은값
    #어떤값과 비교하여서 최대값을 할당하고자 할때 사용한다.
    max = float('-inf')
    countNum = 0
    #갯수가 최대치를 찍었을때를 저장하는 변수
    #이 변수가 없으면 최초로 최대치를 찍는 값은 리스트에 저장되지 않는다.
    summit = 0
    sortedSumArr = sorted(arr)
    maxCountArr = []
    for i, x in enumerate(sortedSumArr) :
        try :
            countNum += 1
            if x != sortedSumArr[i + 1] :
                count = countNum
                countNum = 0
                if count > max :
                    max = count
                    #최대치를 찍었을 때마다 저장
                    summit = x
                elif count == max :
                    #직전에 최대치를 찍었던 값을 저장
                    if summit != 0 :
                        maxCountArr.append(summit)
                        #최대치를 찍었던 값 더이상 작동않하게
                        summit = 0
                    maxCountArr.append(x)
                else :
                    #최대치를 찍는 값이 하나일경우 작동
                    if summit != 0 :
                        maxCountArr.append(summit)
                        summit = 0
                    return maxCountArr
        #사실 원리상으로는 이곳을 지날일이 없다.
        #왜냐하면 count < max 인 경우가 원리상 반드시 존재하기 때문이다.
        except :
            return maxCountArr
    '''
    enumerate 사용안할시
    for i in range(len(sortedSumArr)) :
    maxCountArr = []
    try :
        countNum += 1
        if sortedSumArr[i] != sortedSumArr[i + 1] :
            count = countNum
            countNum = 0
            if count > max :
                max = count
            elif count == max :
                maxCountArr.append(sortedSumArr[i])
            else :
                return maxCountArr
    except :
        return maxCountArr
    '''

#이상으로 비효율적이지만 있어보이고싶은 코드를 짜봤습니다.
#for x in getMaxCount(getSumArr(N, M)) :
#    print(x, end = ' ')



#새로운 접근법이 강의 앞부분에 나왔다.
#인덱스를 마치 key 처럼 활용하여 합에 해당하는 인덱스의 값을 증가시킨다.
N, M = map(int, input().split())

#딕셔너리를 활용한 풀이
#트라이 익셑트를 활용했다.
count = {}
for i in range(1, N + 1) :
    for j in range(1, M + 1) :
        #i + j 값이 나올때마다 해당 카운트를 증가시킨다.
        #두개의 육면체에서 나올 수 있는 합은 한정되어있고 또 중복되기때문에
        #이런 풀이도 가능하다.
        #이것은 딕셔너리를 이용한 풀이 다만 아직 코드는 미완성
        try: count[i + j] += 1
        except: count[i + j] = 1
maxVal = max(list(count.values()))
for k, v in count.items() :
    if v == maxVal :
        print(k, end = " ")

#리스트를 활용한 풀이
#위의 풀이가 더 좋다. 왜냐하면
#리스트를 활용시에는 키 값을 제어할 수 없어서 반드시 키 값이 정수여야만 한다.
sumArr = [0] * 40
for i in range(1, N + 1) :
    for j in range(1, M + 1) :
        #i + j 값이 나올때마다 해당 카운트를 증가시킨다.
        #두개의 육면체에서 나올 수 있는 합은 한정되어있고 또 중복되기때문에
        #이런 풀이도 가능하다.
        sumArr[i + j] += 1
#인덱스를 활요해야하기때문에 튜플 사용
#튜플을 사용하려면 enumerate 를 사용
for i, x in enumerate(sumArr) :
    if x == max(sumArr) :
        print(i, end = " ")
