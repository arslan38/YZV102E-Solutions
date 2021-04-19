
def read_grades(filename):
    """
    Takes a string that stores filename
    Args: 
        filename: string
    Return:
        result: Tuple of names, mt1 scores, mt2 scores, final scores in dictionary type
    """
    import csv

    name, mt1, mt2, final = {},{},{},{}
    
    with open('grades.csv',newline='') as csv_file:
        spamreader = csv.reader(csv_file,delimiter=',')
        for row in spamreader:
          student_number = row[0]
          name[student_number]=row[1]
          if row[2]=='midterm1':mt1[student_number]=int(row[3])
          elif row[2]=='midterm2':mt2[student_number]=int(row[3])
          elif row[2]=='final':final[student_number]=int(row[3])

    return name, mt1, mt2, final


def convert(names, midterm1, midterm2, final):
    """
    Takes dictinaries and convert them to a list
    Args: 
        names: dictionary keys are numbers values are names
        midterm1: dictionary keys are numbers values are midterm1 scores
        midterm2: dictionary keys are numbers values are midterm2 scores
        final: dictionary keys are numbers values are final scores
    Return:
        lst: list of tuples. Tuples includes number, name, midterm1, midterm2, final scores
    """
    lst = []

    for i in names.keys():
        lst.append((i,names[i],midterm1[i],midterm2[i],final[i]))
 
    return lst


def calculate_exam_average(lst, exam):
    """
    Takes a list and exam type and returns the average of the exam.
    Args: 
        lst: list of tuples created in convert function
        exam: string speciefies the type of the exam
    Return:
        average: float that is the average of an exam specified with exam param.
    """

    average = 0.0

    for element in lst:
        number, name, mt1, mt2, final = element
        if exam=='midterm1': average+=mt1
        elif exam=='midterm2': average+=mt2
        elif exam=='final': average+=final

    average /= len(lst)

    return average


def find_passing_students(lst):
    """
    Takes a list created in convert function. Students can pass if the mt1*0.3 + mt2*0.3 + final*0.4 > 60.
    Args: 
        lst: list of tuples created in convert function
    Return:
        student_names: list of stringss that stores the passing students' names.
    """
    
    student_names =[]

    for element in lst:
        number, name, mt1, mt2, final = element
        cumulative_grade = (0.3)*mt1 + (0.3)*mt2 + (0.4)*final
        if cumulative_grade>60:
            student_names.append(name)

    return student_names



def manipulate(filename, lst):
    """
    Takes a string that stores filename and a list created in convert function
    Args: 
        filename: string
        lst: list of tuples created in convert function
    Return:
        result: Tuple of names, mt1 scores, mt2 scores, final scores in dictionary type
    """
    result = []

    import csv

    for i in range(len(lst)):
        number, name, mt1, mt2, final = lst[i]
        with open(filename,newline='') as csv_file:
            spamreader = csv.reader(csv_file,delimiter=',')
            for row in spamreader:
                student_number,exam,grade = row[0],row[1],int(row[2])
                if student_number==number:
                    if exam=='midterm1': mt1=grade
                    elif exam=='midterm2': mt2=grade
                    elif exam=='final': final=grade

            
        result.append((number, name, mt1, mt2, final))

                
    return result
    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    names, midterm1, midterm2, final = read_grades("grades.csv")
    lst = convert(names, midterm1, midterm2, final)
    print(lst)
    print("midterm1: ", calculate_exam_average(lst, "midterm1"))
    print("midterm2: ", calculate_exam_average(lst, "midterm2"))
    print("final: ", calculate_exam_average(lst, "midterm2"))
    print(find_passing_students(lst))
    lst = manipulate("edit.csv", lst)
    print("midterm1: ", calculate_exam_average(lst, "midterm1"))
    print("midterm2: ", calculate_exam_average(lst, "midterm2"))
    print("final: ", calculate_exam_average(lst, "midterm2"))
    print(find_passing_students(lst))

    
