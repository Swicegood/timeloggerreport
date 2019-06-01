def parityOf(int_type):
    parity = 0
    while (int_type):
        parity = ~parity
        int_type = int_type & (int_type - 1)
    return bool(parity)

statement = [False,False,False,False,False,False,False,False,False,False,False,False]
statementb = []
statementb = statement

while True:
    statement[0] = True
    statement[1] = False
    statement[2] = not(parityOf(sum(1<<i for i, b in enumerate(statement[1::2]) if b)))
    statement[3] = parityOf(sum(1<<i for i, b in enumerate(statement[4:6]) if b))
    statement[4] = parityOf(sum(1<<i for i, b in enumerate(statement[1:3]) if b))
    statement[5] = not(parityOf(sum(1<<i for i, b in enumerate(statement[:2]) if b)))
    statement[6] = (statement[1] != statement[2])
    statement[7] = parityOf(sum(1<<i for i, b in enumerate(statement[4:6]) if b))
    statement[8] = parityOf(sum(1<<i for i, b in enumerate(statement[0:5]) if b))
    statement[9] != parityOf(sum(1<<i for i, b in enumerate(statement[10:11]) if b))
    statement[10] = parityOf(sum(1<<i for i, b in enumerate(statement[6:8]) if b))
    statement[11] = parityOf(sum(1<<i for i, b in enumerate(statement[8:11]) if b))
    if sum(1<<i for i, b in enumerate(statement[8:11]) == statementb:
        break
    else:
        statementb = statement
print(statement)