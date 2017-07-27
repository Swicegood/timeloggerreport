
file = open("C:\\Users\\jguru\\Google Drive\\Computer\\pyhon\\raw_data_ocr.txt", "r")
for unicode_line in file:
    filtered = unicode_line.translate({ord(c): None for c in '!@#$%^&*()_+-=[]{}\\|'})
    print(filtered)
