name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hour_dict = dict()
for line in handle:
    line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    time = words[5]
    hour = time[0:2]
    hours = hour.split()
    for hour in hours:
        hour_dict[hour] = hour_dict.get(hour, 0) + 1

t = sorted(hour_dict.items())
for k, v in t:
    print(k,v)
