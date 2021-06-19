def score_matrix(matrix):
    final=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i+j)%2==0:
                final+=matrix[i][j]
            else:
                final-=matrix[i][j]
    return final