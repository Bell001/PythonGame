f = open('courses.txt','r')
lines = f.readlines()
course_count = 0
total_credit = 0
for line in lines:
    items = line.strip().split(',')
    total_credit += int(items[1])
print(total_credit)

