import seaborn as sns

tips = sns.load_dataset("tips")

tips["tippercentage"] = tips["tip"] / tips["total_bill"] * 100

print(tips.head())
