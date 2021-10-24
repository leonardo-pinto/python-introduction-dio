import shutil

## read grade from a file and calculates the mean value for each student

def mean_grades(filename):
    file = open('grades.txt', 'r')
    grades = file.read()
    grades_separated_by_student = grades.split('\n')
    student_mean_grade = []
    for index in grades_separated_by_student:
        elements = index.split(',')
        student = elements[0] ## first element as the student name
        elements.pop(0) ##removes first element
        ## lambda function to calculate the list average
        ## transform strings to number
        mean_grade = lambda grades: sum([int(grade) for grade in grades])/len(grades)
        ## creates a dictionary to display the results
        student_mean_grade.append(({student: mean_grade(elements)}))
    new_file = open('mean_grades.txt', 'w')
    new_file.write(str(student_mean_grade))
    new_file.close()
    return student_mean_grade

# def write_file(content):
#     file = open('grades.txt', 'w')
#     file.write(content)
#     file.close()
#
# def update_file(content):
#     file = open('grades.txt', 'a')
#     file.write(content)
#     file.close()
# #
# def read_file(filename):
#     file = open(filename, 'r')
#     text = file.read()
#     print(text)
#
# def copy_file(filename):
#     shutil.copy(filename, '/home/leonardo/PycharmProjects/python-introduction-dio/09-crud-files/newFilePath')

def move_file(filename):
    shutil.move(filename, '/home/leonardo/PycharmProjects/python-introduction-dio/09-crud-files/newFilePath')

if __name__ == '__main__':
    # write_file('José, 10, 10, 7, 10\n')
    # update_file('Leonardo, 10, 8, 7, 8\n')
    # read_file('test.txt')
    # mean_grades_result = mean_grades('grades.txt')
    # print(mean_grades_result)
    # copy_file('test.txt')
    move_file('grades.txt')
