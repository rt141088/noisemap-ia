import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("dados.csv")

X = df[['hora']]
y = df['ruido']

modelo = LinearRegression()
modelo.fit(X, y)

with open("modelo.pkl", "wb") as f:
    pickle.dump(modelo, f)

print("Modelo treinado!")