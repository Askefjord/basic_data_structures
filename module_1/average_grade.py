grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_stud = sorted(students)
diary = {}

for i in range(len(list_stud)):
    grades[i] = sum(grades[i]) / len(grades[i])
    diary[list_stud[i]] = grades[i]

print(diary)

