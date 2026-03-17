import pandas as pd

tips = pd.DataFrame({
    "total_bill":[16.99,10.34,21.01,23.68,24.59],
    "tip":[1.01,1.66,3.50,3.31,3.61]
})

tips["tippercentage"] = tips["tip"] / tips["total_bill"] * 100

print(tips)