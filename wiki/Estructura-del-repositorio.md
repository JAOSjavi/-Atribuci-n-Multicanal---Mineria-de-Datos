# Estructura del repositorio

## Arbol de directorios

```
.
├── Atribucion_Multicanal_Fases_1_2_3.ipynb
├── streamlit_app.py
├── requirements.txt
├── README.md
├── data/
│   ├── olist_marketing_qualified_leads_dataset.csv
│   └── olist_closed_deals_dataset.csv
├── output/
│   ├── .gitkeep
│   └── (artefactos generados por el notebook)
├── docs/
│   ├── GLOSARIO.txt
│   └── INFORME_TECNICO_Y_RECOMENDACIONES.txt
└── wiki/
    └── (esta documentacion)
```

## Reglas de organizacion

| Ubicacion | Que contiene |
|-----------|----------------|
| Raiz | Solo el notebook principal, la app Streamlit y archivos de configuracion |
| `data/` | Datasets fuente de Kaggle. No se modifican en el pipeline |
| `output/` | Todo lo generado al ejecutar el notebook: CSV, PNG, HTML, TXT |
| `docs/` | Documentacion estatica de referencia (glosario, informe) |
| `wiki/` | Documentacion operativa del proyecto |

## Variables de rutas en el notebook

La segunda celda de codigo define:

```python
ROOT = Path('.')
DATA_DIR = ROOT / 'data'
OUTPUT_DIR = ROOT / 'output'
```

Todas las lecturas de datos fuente usan `DATA_DIR`. Todos los guardados (CSV, figuras, informes) usan `OUTPUT_DIR`.

## Ejecucion desde la raiz

El notebook y Streamlit deben ejecutarse con el directorio de trabajo en la raiz del repositorio, para que las rutas relativas `data/` y `output/` resuelvan correctamente.
