import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("StatischeWerte.xlsx")

grouped_means = df.groupby(list(df.columns[:5])).mean()
grouped_means.to_excel("groups.xlsx")

# Kurzübersicht:
grouped_means.describe() 

# Alternativ:
grouped_means.mean() 
grouped_means.std() 
grouped_means.quantile(q=0.05)  
grouped_means.quantile(q=[0.01, 0.05, 0.1, 0.5])

# geplottet
grouped_means['Biegefestigkeit [N/mm²]'].hist(cumulative=True, density=True, bins=30)
plt.show() 


# Spaltenspezifische Aggregation:
df.groupby(list(df.columns[:5])).agg(
    {
        "Biegefestigkeit [N/mm²]": np.mean,
        "Biege-E-Modul [N/mm²]": np.mean,
        "Biegesteifigkeit [kNm²/m]": np.mean,
    }
).to_excel("groups.xlsx")


# Filterungen:
df.query("`Prüfseite` == 'TS'")
df.loc[ df['Plattenzustand'] == 'T' ]