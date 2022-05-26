import pandas as pd

df = pd.read_csv("Worldometers_data.csv", thousands=',')
# df.fillna(0, inplace=True)
total = df.sum(numeric_only = True, skipna=True).sum()
print(f"La somme est %.2f ,le 6em chiffre est %s"%(total, str(total)[5]))
