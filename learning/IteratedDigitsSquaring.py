from typing import Any, Union

n = 2
finalresult =0 
result = 0
ones = 0
eightynines = 0

for i in range(1000000):
    while (finalresult != 1 and finalresult != 89):
        result = 0
        for j in [int(d) for d in str(n)]:
            result: Union[int, Any] = (result + (j * j))
        n = result
        finalresult = result
    if result is 1:
        ones = ones + 1
        print(ones)
    if result is 89:
        eightynines = eightynines + 1
        print(eightynines)
    result = 0
    finalresult = 0
    n = i+3
print("Eightynines", eightynines)
print("Ones", ones+1)
