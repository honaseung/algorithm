import sys
#sys.stdin = open('in1.txt')

#sudokuList = [list(map(int, input().split())) for _ in range(9)]

#stepList 를 만들자!!
#센세가 강조한건 이유가 있으리라!!
#나도 해보는거야!!
#흠 근데 사실 이 문제에는
#그다지 적합한 풀이는 아닌거같긴한데 ㅋㅋ
#그래도 해보는거니까
#stepList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#stepList 의 요소가 될 값들에 대해서도 생각해보자.
#요소들을 idx 값으로서만 활용할게 아니라 val 값으로도
#활용가능하다!!
stepList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#라인 83 의 발상을 활용하면 stepList 가 필요없고
#set 자료형을 이용하여 처리할 수가 있다.
#훌륭한 발상인지에 대해서는 의문이 좀 남지만
#강의를 아직 안보았고 정답 체크도 안했으니까.
#아 물론 강의에서 훌륭하다고 해도 내 맘에 안들면
#그건 훌륭하지않지.

#사각형 검사
#가변값이 아니라서 그냥 fix 된 값
#for i in range(0, 3) : 
#    squareChk = sudokuList[i * 3]
#을 넣어도 되지만
#언제나 그렇듯이 연습용이다.
#뭐 사실 이것도 fix 되긴했지 ㅋㅋ
#for i in range(0, 9, 3) : 
#    squareChk = sudokuList[i]
#    #이거는 위의 주석에 들어있는 방식으로 표현!!
#    for j in range(0, 3) :
#        squareChkFst = squareChk[j * 3]
#크흠
#너무 시시하다고 생각했나??
#멍청하긴!! 각 사각형의 시작점에 접근하면
#끝날거라고 생각한건 너무나도 큰 오산이었다!!
#접근까지는 당근 가능하지만
#그 뒤로는 idx 컨트롤을 어떻게 해야할지
#감도 오는데(주석 쓰는데 갑자기 옴 ㅋㅋ: i, j 가 있자너)
#과연 이게 효율적이야??
#잘봐, 이미 한 행, 한 행 읽어오는중인데 굳이??
#굳이 다 읽고서 또 접근해서 체크??
#읽으면서 최소 행 체크는 가능하자너 ㅋㅋ
#효율 극대화 ON!!

#전역변수 꺼졍.
#res = 'YES'

#이 함수는 그저 체크를 해주기 위한 함수가 아니다.
#map 생성자에 같이 들어가서 input 요소 하나하나에
#변형을 주면서 map 형태로 만들어주기 위한 함수이다.
#하나의 함수에 여러 기능을 담는 일은 지양해야하겠지만
#여기서는 두가지 기능을 동시에 담당할 수 있도록 작업하였다.
def chkRow(targetList: list) :
    #targetList 에 있는 요소를 가지고
    #stepList 에 있는 요소의 갯수를 세면 안된다.
    #반드시 1 만 나오게 된다.
    #반대로 stepList 에 있는 요소들을 갖고
    #targetList 에 몇 개 있는지 세야된다.
    #for x in targetList :

    #라인 83 의 발상이다.
    #치워라. set 나가신다.
    #딱대.
    #for x in stepList :

    for x in targetList :
        #stepList 에 있는 요소를 카운트 하면 안된다.
        #반대로 stepList 에 있는 요소를 가지고
        #targetList 에 있는 요소를 카운트 해야한다.
        #if stepList.count(intEl) != 1 :
        #if targetList.count(intEl) != 1 :

        #라인 83 의 특권이다.
        #딱대.
        #망할 황영식
        #까먹었자너 ㅋㅋ
        #라인 85 의 사유로 주석처리
        #chkSet = set()
        #chkSet.add(intEl)
        
        #그런데 문제 발생
        #이렇게 체크를 하면 아무래도
        #res 는 반드시 NO 가 된다.
        #if len(chkSet) != 9 : 은 반드시
        #모든 요소가 set 에 들어갔을시에만
        #해줘야한다.
        #따라서 결론적으로는 이 함수에서
        #체크 기능을 분리해줘야 한다.
        #if len(chkSet) != 9 :
        #    res = 'NO'
        #변형 또는 작업을 거친 요소 하나하나를 반드시 return 해줘야
        #map 생성자에 넣기에 적합한 함수가 될 것이다.
        #추측이긴한데 내 생각엔 이게 맞다.

        #이 함수는 더이상 map 생성자에 넣어서 요소를
        #변형시키는 함수가 아니다.
        #해당 기능은 분리시켰고
        #여기서 하는 기능은 그저 Row Chk 만 남긴다.
        #return intEl
        chkSet = set()
        #뭐 그냥 Row 고
        #Row 는 뭐 그냥 리스트니까
        for y in x :
            chkSet.add(y)
        if len(chkSet) != 9 :
            res = 'NO'
            return res
    

def chkCol(targetList: list) :
    #정확히는 len(targetList) 가 아니다.
    #여기서는 targetList 가 정사각형 모양이기에 가능한것이다.
    #문제에서 주어지는 한 행의 길이에 대해서 주목해야한다.
    #for i in range(len(targetList)) :

    #문제에서 주어지는 정확한 값 9 로 픽스하였다.
    for i in range(9) :
        #위와 동일하다.
        #targetRow = targetList[i]
        #아니 위와는 다르다.
        #col 에 대한 것이기에 그저 targetList 한 요소에 접근하여
        #바로 리스트처럼 사용해버릴수가 없다.

        #칸은 총 9 칸 가능한 숫자는 1 ~ 9
        #중복 없이 칸을 채웠다는 말의 의미는 1 ~ 9 까지 다 있다는 의미이다.
        #여기서 중복이라는 단어에 포커스를 두어서 Set 자료를 사용하기로 하였다.
        #좋은 발상일지는 모르겠다. 조금 복잡한 발상이라는 생각이 들어서
        #그런데 이 발상이면 앞서 만들어두었던 stepList 도 변경 가능할 듯 싶다.
        #키워드는 중복에서 시작된 발상인데 쫌 괜찮아 보이긴한다.
        chkSet = set()
        for j in range(9) :
            #if stepList.count(targetRow[j]) != 1 :
            #if targetRow.count(stepList[j]) != 1 :
            #위의 주석과 동일하게 여기는 Row 가 아니라
            #Col 을 체크해주는 함수이고
            #Col 은 Row 와 다르게 변형없이는 리스트 취급을 할 수가 없다.
            #여기서는 변형을 통한 리스트 취급보다는 idx 컨트롤을 이용한다.
            #j 를 행으로 i 를 열로 둠으로써
            #이 반복문 안에서 행이동 열고정을 구현했다.
            chkSet.add(targetList[j][i])

        if len(chkSet) != 9 :
            res = 'NO'
            #chkRow 에서는 return 하지 않았다.
            #왜냐하면 chkRow 함수는
            #input 을 읽어오면서
            #map 형변환을 통한 처리를 하기위한 함수이기에
            #return 을 해버리면 모든 input 을 가져올 수 없었다.
            #하지만 여기 함수에서는 얘기가 다르기에 return 해주었다.
            return res

#아마도 이 부분이 이 문제의 핵심이겠지??
#idx 컨트롤 또는 포인터 컨트롤 연습하기에 적당한
#함수가 될것이다.
#근데 한 주 쉬었더니 flag, step 만드는건 알겠는데
#이전 문제에서 끝내주게 잘 활용했던게 기억안나.
#이거 끝나고 잠깐 복습 해보자.
def chkSquare(targetList: list) :
    #사각형의 x 좌표값
    for i in range(0, 9, 3) :
        #사각형의 y 좌표값
        for j in range(0, 9, 3) :
            chkSet = set()
            #i 와 j 를 이용하여 시작점을 잡고
            #그 시작점에서 사각형을 체크
            for k in range(i, i + 3) :
                for m in range(j, j + 3) :
                    chkSet.add(targetList[k][m])
            if len(chkSet) != 9 :
                res = 'NO'
                return res


#다시바다
sudokuList = []
#idx 를 쓸지 안쓸지 모르니 일단 넣어두고
for _ in range(9) :
    #set 자료형을 사용하기위해선 함수의 기능을
    #찢어야한다.
    #row = list(map(chkRowToMap, input().split()))
    row = list(map(int, input().split()))
    sudokuList.append(row)
if chkRow(sudokuList) != 'NO' :
    if chkCol(sudokuList) != 'NO' :
        if chkSquare(sudokuList) != 'NO' :
            print('YES')
        else :
            print('NO')
    else : 
        print('NO')
else : 
    print('NO')
#어째서 함수안에서 변경된
#res 는 반영되지 않는거지?
#그렇구나
#밑의 res 와 함수들의 res 는 색깔도 다르고
#스코프때문에 같은 res 라는 인식이 없는거야
#그래서 마우스 커서를 올리면 접근할 수 없다는
#메세지가 보이는거고
#하나 또 배운다.
#파이선에서 함수를 짤때에는
#전역변수 따위는 함수안에 접근할 수 없다.
#근데 잠만 자바스크립트에서도 그랬나??
#뭐 어찌되었건 전역변수를 남발하지 않는건
#음 좋은거 같아 적어도 지금 생각엔
#print(res)
    