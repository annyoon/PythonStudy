n = int(input())
grades = []

for i in range(n):
    grades.append(list(input().split()))
    
    grades[i][1] = int(grades[i][1])
    grades[i][2] = int(grades[i][2])
    grades[i][3] = int(grades[i][3])
    
grades.sort(key = lambda grade: (-grade[1], grade[2], -grade[3], grade[0]))

for j in range(n):
    print(grades[j][0])
