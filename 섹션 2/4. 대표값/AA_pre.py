#최솟값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]
#가장 큰 값 할당
arrMin = float('inf')
for x in arr :
    #경우에 따라서 < 가 아닌 <= 를 사용해야할 수도 있다.
    #< 이냐 <= 이냐 에 따라서 인덱스가 달라지기 때문이다.
    #같은 값일 경우 나중값을 선택하라는 경우가 있을수가 있다.
    if x < arrMin :
        arrMin = x

