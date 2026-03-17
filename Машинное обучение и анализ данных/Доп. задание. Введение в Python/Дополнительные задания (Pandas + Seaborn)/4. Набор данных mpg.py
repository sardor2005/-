import pandas as pd

mpg = pd.DataFrame({
    "car":["a","b","c","d","e"],
    "mpg":[18,25,30,22,35]
})

mpg_sorted = mpg.sort_values("mpg", ascending=False)

print(mpg_sorted.head(10))