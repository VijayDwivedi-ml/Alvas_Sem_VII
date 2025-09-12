import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("state.csv")

# 1. How many rows and columns does the dataset have, and what are the column names?
print(df.shape)
print(df.columns)

# 2. What are the mean, median, and standard deviation of the Murder.Rate column?
print("Mean:", df["Murder.Rate"].mean())
print("Median:", df["Murder.Rate"].median())
print("Std Dev:", df["Murder.Rate"].std())

# 3. Which state has the highest and lowest population?
print("Highest population:", df.loc[df["Population"].idxmax()])
print("Lowest population:", df.loc[df["Population"].idxmin()])

# 4. Plot the distribution of Murder.Rate values across all states.
plt.hist(df["Murder.Rate"], bins=10, edgecolor="black")
plt.xlabel("Murder Rate")
plt.ylabel("Number of States")
plt.title("Distribution of Murder Rate")
plt.show()

# 5. Which 5 states have the highest Murder.Rate relative to their population size?
df["MurderRatePer100kPop"] = (df["Murder.Rate"] / df["Population"]) * 100000
print(df.sort_values("MurderRatePer100kPop", ascending=False).head(5))

# 6. Create a scatterplot of Population vs Murder.Rate and describe the trend.
plt.scatter(df["Population"], df["Murder.Rate"])
plt.xlabel("Population")
plt.ylabel("Murder Rate")
plt.title("Population vs Murder Rate")
plt.show()
