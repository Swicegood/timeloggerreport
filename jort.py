def JortSort (x):
    y = x
    if x == sorted(y):
        return True
    else:
        return False

mylist = ["dog", "cat", "apple", "pear", "bird", "grape"]
if JortSort(mylist):
    print ("Yes! List is sorted.")
else:
    print("No, list is not sorted!")

mylist = ["apple", "bird", "cat", "dog", "grape", "pear"]
if JortSort(mylist):
    print ("Yes! List is sorted.")
else:
    print("No, list is not sorted!")

word = "Californina"
print(sorted(word))
