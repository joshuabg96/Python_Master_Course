# We have a matrix, the last value of every row 
# have to be a sum of the three elements before
# create a code that solve the incorrect values
matrix = [[1,1,1,3],[2,2,2,7],[3,3,3,9], [4,4,4,13]]
print(matrix)
for i in range(0,len(matrix)):
    matrix[i][-1] = sum(matrix[i][:-1])
print(matrix)
        
