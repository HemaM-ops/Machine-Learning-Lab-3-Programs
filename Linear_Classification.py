import pandas as pd
import numpy as np

df = pd.read_excel("C:/Users/mahad/OneDrive/Desktop/purchase_data.xlsx")
# Extraction of specific columns into matrices
A = df[['Candies (#)','Mangoes (Kg)','Milk Packets (#)']].values  
C = df[['Payment (Rs)']].values
print(A)
print(C)
num_rows, num_columns = A.shape
print("Dimensionality of the vector space:", num_columns)
print("The number of vectors that exist in the vector space:", num_rows)
np_matrix = df.to_numpy()
rank = np.linalg.matrix_rank(matrix1)
print("Rank of the matrix:", rank)
pseudo_inv=np.linalg.pinv(A)
X=pseudo_inv@C
print(X)
print("The individual cost of a candy is: ",round(X[0][0]))
print("The individual cost of a mango is: ",round(X[1][0]))
print("The individual cost of a milk packet is: ",round(X[2][0]))
