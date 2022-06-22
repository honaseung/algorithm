import sys
#sys.stdin = open('in5.txt')

#문제랑 관계없는 상식
#파이선에서는 문자열 대소 비교가 가능하다.
#여기서 이루어지는 대소 비교는 알파벳 순이며
#대, 소문자 를 비교시에는 대문자가 항상
#소문자 보다 앞서기 때문에 유의하자
#또한 == 연산자를 사용하는데
#문자열 객체가 값을 들고 있어서 가능한지
#혹은 주소를 비교해주는데 진짜 그냥 같은건지는
#아직 모르겠다. 아마도 내 생각에는 지원하는 함수가
#따로 있을듯하다. 다른 많은 언어들이 그렇게 하는데에는
#이유가 있기 때문이니까.(내 생각에는 오리지널 값을 유지하기 위함)

def calPrize(diceNumArr: list) :
    #여기서의 발상은 이러하다.
    #문제에서는 단순히 3 번 던지기 때문에 이렇게까지 할 필요는 없다.
    #다만 내가 하고 싶은것은 좀 더 범용성 있는 코드가 되길 바라기에
    #아래처럼 작업하였다.
    #1) 숫자가 몇 번 등장하는지 세기 위해서 편한 방법은
    #숫자를 정렬하여서 같은 숫자들끼리 모아 두는 것이다.
    #컴퓨터가 아닌 사람이 작업한다고 하여도 이런 방식으로 작업할 것이다.
    #다만 정렬하는 작업이 한번 더 요구되기는 한다.
    #2) 그 다음에는 해당 숫자가 몇 번 등장하는지를 세는 방법이다.
    #1 개 2 개 3 개 야 쉽게 세겠지만 그 수가 만약 엄청 크다면??
    #그렇다면 인덱스를 활용하여 갯 수를 구할 수 있을것이다.
    #해당 숫자가 마지막으로 등장하는 index 에서 처음 등장하는 index 를 빼고
    #1 을 더해 준다면 해당 숫자가 몇 번 등장하는지를 알 수가 있다.
    #단순히 보기 편하기 위한 sort 가 아니다. 이렇게 추진력을 얻기 위함이었따!!
    
    #다만 그래서 마지막으로 등장하는 index 는 어떻게 구하느냐??
    #파이선에는 rfind 라는 함수가 존재한다. 단! 문자열 한정으로 존재한다.
    price = 0
    cnt = 0
    maxCnt = float('-inf')
    maxCntNum = 0
    #숫자만 들어오기에 가능
    #문자열만 들어와도 가능할거같은데
    #만약 숫자와 문자가 섞인다면 불가능할 것 같다.

    #sortedDiceNumStr = diceNumArr
    #sort 는 리턴값이 없다!!(None) 명심!!
    #sortedDiceNumStr = str(sortedDiceNumStr.sort(reverse = True))

    #아래방식으로 한다면
    #리스트가 쌩으로 문자열이된다.
    #따라서 ['6','2','5'] 이렇게 통으로 되어 버린다.
    #sortedDiceNumStr = str(sorted(diceNumArr, reverse = True))

    #toString 같은게 없을까
    #''.join 이면 끝 ㅋㅋ
    #근데 ''.join 은 뭔가 야매같아 힝
    #더 좋은게 있을까??
    #파이선에서 정식으로 지원하는 함수로
    sortedDiceNumStr = ''.join(sorted(diceNumArr, reverse = True))
    for x in sortedDiceNumStr :
        cnt = sortedDiceNumStr.rfind(x) - sortedDiceNumStr.index(x) + 1
        if cnt > maxCnt :
            maxCnt = cnt
            #이녀석을 int 화 시키지 않으면 계산을 할수가 엄써!!
            #난 곱셈 만나면 자동으로 형변환 해줄줄 알았찡.
            maxCntNum = int(x)
    #이거 어제 누가 maxCnt 가 아닌 cnt 로 해놨드라??
    if maxCnt == 3 :
        price = 10000   +   maxCntNum * 1000
    elif maxCnt == 2 :
        price = 1000    +   maxCntNum * 100
    #모든 숫자가 1 번씩만 등장했을 경우 위에 코드를 그대로 활용할 수 없다.
    #왜냐하면 cnt > max 일때만
    #maxCntNum 을 변경해주고 있는데
    #cnt > max 인 경우는 단 한번 존재하고
    #그 값은 문제에서 요구하는 제일 큰 값이 아닌 제일 작은 값이기 때문이다.
    elif maxCnt == 1 :
        #불가피하게도 위의 maxCntNum 을 활용하지 않았다.
        #코드를 조금 손 봐서 정렬을 오름차순이 아닌 내림차순으로 하거나
        #아니면 케이스를 따로 처리해야 할듯하지만 그냥 이런 접근 방식도 있음을 알아두자.
        price = 0        + maxCntNum * 100

        #그래도 짜세는 간결함이지.
        #내림차순 가볼게용~~
        #오이오이 왜 간다면서 가지 않았지?
        #price =         int(sortedDiceNumStr[-1]) * 100
        price =         maxCntNum * 100
    return price


maxPrice = float('-inf')
N = int(input())
for i in range(N) :
    #여기서 꼭 리스트로 받을 필요는 없잖아??
    #문자열로 받고 문자열로 다 처리해버려 걍 ㅋㅋ
    #ㅋㅋ 야 지가 정렬해서 쓸거람서 문자열로 만들면 어캄 ㅋㅋ
    #천천히 생각해.
    #그리고 바부야 diceNumArr 을 받고 바로 처리 해야지
    #덮어쓰고 덮어쓰고 한다음에 사용하면 어캄 ㅋㅋ
    #split 은 리턴이 리스트얌. 문자열 아님.
    #착각은 ㄴㄴ 해. 이녀석 이미 리스트야.
    #diceNumArr = list(input().split())

    #변수는 적을수록 좋지!!
    #max 와 maxPrice 가 공존할 이유는 없어.
    #그리고 여기다가 maxPrice 두면 한바쿠 돌때 마다 얘가 최소값이 되어 버려 ㅋㅋ
    #밖으로 나가있으라그래
    diceNumArr = input().split()
    price = calPrize(diceNumArr)
    if price > maxPrice :
        #최대값 변경해줭.
        #너 지금 시간 얼마 안남아서 급하지?? ㅋㅋ
        #빠른것보다 중요한건 정확한거야. 괜찮아.
        maxPrice = price
print(maxPrice)

#원인불명
#in4.txt 기준으로 2 가 두개 포함된 문자열이 전부 1 이 2 개로 들어온다?? 삐슝빠슝
#in5.txt 까지 돌려본 결과 이쉑 뭔데 지 멋대로 지가 읽고 싶은것만 읽냐 ㅋㅋ
#대충보니 한 인덱스 3 개씩 점프하는듯??
#처리해!!
#아주 그냥 죽여버려
#나중에...
#to be continued ...

#라인 113 캇트!
#인풋을 끊어서 오는게 아니라 디버깅을 찍은 위치에 접근하는게 띄엄띄엄 있던것일뿐
#역시 디버깅이야.