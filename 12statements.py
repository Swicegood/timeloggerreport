def parityOf(int_type):
    parity = 0
    while (int_type):
        parity = ~parity
        int_type = int_type & (int_type - 1)
    return bool(parity)

statement = [False,False,False,False,False,False,False,False,False,False,False,False]
statement[0] = True
statement[1] = False
statement[2] = not(parityOf(statement[1:2]))
statement[3] = parityOf(statement[4:6])
statement[4] = parityOf(statement[1:3])
statement[5] != parityOf(statement[:2])
statement[6] = (statement[1] != statement[2])
statement[7] = parityOf(statement[4:6])
statement[8] = parityOf(statement[0:5])
statement[9] != parityOf(statement[10:11])
statement[10] = parityOf(statement[6:8])
statement[11] = parityOf(statement[8:11])