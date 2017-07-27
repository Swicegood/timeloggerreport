file = open("C:\\Users\\jguru\\Google Drive\\Computer\\pyhon\\unixdict.txt", "r")
for word in file:
    if list(word.rstrip()) == sorted(word.rstrip()):
        if len(word)-1 >= 6:   
            print(word)