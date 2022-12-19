import sys
sys.stdin = open('3. 부분집합 구하기/input.txt')

def printsubset(number: int) :
    if (number == 0) :
        for idx in range(1, len(switchlist)) :
            if (switchlist[idx] == 0) :
                continue
            else :
                print(idx, end=' ')
        print()
    else :
        switchlist[number] = 1
        printsubset(number - 1)
        switchlist[number] = 0
        printsubset(number - 1)

if __name__ == '__main__' :
    target = int(input())
    switchlist = [0] * (target + 1)
    printsubset(target)