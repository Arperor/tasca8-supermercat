import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st

# Llegir les dades
data = pd.read_csv("vendes_setmanals.csv")

# Separar dades d'entrada (X) i sortida (y)
X = data[['Setmana']]
y = data['Vendes']

# Dividir dades en entrenament i prova
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Crear i entrenar el model
model = LinearRegression()
model.fit(X_train, y_train)

# Aplicació Streamlit
st.title("Predicció de Vendes Setmanals")

setmana = st.number_input(
    "Introduïu el número de setmana:",
    min_value=1,
    max_value=52,
    step=1
)

if setmana:
    prediccio = model.predict([[setmana]])
    st.write(f"La predicció de vendes per a la setmana {setmana} és: {prediccio[0]:.2f}")

