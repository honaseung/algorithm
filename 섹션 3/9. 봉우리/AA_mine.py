import sys
#sys.stdin = open('input.txt')

N = int(input())
#ㅋㅋ 너 또 옛날 명명규칙 쓸라했지??
#적응해 ~~
gridIntList = [list(map(int, input().split())) for _ in range(N)]

#발상1
#이차원 리스트??
#ㅈ 까
#일차원 리스트로도 충분히 가능해
#어찌보면 수 많은 이차원 리스트 문제들이
#일차원 리스트로도 가능해
#왜냐하면 인덱스 컨트롤만 잘해주면 되는 문제거든
#그리고 이 문제에서도 들어오는 요소들 각각
#즉, 각 리스트의 길이들이 항상 N 으로 동일하거든??
#그러니까 다음 요소(리스트)에 접근하고 싶으면 그저
#idx 를 N 만큼 늘려주면 될 뿐이야.
#이 발상이 좋다고 생각하는 이유는
#idx 를 하나 더 컨트롤할 필요가 없어져.
#그러니까 원래는 3 개를 컨트롤해야하는데
#2 개만 컨트롤해도 되는거지.

#ㅇㅋ 해보자.

#야 라인 9 나와봐.
#뒈지고 싶냐??
#굳이 이차원 리스트를 쓸 수 있는데
#깝치지마라. 진짜 뒤진다.
#아니 시부레 생각을혀봐.
#이문제에서 봉우리 찾을때
#좌우 살핀다 캣냐 안캣냐??
#ㅋㅋㅋㅋ 새기야 이차원 찢어서
#일차원 만들면 일이 너무 커져.
#발상1?? ㅇㅈㄹ ㅋㅋ.
#너 진짜 내 눈에 띄면 뒤져 진짜. ㅋㅋ

#0 으로만 이루어진 리스트가 둘러싸고 있다고 가정한다는게
#봉우리를 구하기위해 상하좌우를 비교할 수 없는 예외사항
#자체를 배제하겠다는 의미가 담겨있다.
#다만 중요한건
#진짜로 0으로 감싸?? ㅋㅋ
#물론 진짜로 감싸면 감싸는것만 불편하지.
#나머지 코드들은 정말 편해져.
#당연하게도 idx 컨트롤만 조금 주의하면
#에러는 발생안하게 되니까!!
#모르겠으면 강의 보기 전이니까
#감싸서 한번 풀고 안감싸서 한번 풀어보시든가. ㅋㅋ

warppedGridIntList = gridIntList.copy()
#바본가??
#아니;; 킹니;;
#0 우겨넣기 전 작업인데 왜 1 부터 N - 2 까지
#접근함;;
#for i in range(1, N - 1) :
for i in range(N) :
    #뭐?? i == 0??
    #굳이??
    #걍 한번만 해주면 되잖아.

    #라인 52 미쳤냐??
    #한번만 해줄라 그런거자너.

    #라인 57 바보야.
    #라인 52 말은 그걸 굳이 반복문 안에서??
    #라는 말이자너.
    #아마도 그럴껄??
    #if i == 0 : 
    
    warppedGridIntList[i].insert(0, 0)
    warppedGridIntList[i].append(0)

#안 훌륭한데?? ㅋㅋ
#야 다른 리스트에 0 을 추가했으면
#[0] * N 맞아?? ㅋㅋ
#갯 수 제대로 세라 쫌!!
warppedGridIntList.insert(0, [0] * (N + 2))
warppedGridIntList.append([0] * (N + 2))

cnt = 0
#range 를 잡을 때 주의 사항
#빠짐없이 돌기 위해서는 어디서부터
#어디까지인지에 대해서 분명하게 잡고
#range 를 잡자
#헷갈리면 가장 큰 idx 의 최종값을
#range 끝값에 대입해보자.
#여기서는 i + 2 가 가장 큰 idx 이지.
#그리고 위에서 0 으로 감싸주었다는 사실을 명심하자!!
#그러니까 당연하게도 range 의 범위도 idx 의 접근도 전부
#달라진다!!
for i in range(N) :
    upRow = warppedGridIntList[i]
    targetRow = warppedGridIntList[i + 1]
    downRow = warppedGridIntList[i + 2]
    #이 녀석이 N 인 이유
    #targetRow 의 len 이 N 이니까!!
    #위와 동일하게
    #접근하려는 가장 큰 idx 의 값이 j + 2 이니까.
    for j in range(N) :
        uCol = upRow[j + 1]
        dCol = downRow[j + 1]
        lCol = targetRow[j]
        rCol = targetRow[j + 2]

        tCol = targetRow[j + 1]

        #단순히 max 치면 안될거 같아.
        #만약 tCol 과 다른 col 의 값이 같다고쳐도
        #아래는 True 가 되어버려.
        #if tCol == max(uCol, dCol, lCol, rCol, tCol)

        if tCol > uCol and tCol > dCol and tCol > lCol and tCol > rCol :
            cnt += 1
print(cnt)
#ㅋㅋ 훌륭하도다!!

#이건 wrap 없이 해보는거얌.
#for i in range(N) :
#    gridIntList
#ㅋㅋ 갑자기 해볼려는데 너무 막막하다.
#구냥 하지말장 ㅎㅎ.
#중요한 사실은 때로는 문제에서 주어진 조건을 변형 시킴으로써
#문제를 좀 더 수월하게 풀 수 있다는 사실이다. 그것만 알고 가자.