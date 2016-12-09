import sys

comf = sys.argv[1]
f = open('courses.txt','r')
lines = f.readlines()
course_count = 0
total_credit = 0

for line in lines:
    items = line.strip().split(',')
    if line.startswith(comf):
       print(line,end="")
       total_credit += int(items[1])
print("Total:"+" "+str(total_credit)+" credits")

