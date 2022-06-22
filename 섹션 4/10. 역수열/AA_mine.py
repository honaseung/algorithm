import sys
#sys.stdin = open('input.txt')

#원래 수열의 역수열이 주어지면
#원래 수열을 출력하는 프로그램.

N = int(input())
reverseNumList = list(map(int, input().split()))
originNumList = [float('inf')] * N

#reverseNumList[i] 만큼 i 보다 큰 수가
#오도록 리스트를 만들면 된다.
#즉, 최대값을 갖는 새로운 리스트를 만들어서
#i 부터 N 까지 앞에서부터
#새로운 리스트의 값들과 비교하며
#i 보다 크면 reverseNumList[i] 를 하나씩 감소시켜서
#reverseNumList[i] 가 0 이 되는 지점에 값을 변경 시켜주는 방식이다.
#다만 이 문제의 방식은 reverseNumList[i] 가
#원래 0 인 지점을 처리하기가 곤란해진다는 점이다.
for i in range(len(reverseNumList)) :
    for j in range(len(originNumList)) :
        if reverseNumList[i] <= 0 :
            if originNumList[j] == float('inf') :
                originNumList[j] = i + 1
                break
        if originNumList[j] > i + 1 :
            reverseNumList[i] -= 1

#흐음 코드를 크게 수정하지 않았는데
#변경된 점이라면 출력 방식의 변경 뿐이다.
#결국 처음 풀이가 틀린 이유는 고작 출력 방식 때문이라는건가...
for x in originNumList :
    print(x, end = " ")

#좋은 발상이고 좋은 풀이야.
#다만 정답도 틀렸고 또 그리디에 맞지않아.
#분명 어딘가에선 써먹을 수 있을정도로 괜찮아.
#하지만 여기서는 아니야. 이 문제는 그리디로 풀자.
#물론 이 문제 또한 그리디가 아니어도 풀 수 있을거야.
#그래도 지금은 그리디 연습중이니까.

#센세도 딱히 그리디를 활용하진않았다.
#단지 이 문제에서의 접근법(발상)을 그리디로 봐야하는 것 같다.
#그리고 그렇게 생각하면 나의 발상이 맞았다.
#다만 코드를 수정해야겠지.