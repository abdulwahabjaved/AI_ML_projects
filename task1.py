
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('iris')



print("🔹 Shape of dataset:", df.shape)
print("\n🔹 Column Names:", df.columns.tolist())

print("\n🔹 First 5 Rows:")
print(df.head())

print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Statistical Summary:")
print(df.describe())


# Scatter Plot
plt.figure(figsize=(6,4))
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df)
plt.title("Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

#Histograms
df.hist(figsize=(10,6))
plt.suptitle("Feature Distributions")
plt.show()

# Box Plot
plt.figure(figsize=(8,5))
sns.boxplot(data=df)
plt.title("Box Plot for Outlier Detection")
plt.show()



#  Pairplot
sns.pairplot(df, hue='species')
plt.show()