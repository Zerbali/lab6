# "For a two-dimensional array A(n,n), find the geometric mean of the positive elements in each column and write it on the main diagonal. Print the matrix in the standard format."


import math

def geometric_mean(nums):
    product = 1
    count = 0
    for num in nums:
        if num > 0:
            product *= num
            count += 1
    if count == 0:
        return 0
    return product ** (1 / count)

def process_matrix(A):
    n = len(A)
    for j in range(n):  
        column = [A[i][j] for i in range(n)]
        gm = geometric_mean(column)
        A[j][j] = round(gm, 2)  

    return A

def print_matrix(A):
    for row in A:
        print('\t'.join(f"{val:.2f}" if isinstance(val, float) else str(val) for val in row))

n = 4
A = [
    [4, -2, 3, 1],
    [2, 0, -5, 6],
    [9, 8, 7, -1],
    [5, 2, 1, 0]
]

print("Original matrix:")
print_matrix(A)

print("\nProcessed matrix:")
A = process_matrix(A)
print_matrix(A)
