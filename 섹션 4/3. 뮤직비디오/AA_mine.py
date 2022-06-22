import sys
#sys.stdin = open('in1.txt')

#으으 머리 안돌아가.
#오늘은 여기까지만 하자.
#아래 함수 수정해야해.

#부산 내려가는 기차안에서 수정한 코드이다.
#포인터를 아주 그냥 가지고 노셨다.
#잘했다. 이번 코드 만족스럽다.
#그렇지만 아직 부족하다고 많이 느낀다.
#개인적으로 제일 부족한 부분은
#포인터의 마지막을 잡는 부분이라고 생각한다.
#나름 꽤 힘들었으니까.
#근데 문제가 이상한거 같다. 일단 강의를 보러 가자.

#강의에 오류가 있었던건 사실이지만
#내 경우와는 다르다.
#내 경우에서의 문제점은
#in1.txt 기준으로
#4장에 나눠 담으라고 했을때
#반드시 4장에 나눠 담을 수 있는 경우만을 생각했던거다.
#이를테면 1장에 나눠 담을 수 있는 용량 또한 4장에
#나눠담을 수 있기 때문에 일어난 문제이다.
#함수를 조금 수정해보자.
def countDVD(mLen: int) :
    cnt = lt = rt = 0
    #그냥 9 가 아니다.
    #9 는 변수로 들어온다.
    #while rt < 9 :
    while rt < N :
        slicedSum = sum(mLenList[lt : rt + 1])
        if slicedSum > mLen :
            lt = rt
            cnt += 1
        elif slicedSum == mLen :
            rt += 1
            lt = rt
            cnt += 1
        else :
            rt += 1
            if rt == N :
                cnt += 1
    return cnt
N, M = map(int, input().split())
mLenList = list(map(int, input().split()))

#기준점을 무엇으로 잡을것인가??
#DVD 장수로 잡을 것인가??
#아니면 DVD 장당의 용량으로 잡을 것인가??
#문제에서 요구하는 답은 DVD 장당의 용량이다.
#그렇기 때문에 여기서도 기준점은 DVD 장당의 용량으로 잡았다.

#모든 곡을 각각 한 DVD 에 담을 수 있는 가장 작은 DVD 용량이다.
s = max(mLenList)
#모든 곡을 전부 한 DVD 에 담을 수 있는 가장 큰 DVD 용량이다.
e = sum(mLenList)
res = 0
while s <= e :
    #앞선 문제와 마찬가지로 자연수 사이에서 중간값을 구한다.
    #idx 가 아니기때문에 0 을 고려하지 않은 상태로
    #중간값을 구해보는 계산을 해보길 권장한다.
    m = (s + e) // 2
    #센세가 했던대로 함수를 만들어서 해보자.
    cntDVD = countDVD(m)
    if cntDVD > M :
        s = m + 1
    #주의해야할것은 M 장 보다 적게 담을 수 있는것 또한
    #정답이 될 수 있다는 것이다.
    #왜 그런지는 라인 17 에서 자세히 상술해두었다.
    #그리고 여기만 수정하니까 잘된다. ㅋㅋ 똘똘해 ㅋㅋ
    #elif cntDVD < M :
    #    e = m - 1
    else :
        e = m - 1
        res = m
print(res)
    