
import statistics
import pandas as pd



file_path="C:\\Users\\mahad\\OneDrive\\Desktop\\SEM 4 Courses\\ML\\Lab Programs\\Lab 3- 13.02.24(Tue)\\Lab Session1 Data.xlsx"

sheet_names = ["Purchase Data","IRCTC Stock Price"]

data_dict = pd.read_excel(file_path, sheet_name=sheet_names)

df_sheet1=data_dict["Purchase data"]
df=data_dict["IRCTC Stock Price"]

print(df.head)

import statistics


price_data = df_sheet2["Price"]

#Mean and Variance of Price Data (column D): 
mean_price = statistics.mean(price_data)
variance_price = statistics.variance(price_data)

print("Mean of Price:", mean_price)
print("Variance of Price:", variance_price)

#Wednesdays
wednesday_prices = df[df["Day"].dt.dayofweek == 2]["Price"]  
wednesday_mean = wednesday_prices.mean()

print("Sample Mean of Wednesdays:", wednesday_mean)
print("Comparison with Population Mean:", "Higher" if wednesday_mean > mean_price else "Lower")
# April
april_prices = df[df["Date"].dt.month == 4]["Price"]  
april_mean = april_prices.mean()

print("Sample Mean of April:", april_mean)
print("Comparison with Population Mean:", "Higher" if april_mean > mean_price else "Lower")

loss_probability = sum(df["Chg%"] < 0) / len(df["Chg%"])

print("Probability of Loss:", loss_probability)

wednesday_profits = len(df[(df["Day"].dt.dayofweek == 2) & (df["Chg%"] > 0)])
wednesday_probability = wednesday_profits / len(df[df["Day"].dt.dayofweek == 2])

print("Probability of Profit on Wednesdays:", wednesday_probability)


total_profits = len(df[df["Chg%"] > 0])
conditional_probability = wednesday_probability / (total_profits / len(df))

print("Conditional Probability of Profit on Wednesday:", conditional_probability)


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(df["Day"].dt.dayofweek, df["Chg%"])
plt.xlabel("Day of Week")
plt.ylabel("Chg%")
plt.title("IRCTC Stock Price: Change% vs. Day of Week")
plt.xticks([0, 1, 2, 3, 4, 5, 6], ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
plt.show()
