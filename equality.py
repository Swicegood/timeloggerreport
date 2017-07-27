
def is_winner(myslice):
        if myslice[0].islower(): return False
        if myslice[1].islower(): return False
        if myslice[2].islower(): return False
        if myslice[4].islower(): return False
        if myslice[5].islower(): return False
        if myslice[6].islower(): return False
        if myslice[3].isupper(): return False
        return True


message = ""

file = open("C:\\Users\\jguru\\Google Drive\\Computer\\pyhon\\equality.txt", "r")
for line in file:
    for i in range (0,len(line)-7):
        if is_winner(line[i:i+7]):
            if i == 0:
                if  line[i+8].islower():
                    print(line[i+3])
                    message = message + line[i+3]
            if  i == len(line)-7:
                if  line[i-1].islower():
                    print(line[i+3])         
                    message = message + line[i+3]
            else:
                if line[i-1].islower() and line[i+8].islower():
                     print(line[i+3])         
                     message = message + line[i+3]
print(message)


#print(m)
