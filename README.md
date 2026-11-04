# tasca8-supermercat

Anàlisi de dades de vendes amb Python. És una tasca de l'optativa de 1r (ASIX,
curs 2025-26): integrar les dades d'uns sensors de comptatge de clients amb les
vendes del dia i veure si hi ha relació.

## Què fa

- **`analisi_estacio.py`** — llegeix `vendes_estacio.csv`, dibuixa una regressió
  amb `seaborn.regplot` i desa el gràfic a `grafic_analisi_8.png`.
- **`app_tasca8.py`** — el mateix, però com a aplicació de Streamlit: taula de
  dades a l'esquerra i gràfic a la dreta.
- **`vendes_app.py`** — un pas més: entrena una `LinearRegression` de
  scikit-learn amb `vendes_setmanals.csv` i prediu les vendes d'una setmana que
  li demanis.

## Les dades

`vendes_estacio.csv` són vuit setmanes amb tres columnes: setmana, vendes en
euros i recompte de clients dels sensors IR.

```
setmana,vendes,recompte_clients
1,950,210
2,1100,245
...
```

`vendes_setmanals.csv` és un conjunt més llarg, de 52 setmanes amb dues
columnes (setmana i vendes), que és el que fa servir el model de regressió. És
una sèrie amb tendència creixent, pensada perquè la recta tingui sentit.

## Com s'executa

```bash
pip install -r requirements.txt

python analisi_estacio.py                     # genera el PNG
streamlit run app_tasca8.py                   # el dashboard
streamlit run vendes_app.py                   # el predictor
```

Els tres scripts llegeixen els CSV del directori de treball, així que s'han
d'executar des de l'arrel del repositori.

## Detalls

- El model de `vendes_app.py` separa entrenament i prova amb
  `train_test_split(test_size=0.2, random_state=42)`. Amb 52 setmanes, la prova
  són deu punts: prou per veure que la recta s'ajusta, no per treure'n
  conclusions estadístiques.
- `app_tasca8.py` fa servir `width='stretch'` a `st.dataframe` perquè les
  versions noves de Streamlit han canviat el paràmetre antic
  `use_container_width`.

## Autor

Pere Brau Martínez · ASIX C1A
