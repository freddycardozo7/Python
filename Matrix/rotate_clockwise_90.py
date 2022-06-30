# Program to rotate a square matrix clockwise by 90 degrees

mat = [[1,2,3,4],[5,6,7,8], [8,9,10,11], [13,14,15,16]]

def rotateMatrix(mat):
    for row in range(len(mat)):
       mat[row] = mat[row][len(mat) - 1:] + mat[row][len(mat) - 2::-1]


    print()
    displayMatrix(mat)

    col=len(mat[0])-1
    irow = 1
    row = 1
    icol=col
    mainrow = 0
    while col >= 0:
        #for row in range(1, col+1):
        row=irow
        col1 = col
        while row < len(mat[0]):
            col1 -= 1
            temp =  mat[mainrow][col1]
            mat[mainrow][col1] = mat[row][col]
            mat[row][col] = temp
            row+=1
        mainrow += 1
        col -= 1
        irow+=1

def displayMatrix(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            print(mat[i][j], end=' ')
        print()

displayMatrix(mat)
print()
rotateMatrix(mat)
displayMatrix(mat)
