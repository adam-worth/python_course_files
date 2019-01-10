fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lines = line.rstrip()
    words = lines.split()
    for word in words:
        if word not in lst:
            lst.append(word)
            lst.sort()
print(lst)
