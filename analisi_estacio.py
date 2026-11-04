import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vendes_estacio.csv')
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# Gràfic de dispersió: Correlació entre clients (Sensors IR) i Vendes
sns.regplot(x='recompte_clients', y='vendes', data=df, color='blue', line_kws={'color':'red'})

plt.title('Anàlisi Tasca 8: Correlació Clients vs Vendes - Supermercat l\'Estació')
plt.xlabel('Recompte de Clients (Sensors IR)')
plt.ylabel('Vendes totals (€)')

plt.savefig('grafic_analisi_8.png')
print("✅ Gràfic 'grafic_analisi_8.png' generat amb èxit.")
