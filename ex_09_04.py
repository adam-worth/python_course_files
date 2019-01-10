name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
email_dict = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    lines = line.split()
    stuff = lines[1]
    emails = stuff.split()
    for email in emails:
        email_dict[email] = email_dict.get(email, 0) + 1

bigcount = None
bigword = None
for email, count in email_dict.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count

print(bigword, bigcount)
