import seaborn as sns

mpg = sns.load_dataset("mpg")

mpg_sorted = mpg.sort_values("mpg", ascending=False)

print(mpg_sorted.head(10))
