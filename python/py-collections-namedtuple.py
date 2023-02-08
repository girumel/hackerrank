from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
total = 0
for i in range(n):
    row = input().split()
    s = Student(row[0], row[1], row[2], row[3])
    total += int(s.MARKS)
print('{:.2f}'.format(total / n))