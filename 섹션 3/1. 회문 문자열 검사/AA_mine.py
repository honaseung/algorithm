import sys
#sys.stdin = open('input.txt')

#문자열을 바로 리턴해주는 방식도 있어서
#작업은 하였고 100 점이 나왔으나 다른 방식해보고 싶어서
#코드 수정해봄 ㅋㅋ
#왜냐고?? is~ 니까 bool 값 리턴하는게 정석같이 느껴져서 그랭
def isReverEqual(str: str) :
    #res = ''
    #초기값은 False 가 좋겠다.
    #왜냐면 True 가 되는 경우보다 False 가 되는 경우가 많으니까
    res = False
    #문제에서 당연히 대소문자를 구분하지 않는다기에 넣어주었지만
    #사실 대소문자를 구분한다라는 문구가 있는 경우가 아닌이상
    #대소문자를 구분해주는게 더 좋다고 생각한다.
    tarStr = str.upper()
    #가운데 index 까지 접근 가능하도록
    #그냥 // 2 였다면 // 2 - 1 까지만 돌기에
    #// 2 + 1 을 해줘서 // 2 까지 돌도록 작성
    #len(tarStr) 을 두번 이상 사용하니까 변수화 해도 좋다.
    for i in range(len(tarStr) // 2 + 1) :
        #이 문제에서는 for 문을 한번 더 돌리거나 할 필요없이
        #서로 매칭 되는 단어 끼리만 비교하여
        #다르다면 결과 문자열을 변경 하고 바로 for 문을 종료

        #오호 진기한 사실
        #인덱스를 음수값으로 둠으로써 뒤에서부터 접근가능!
        #단 이럴경우 인덱스는 -1 부터 시작
        #즉, 첫번째 index 는 0 이지만 마지막 index 는 -1 이다.
        #이러면 len(tarStr) 이 필요없지
        if tarStr[i] != tarStr[len(tarStr) - i - 1] :
            #res = 'NO'
            break
    else :
        res = True
    return res

N = int(input())
for i in range(N) :    
    #읽을때는 원래 문자열로 읽고 여기서는
    #문자열 하나씩 읽기때문에 그냥 input() 으로도 충분하다.
    str = input()
    #이거 자주 안써서 또 까먹을뻔함
    #포멧 표현식 기억해두자
    #참고로 %s 는 문자열 %d 는 숫자(아마도 실수??)
    #일부러 함수 구조를 바꿔 봤성
    #print('#%d %s' %(i + 1, isReverEqual(str)))

    if isReverEqual(str) :
        print('#%d %s' %(i + 1, 'YES'))
    else :
        print('#%d %s' %(i + 1, 'NO'))
