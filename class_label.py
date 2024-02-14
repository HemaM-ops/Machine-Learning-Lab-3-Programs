import pandas as pd

# Read the Excel file
df = pd.read_excel(r"C:\Users\mahad\OneDrive\Desktop\SEM 4 Courses\ML\Lab Programs\Lab 3- 13.02.24(Tue)\purchase_data.xlsx")

# Add a new column 'CustomerCategory' based on the payment amount
df['CustomerCategory'] = df['Payment (Rs)'].apply(lambda x: 'RICH' if x > 200 else 'POOR')

# Save the modified DataFrame back to Excel
df.to_excel("labeled_customers.xlsx", index=False)
