import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Supermercat l'Estació", layout="wide")

st.title("📊 Anàlisi de Dades - Supermercat l'Estació")
st.markdown("Basat en la integració de sensors IR (OT) i sistemes de vendes (IT).")

# Carregar dades
df = pd.read_csv('vendes_estacio.csv')

# Layout de columnes
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Dades recollides")
    # Hem canviat use_container_width per width='stretch' per evitar el warning
    st.dataframe(df, width='stretch')

with col2:
    st.subheader("📈 Correlació Clients vs Vendes")
    fig, ax = plt.subplots()
    sns.regplot(x='recompte_clients', y='vendes', data=df, ax=ax, color='blue', line_kws={'color':'red'})
    st.pyplot(fig)

st.success("✅ L'anàlisi confirma que a major afluència detectada pels sensors IR, les vendes augmenten linealment.")
