#https://www.hackerrank.com/challenges/grading/submissions/code/339486306
def gradingStudents(grades):
    arr_new_grades = []
    for i in range(len(grades)):
        falta = 0
        if(grades[i] < 38):
            arr_new_grades.append(grades[i])
        elif(grades[i]%10>2 and grades[i]%10 <= 4):
            falta = 5 - grades[i]%10
            arr_new_grades.append(grades[i]+falta)
        elif(grades[i]%10 >7):
            falta = 10 - grades[i]%10
            arr_new_grades.append(grades[i]+falta)
        else:
            arr_new_grades.append(grades[i])
    return arr_new_grades