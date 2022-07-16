import sys
#sys.stdin = open('input.txt')

#You can use 'greedy' when if given input isn't sorted but sorting has meaning.

'''
test1 = sorted(list(input()))
test2 = sorted(list(input()))
if test1 == test2 :
    print("YES")
else :
    print("NO")
'''

str1 = input()
str2 = input()

dic1 = {}
dic2 = {}

for x in str1 :
    try :
        dic1[x] += 1
    except :
        dic1[x] = 1

for x in str2 :
    try :
        dic2[x] += 1
    except :
        dic2[x] = 1

if dic1 == dic2 :
    print("YES")
else :
    print("NO")