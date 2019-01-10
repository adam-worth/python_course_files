import re
lst = list()
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum.txt"
handle = open(name)

for line in handle:
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    for numbers in nums:
        lst.append(numbers)


num_lst = list(map(int, lst))
sum = sum(num_lst)
print(sum)
