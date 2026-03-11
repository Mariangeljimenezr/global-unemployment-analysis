# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Entorno de análisis listo")

df = pd.read_csv(r"C:\Users\Mariangel Jiménez\OneDrive\Escritorio\Data-analytics-portafolio\labor-market-analysis\Data\API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_93\API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_93.csv", skiprows=4)

print(df.head())
countries = ["Argentina", "Brazil", "United States", "Germany"]

df_countries = df[df["Country Name"].isin(countries)]

df_years = df_countries[["Country Name"] + [str(y) for y in range(2010, 2023)]]

print(df_years)

df_plot = df_years.set_index("Country Name").T

plt.clf()

df_plot.plot(figsize=(10,6))

plt.title("Unemployment Rate Comparison")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")

plt.grid(True, linestyle="--", alpha=0.4)

plt.savefig("unemployment_comparison.png", dpi=300)

plt.show()
