def MakeList(Separator,MyList):
    i = 0
    def MakeItem():
        nonlocal i
        i=i+1
        return (str(i)+Separator+MyList[i-1])
    for item in MyList:
        print(MakeItem())

MakeList(". ", ["First", "Second", "Third"])