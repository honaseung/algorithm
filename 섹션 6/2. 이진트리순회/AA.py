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

def midRounds(x: dict, self) :
    key = list(x.keys())
    try :
        midRounds(x[key[0]], key[0])
        print(key[0], end = ' ')
        midRounds(x[key[1]], key[1])
        #print(self, end = ' ')
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

