# Metodologia CRISP-DM

El proyecto sigue las seis fases de CRISP-DM. La implementacion esta en un unico notebook en la raiz del repositorio.

## Fase 1 — Business Understanding

Define el marco de negocio antes del modelado:

- **Conversion:** MQL con `mql_id` en `closed_deals` y `won_date` registrada.
- **Reglas:** `origin` vacio a `(not set)`; leads con mas de 90 dias marcados con `long_journey=True` sin excluirlos.
- **Metrica principal:** Removal Effect por canal.
- **Objetivos del modelo:** documentados en la celda "Objetivos del modelo" del notebook.

## Fase 2 — Data Understanding

EDA sobre los datasets en `data/`:

- Distribucion de MQLs y tasas de conversion por canal.
- Analisis temporal y de lead time.
- Hallazgo critico: un solo touchpoint por lead (`origin`).

Salida: figuras en `output/fig_*.png` (prefijos de fases 2 y 3).

## Fase 3 — Data Preparation

- LEFT JOIN MQLs + Deals por `mql_id`.
- Construccion de `journey_str`: `Start > [canal] > Conversion|Non_Conversion`.
- Matriz de transicion (conteos y probabilidades).
- Validaciones: 842 conversiones, 16.000 transiciones, filas que suman 1.

Salida principal: `output/transition_matrix_probs.csv`, `output/journeys_dataset.csv`.

## Fase 4 — Modeling

- **Baseline:** First-touch = Last-touch = Linear (equivalentes con un touchpoint).
- **Markov orden 1:** P(conv global) y Removal Effect por canal.
- **Tabla comparativa:** `output/attribution_comparison.csv`.
- Markov orden 2-3: no aplicable con la estructura actual de journeys.

## Fase 5 — Evaluation

- Comparacion de rankings (tasa vs baseline vs Markov).
- Coherencia numerica (842 conversiones).
- Sensibilidad sin `long_journey`.
- Simulaciones al eliminar canales.
- Bootstrap en canales de bajo volumen.
- Informe: `output/validation_report.txt`.

## Fase 6 — Deployment

- Generacion de `streamlit_app.py` en la raiz.
- Figura ejecutiva HTML en `output/`.
- Dashboard con comparativa, Sankey, heatmap y simulador de pesos por canal.

## Flujo de dependencias

```
data/*.csv  -->  Fases 1-3  -->  output/journeys + matriz
                                      |
                                      v
                               Fases 4-5  -->  output/atribucion + validacion
                                      |
                                      v
                               Fase 6  -->  streamlit_app.py
```
