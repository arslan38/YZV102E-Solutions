# Table of Contents
- [Question](#question)
- [Report](#report)

 ----

## Question


#### In implementation part you will fill the following functions;

- _read_grades_ : As shown in Code Snippet 1, read grades function takes a string
parameter named as filename. In the function, you will create four dictionaries
named name, mt1, mt2 and final. You will open and read the csv file located in
the input parameter. You can check the csv file named as grades.csv. The keys
of these dictionaries are the numbers of the students given in the csv in string
format. In name dictionary you will store names of the students in string format.
mt1, mt2 and final dictionaries store the grades as values in integer format. Finally
this function returns these dictionaries.

- _convert_ : As shown in Code Snippet 2, the function takes four dictionaries. In
the function you will create a list of tuples. The tuple should be structured like
(number, name, mt1, mt2, f inal). In each list item will be a tuple and in the each
tuple you will store a student’s information and grades.

- _calculate_exam_average_ : As shown in Code Snippet 3, the function takes two
inputs; first one is a list created in convert function and the second one is a string
that can be ”midterm1”, ”midterm2”or”f inal”. In this function you will calculate
the average grade of the exam specified in the second parameter.

- find_passing_students : As shown in Code Snippet 4, the function takes a list
created in convert function. You will create a list of students who can pass the
course. Cumulative grade is calculated like in Equation 0.1. If cumulative grade >
60 student can pass otherwise student will fail. You will return the student names
who can pass the lecture. [cumulative grade = (0.3) ∗ mt1 + (0.3) ∗ mt2 + (0.4) ∗ final]

- _manipulate_ : As shown in Code Snippet 5, the function takes a string that contains
a csv file name and a list created in convert function. In this function you will open
a csv file and parse the csv(check the edit.csv). If the number is in the list you will
update the grade of the student that has the number otherwise you should ignore
that line. After update operation of the list you should return the manipulated
list.


## Report

Report Template
- https://ninova.itu.edu.tr/Sinif/24421.67325/Odev/107577?g3472996 (.pdf)
- https://ninova.itu.edu.tr/Sinif/24421.67325/Odev/107577?g3478922 (.tex)

Learn LateX
- https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes

 ----
