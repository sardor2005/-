import seaborn as sns

titanic = sns.load_dataset("titanic")

female_passengers = titanic[titanic["sex"] == "female"]

print(female_passengers.head())
