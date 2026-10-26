import numpy as np

# Input: Two matrices (Lists)
matrix1 = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]

matrix2 = [[9, 8, 7], 
           [6, 5, 4], 
           [3, 2, 1]]

print("--- Matrix Addition Using Python Lists ---")
# Initialize empty result matrix
result_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Perform addition
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result_list[i][j] = matrix1[i][j] + matrix2[i][j]

for row in result_list:
    print(row)

print("\n--- Matrix Addition Using NumPy Arrays ---")
# Convert lists to NumPy arrays
np_arr1 = np.array(matrix1)
np_arr2 = np.array(matrix2)

# Perform addition directly
result_numpy = np_arr1 + np_arr2

print(result_numpy)
