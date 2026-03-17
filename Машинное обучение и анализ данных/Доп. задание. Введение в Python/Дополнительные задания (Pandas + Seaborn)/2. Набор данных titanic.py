import pandas as pd

titanic = pd.DataFrame({
    "sex":["male","female","female","male","female"],
    "age":[22,38,26,35,27],
    "fare":[7.25,71.28,7.92,53.10,11.13]
})

female_passengers = titanic[titanic["sex"]=="female"]

print(female_passengers)