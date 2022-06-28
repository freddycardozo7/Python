mat = [[1,2],[3,4]]

def rotateMatrix(mat):
    for row in range(len(mat)):
        mat[row].reverse()
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
