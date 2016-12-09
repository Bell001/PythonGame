f = open('courses.txt','r')
lines = f.readlines()
credits = {}

for line in lines:
        items = line.strip().split(',')
        credits[items[0]] = int(items[1])

num=0

for c in credits:
        num += credits[c]
gpa = num/len(credits)
print("%.3f" %(gpa,))
