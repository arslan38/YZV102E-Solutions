
def read_grades(filename):
    """
    Takes a string that stores filename
    Args: 
        filename: string
    Return:
        result: Tuple of names, mt1 scores, mt2 scores, final scores in dictionary type
    """
    #  /$$$$$$$$ /$$$$$$ /$$       /$$
    # | $$_____/|_  $$_/| $$      | $$
    # | $$        | $$  | $$      | $$
    # | $$$$$     | $$  | $$      | $$
    # | $$__/     | $$  | $$      | $$
    # | $$        | $$  | $$      | $$
    # | $$       /$$$$$$| $$$$$$$$| $$$$$$$$
    # |__/      |______/|________/|________/
    name, mt1, mt2, final = {},{},{},{}

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
    #  /$$$$$$$$ /$$$$$$ /$$       /$$
    # | $$_____/|_  $$_/| $$      | $$
    # | $$        | $$  | $$      | $$
    # | $$$$$     | $$  | $$      | $$
    # | $$__/     | $$  | $$      | $$
    # | $$        | $$  | $$      | $$
    # | $$       /$$$$$$| $$$$$$$$| $$$$$$$$
    # |__/      |______/|________/|________/
    lst = []

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
    #  /$$$$$$$$ /$$$$$$ /$$       /$$
    # | $$_____/|_  $$_/| $$      | $$
    # | $$        | $$  | $$      | $$
    # | $$$$$     | $$  | $$      | $$
    # | $$__/     | $$  | $$      | $$
    # | $$        | $$  | $$      | $$
    # | $$       /$$$$$$| $$$$$$$$| $$$$$$$$
    # |__/      |______/|________/|________/
    average = 0.0

    return average


def find_passing_students(lst):
    """
    Takes a list created in convert function. Students can pass if the mt1*0.3 + mt2*0.3 + final*0.4 > 60.
    Args: 
        lst: list of tuples created in convert function
    Return:
        student_names: list of stringss that stores the passing students' names.
    """
    #  /$$$$$$$$ /$$$$$$ /$$       /$$
    # | $$_____/|_  $$_/| $$      | $$
    # | $$        | $$  | $$      | $$
    # | $$$$$     | $$  | $$      | $$
    # | $$__/     | $$  | $$      | $$
    # | $$        | $$  | $$      | $$
    # | $$       /$$$$$$| $$$$$$$$| $$$$$$$$
    # |__/      |______/|________/|________/
    student_names =[]

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
    #  /$$$$$$$$ /$$$$$$ /$$       /$$
    # | $$_____/|_  $$_/| $$      | $$
    # | $$        | $$  | $$      | $$
    # | $$$$$     | $$  | $$      | $$
    # | $$__/     | $$  | $$      | $$
    # | $$        | $$  | $$      | $$
    # | $$       /$$$$$$| $$$$$$$$| $$$$$$$$
    # |__/      |______/|________/|________/
    result = []

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

    