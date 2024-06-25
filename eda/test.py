import numpy as np
import pandas as pd

from clean import CleanDataFrame

# Limpieza de Datos

df = pd.read_csv("data/spam.csv", encoding="latin-1")
df = CleanDataFrame.CleanDf(df)

print(df)
