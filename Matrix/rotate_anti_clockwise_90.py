mat = [[1,2],[3,4]]

def rotateMatrix(mat):
    # Reverse the elements of each row 
    for row in range(len(mat)):
        mat[row] = mat[row][len(mat) - 1:] + mat[row][0:len(mat) - 1]
    for row in range(len(mat)):
        for col in range(row, len(mat)):
            mat[row][col], mat[col][row] = mat[col][row], mat[row][col]


def displayMatrix(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            print(mat[i][j], end=' ')
        print()

displayMatrix(mat)
print()
rotateMatrix(mat)

# Print rotated matrix
displayMatrix(mat)
