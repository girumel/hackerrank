#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = 0

    for i in student_marks[query_name]:
        total += i
    average = total / 3
    print(f"{average:.2f}")
