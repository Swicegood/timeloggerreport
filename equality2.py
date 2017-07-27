import re

file = open("C:\\Users\\jguru\\Google Drive\\Computer\\pyhon\\equality.txt", "r")

message = ""

for line in file:
    m = re.search('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', line)
    if m != None:
        print("aha")
        message = message + m.group()
print(message)