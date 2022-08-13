import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv("housing.csv")
print(df)

Profile = ProfileReport(df)
Profile.to_file(output_file="report.html")
