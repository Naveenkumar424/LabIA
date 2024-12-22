'''Write a Python program to compute the multiplication of two matrices. 
Ensure the program checks if matrix multiplication is valid based on the dimensions of the input matrices.'''

r1 = int(input("Enter row size of matrix 1:"))
c1 = int(input("Enter column size of matrix 1:"))
r2 = int(input("Enter row size of matrix 2:"))
c2 = int(input("Enter column size of matrix 2:"))
if(c1 == r2):
    print("Matrix sizes are compatible...")
    print(f"Enter {r1}x{c1} elements for matrix 1:")
    A = []
    for i in range(r1):
        r = []
        for j in range(c1):
            r.append(int(input()))
        A.append(r)
    print(f"Enter {r2}x{c2} elements for matrix 2:")
    B = []
    for i in range(r1):
        r = []
        for j in range(c1):
            r.append(int(input()))
        B.append(r)

    #resultant matrix
    R = []
    for i in range(r1):
        r = []
        for j in range(c2):
            r.append(0)
        R.append(r)

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                R[i][j] += A[i][k]*B[k][j]

    print(R)
else:
    print("The two matrices are incompatible for multiplication")
#end of code