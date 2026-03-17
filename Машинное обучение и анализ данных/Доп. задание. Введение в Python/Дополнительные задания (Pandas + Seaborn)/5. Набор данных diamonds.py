import pandas as pd

diamonds = pd.DataFrame({
    "color":["E","E","F","G","F","G"],
    "price":[3000,3500,2800,4000,3200,4100]
})

result = diamonds.groupby("color")["price"].mean()

print(result)