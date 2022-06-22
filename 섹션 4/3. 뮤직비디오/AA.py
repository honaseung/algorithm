import sys
#sys.stdin = open('input.txt')

'''
문제에서 주어진 input.txt 기준
DVD 한장의 용량을 기준으로 포인터를 만든다.
lt = 1
rt = 45
로 잡는다. 1은 가장 작은 용량을 의미하고
45 는 모든 곡을 담을 수 있는 용량을 의미하는데
모든 곡을 한장의 DVD 에 담을 수 있다는 의미는
나누어 담는다면 충분히 3장에 담을 수 도 있음을 의미하기에
모든 곡의 용량을 합친 45 가 최대값인 rt 가 된다.
'''

def Count(capacity: int) :
    #이부분은 나랑 다르게 시작부터 1 로 잡고 간다.
    cnt = 1
    sum = 0
    #아무래도 전역변수인 Music 을 변형시키지 않기 때문에
    #그냥 사용해도 문제가 없어보인다.
    for x in Music :
        #일단 sum 에 저장하지 않고 미리 더하기만 해보기
        if sum + x  > capacity :
            cnt += 1
            #초과되었으니 새로운 DVD 에 담아야하는데
            #초기화를 꼭 0 으로 시킬 필요가 없다.
            #그냥 바로 다음 곡을 담아 버리면 된다.
            sum = x
        else :
            sum += x
    return cnt
#굉장히 짧네?? ㅋㅋ
    
n, m = map(int, input().split())
Music = list(map(int, input().split()))
#라인 5 에서 설명중
#근데 솔직히 그냥 1 로 두는건 난 비추이다.
#경우에 따라서는 단 한곡도 담지 못할수도 있는데
#굳이 시작부터 검색 범위를 늘릴 필요가 있을까 싶당.
lt = 1
#에라이 ㅋㅋㅋㅋ 내 말이 맞네.
#lt = 1 이라면 범위가 더 늘어나는 수준이 아니라
#그냥 범위가 잘못된거였네.
maxx = max(Music)
rt = sum(Music)
res = 0
#lt 와 rt 가 같다면 마지막 검색임을 의미
while lt <= rt :
    mid = (lt + rt) // 2
    #예를들어 3 장에 담을건데
    #2 장만에 담을 수 있다면
    #당연하게도 3 장에도 담을 수 있기때문!!
    #하지만 그냥 이대로두면 오류가 있음!!
    #if Count(mid) <= m :
    #담을수 있는지 체크하려는 용량이
    #곡들 리스트중에서 제일 용량이 큰 곡보다
    #더 큰 용량인지 체크해줘야한다고한다.
    if mid >= maxx and Count(mid) <= m :
        res = mid
        #더 작은 용량으로 범위 좁히기
        rt = mid - 1
    else :
        #더 큰 용량으로 범위 좁히기
        lt = mid + 1
print(res)
