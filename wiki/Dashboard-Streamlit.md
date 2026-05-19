# Dashboard Streamlit

## Archivo

`streamlit_app.py` en la raiz del repositorio.

Se genera o actualiza desde la Fase 6 del notebook (celda `%%writefile`). Tambien puede editarse directamente; conviene mantener coherencia con las rutas `output/`.

## Lanzamiento

Desde la raiz del proyecto, con los CSV de `output/` ya generados:

```bash
streamlit run streamlit_app.py
```

Puerto por defecto: 8501. La URL se muestra en la terminal.

Desde el notebook, descomentar en la celda de lanzamiento:

```python
import os
os.system('streamlit run streamlit_app.py')
```

## Pestañas

### Comparativa de atribucion

Tabla con MQLs, conversiones reales, tasa, baseline y Markov. Grafico de barras agrupadas: baseline vs Markov normalizado.

### Journey (Sankey)

Flujo agregado: `Start` -> canal -> `Conversion` / `Non_Conversion`. Volumenes escalados al numero de MQLs.

### Grafo de transiciones

Heatmap de `P(canal -> Conversion)` y `P(canal -> Non_Conversion)`.

### Simulador

Sliders por canal para ajustar `P(Start -> canal)`. Los pesos se normalizan a 1. Muestra P(conv) simulada, conversiones estimadas y delta respecto al escenario base. Incluye tabla de escenarios pre-calculados de Fase 5.

## Datos requeridos

| Ruta | Origen |
|------|--------|
| `output/journeys_dataset.csv` | Fase 3 |
| `output/transition_matrix_probs.csv` | Fase 3 |
| `output/attribution_comparison.csv` | Fase 4 |
| `output/scenario_simulations.csv` | Fase 5 |

Si falta algun archivo, ejecutar el notebook completo antes de lanzar Streamlit.

## Sidebar

Resumen del modelo, limitacion de touchpoint unico y fuente de datos.
