students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#print(grades[0])
#print(sum(grades[0]))
#print(len(grades[0]))
#print(sum(grades[0])/len(grades[0]))
pupil = sorted(students)
ball = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
diary = {pupil[0]: ball[0], pupil[1]: ball[1], pupil[2]: ball[2], pupil[3]: ball[3], pupil[4]: ball[4]}
print(diary)


