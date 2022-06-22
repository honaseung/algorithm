import sys
#sys.stdin = open('input.txt')

n, m = map(int, input().split())
a = list(map(int, input().split()))

#초기값 세팅
#초기값을 어떻게 잡느냐에 따라서
#코드 내용이 완전 달라진다.
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True :
    #연속된 합이 원하는 값보다 작을 동안 아래 코드 진입
    if tot < m :
        #오른쪽 포인터가 리스트의 마지막 요소에
        #접근할때 까지 실행
        #즉, rt = n - 1 까지 아래 코드를 탄다.
        if rt < n :
            tot += a[rt]
            rt += 1
        #rt = n 이 되었을때 아래 코드 진입
        else :
            break
    elif tot == m :
        cnt += 1
        #빼는 방법은 생각도 못하긴했다.
        #음 좋은 방법이긴한데
        #뭔가 마음에 안든다.
        tot -= a[lt]
        lt += 1
    else :
        tot -= a[lt]
        lt += 1
print(cnt)
#rt 에 대해서 신경 쓸 일이 없는데??
#뭔가 낚인 기분인데
#내 방식대로 완성 시키겠어!!