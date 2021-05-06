import pandas as pd
from openpyxl.workbook import Workbook

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)
print(df["Age"])

ages = pd.Series([12, 35, 58], name="Age")
print(ages)

print(df["Age"].max())
print(df.describe())

titanic = pd.read_csv("Pandas/titanic.csv")
print(titanic)

print(titanic.head(8))
print(titanic.dtypes)

titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

print(titanic.info())