'''
this file is not finished. I made this long time ago.
so i can't remeber what i was thinking.
i try to understand what i was doing.
and i was such good idea.
evenif it's wrong, still good.
solve the problem with dictionary?!
it's really a good way to visulization.
'''

var = {
    1: {
        2: {
            4: {

            },
            5: {

            }
        },
        3: {
            6: {

            },
            7: {

            }
        }
    }
}

def frontRounds(x: dict) :
    key = list(x.keys())
    try :
        print(key[0], end = ' ')
        frontRounds(x[key[0]])
        print(key[1], end = ' ')
        frontRounds(x[key[1]])
    except :
        return

'''
it's impossible to print parent once.
because this structure is going down till there is no node(occuring exception).
then back and print last parent. and go back to it's own parent's and go to another child.
another child do the same thing and go back to it's own parent's.
it means back to parent at least twice each subtree.
'''
def midRounds(x: dict, self) :
    key = list(x.keys())
    try :
        midRounds(x[key[0]], key[0])
        print(key[0], end = ' ')
        print(self, end = ' ')
        midRounds(x[key[1]], key[1])
        print(key[1], end = ' ')
    except :
        return

def rearRounds(x: dict) :
    key = list(x.keys())
    try :
        rearRounds(x[key[0]])
        print(key[0], end = ' ')
        rearRounds(x[key[1]])
        print(key[1], end = ' ')
    except :
        return

frontRounds(var)
print()
midRounds(var, list(var.keys())[0])
print()
rearRounds(var)

print()

dic1 = {'test': 0}
dic2 = {'test0': 0}

dic1.update({'test': 1})
dic1.update(test1 = 1, test2 = 2, test3 = 3)
dic1.update(dic2)

print(dic1)

