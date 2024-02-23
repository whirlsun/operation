import pandas as pd

data = pd.read_csv("static/opendata.csv", encoding="GBK", dtype="str", nrows=5)


print(data)
