# Table of Contents
- [Question](#question)
- [Report](#report)

 ----

## Question


#### Matrices are commonly used in math. In this homework you will do some operations with matrices. Any pre-ready library like numpy, etc. usage is forbidden. 

Note: You will only use _2x2_ or _3x3_ matrices. Try to be effective, avoid unnecessary loops. The operations are listed below;

- Read Matrix

- Transpose of a Matrix

- Sum of Matrices

- Difference of Matrices

- Multiplication of Matrices

- Determinant of a Matrix
 
### Read Matrix:

- You will complete the function named _read_matrix_ .
- In the function, input is taken from user and input casted as integer. 
- This input will be the dimension size of the matrix. 
- The rows of the matrix are separated with new lines and the columns are separated with spaces.

### Transpose of a Matrix: 

- The transpose of a matrix is an operator which flips a matrix over its diagonal; that is, it switches the row and column indices of the matrix _A_ by producing another matrix, often denoted by _A^T_ . 
- Note: Do not hard code here, the transpose operation should be dynamic so the transpose must be found with for loops.

<img src="https://i.hizliresim.com/lg5LDy.png" data-canonical-src="https://i.hizliresim.com/lg5LDy.png" width="500" height="250" />

### Sum of a Matrices: 

- Sum operation can be done like below. 
- Note: Do not hard code here, the transpose operation should be dynamic so the transpose must be found with for loops. 
You should check whether the dimensions are match or not. If dimensions are not match return -1; otherwise, return the summation of matrices.

<img src="https://i.hizliresim.com/iBqyyF.png" data-canonical-src="https://i.hizliresim.com/iBqyyF.png" width="400" height="110" />

### Difference of a Matrices: 

- Subtraction operation can be done like below. 
- Note: Do not hard code here, the transpose operation should be dynamic so the transpose must be found with for loops. 
You should check whether the dimensions are match or not. If dimensions are not match return -1; otherwise, return the summation of matrices.

<img src="https://i.hizliresim.com/2B5u1F.png" data-canonical-src="https://i.hizliresim.com/2B5u1F.png" width="400" height="110" />

### Multiplication of a Matrix:

-  Multiplication operation can be done like below. 

- Note: Do not hard code here, the transpose operation should be dynamic so the transpose must be found with for loops. 
You should check whether the dimensions are match or not. If dimensions are not match return ; otherwise, return the multiplication of matrices.

<img src="https://i.hizliresim.com/wCn2QV.png" data-canonical-src="https://i.hizliresim.com/wCn2QV.png" width="600" height="500" />

### Determinant of a Matrix:
- Determinant operation can be done like below. 
- Note: Do not hard code here, the transpose operation should be dynamic so the transpose must be found with for loops. You should check whether the dimensions are match or not. If dimensions are not match return ; otherwise, return the multiplication of matrices.

<img src="https://i.hizliresim.com/ALoIv3.png" data-canonical-src="https://i.hizliresim.com/ALoIv3.png" width="500" height="300" />

### Input Format

- n->[2,3] nxn matrix check example test case m->[2,3] mxm matrix check example test case

### Constraints

- You are responsible for only 2x2 or 3x3 matrices. Fill the functions.

### Output Format

- Fill the matrixes. Output will be created with main.

Sample Input 
```
2
1 2
3 4
3
1 2 3
4 5 6
7 8 9
```
Sample Output 
```
Matrix A:
1 2 
3 4 
Matrix B:
1 2 3 
4 5 6 
7 8 9 
Transpose of Matrix A:
1 3 
2 4 
Transpose of Matrix B:
1 4 7 
2 5 8 
3 6 9 
A + B:
Error dimension sizes of the matrixes are not the same
A - B:
Error dimension sizes of the matrixes are not the same
A * B:
Error dimension sizes of the matrixes are not the same
B * A:
Error dimension sizes of the matrixes are not the same
Determinant of Matrix A: -2
Determinant of Matrix B: 08
```
----

## Report

Report Template
- https://ninova.itu.edu.tr/Sinif/24421.67325/Odev/107577?g3472996 (.pdf)
- https://ninova.itu.edu.tr/Sinif/24421.67325/Odev/107577?g3478922 (.tex)

Learn LateX
- https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes

 ----
