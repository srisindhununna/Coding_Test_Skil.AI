import pandas as pd
df=pd.read_csv("task1.csv")
grouped=df[df["gender"]=='Male'].groupby('city')['population'].sum()
city_with_most_population=grouped.idxmax()

print(f"The city with most population is :", city_with_most_population,"with population",max(grouped))