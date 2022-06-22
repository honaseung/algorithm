import sys
#sys.stdin = open('input.txt')

n = int(input())
for i in range(n) :
    s = input()
    #들어온 문자 대문자화
    s = s.upper()
    size = len(s)
    for j in range(size // 2) :
        #오호 진기한 사실
        #인덱스를 음수값으로 둠으로써 뒤에서부터 접근가능!
        #단 이럴경우 인덱스는 -1 부터 시작
        #즉, 첫번째 index 는 0 이지만 마지막 index 는 -1 이다.
        if s[j] != s[-1 - j] :
            print('#%d NO' %(i + 1))
            break
    else :
        print('#%d YES' %(i + 1))
    
    #진짜 단순하게 짠 코드
    #이런것도 가능하구나
    #슬라이스 할때에는
    #[슬라이스시작 index : 슬라이스끝 index : 슬라이스스텝]
    #이런식인데
    #[::-1] 해버리면 뒤에서부터 전부 출력된다.
    #이런 것도 있다는걸 알아두자
    #센세왈 코테에서 이렇게 짜면 직접해보라고 한다고 하는데
    #흠...
    #if s == s[::-1] :
    #    print('#%d YES' %(i + 1))
    #else :
    #    print('#%d NO' %(i + 1))