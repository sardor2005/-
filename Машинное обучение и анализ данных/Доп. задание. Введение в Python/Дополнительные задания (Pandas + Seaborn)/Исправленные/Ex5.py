import seaborn as sns

diamonds = sns.load_dataset("diamonds")

result = diamonds.groupby("color")["price"].mean()

print(result)
