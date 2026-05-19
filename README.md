# Atribucion Multicanal — Olist Marketing Funnel

Proyecto de atribucion multicanal sobre el funnel B2B de Olist (Kaggle), con metodologia CRISP-DM y modelo principal de cadenas de Markov (Removal Effect).

## Estructura

```
.
├── Atribucion_Multicanal_Fases_1_2_3.ipynb   # Notebook principal (fases 1-6)
├── streamlit_app.py                          # Dashboard interactivo
├── requirements.txt
├── data/                                     # Datasets fuente (no modificar)
├── output/                                   # Artefactos generados al ejecutar el notebook
├── docs/                                     # Glosario e informe tecnico
└── wiki/                                     # Documentacion del proyecto
```

## Inicio rapido

```bash
pip install -r requirements.txt
jupyter notebook Atribucion_Multicanal_Fases_1_2_3.ipynb
```

Tras ejecutar el notebook (Kernel > Restart & Run All), lanzar el dashboard:

```bash
streamlit run streamlit_app.py
```

## Documentacion

La documentacion completa esta en la carpeta [wiki/](wiki/Home.md):

- [Home](wiki/Home.md)
- [Estructura del repositorio](wiki/Estructura-del-repositorio.md)
- [Metodologia CRISP-DM](wiki/Metodologia-CRISP-DM.md)
- [Modelo Markov y Removal Effect](wiki/Modelo-Markov-y-Removal-Effect.md)
- [Ejecucion y reproduccion](wiki/Ejecucion-y-reproduccion.md)
- [Outputs y artefactos](wiki/Outputs-y-artefactos.md)
- [Dashboard Streamlit](wiki/Dashboard-Streamlit.md)

## Datos

Fuente: [Olist Marketing Funnel](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle).

- `data/olist_marketing_qualified_leads_dataset.csv` — 8.000 MQLs
- `data/olist_closed_deals_dataset.csv` — 842 deals cerrados
