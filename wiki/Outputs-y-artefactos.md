# Outputs y artefactos

Todos los archivos generados por el pipeline se guardan en `output/`. No deben editarse a mano; se regeneran al ejecutar el notebook.

## Datasets preparados (Fase 3)

| Archivo | Descripcion |
|---------|-------------|
| `journeys_dataset.csv` | 8.000 MQLs con `journey_str`, `converted`, `long_journey` |
| `transition_matrix_probs.csv` | Matriz de transicion (probabilidades) |
| `transition_matrix_counts.csv` | Matriz en conteos |
| `transition_counts.csv` | Pares from/to con conteo |
| `channel_summary.csv` | MQLs, conversiones y tasa por canal |

## Modelado y evaluacion (Fases 4-5)

| Archivo | Descripcion |
|---------|-------------|
| `attribution_comparison.csv` | Tabla comparativa: tasa, baseline, Markov |
| `sensitivity_analysis.csv` | Removal Effect con y sin `long_journey` |
| `scenario_simulations.csv` | Impacto al eliminar canales |
| `bootstrap_low_volume.csv` | IC95 en canales pequenos |
| `validation_report.txt` | Resumen de validacion |

## Visualizaciones

| Archivo | Fase aprox. |
|---------|-------------|
| `fig_nulls.png` | 2 |
| `fig_channel_distribution.png` | 2 |
| `fig_conversion_rates.png` | 2 |
| `fig_volume_vs_rate.png` | 2 |
| `fig_monthly_trends.png` | 2 |
| `fig_lead_time.png` | 2 |
| `fig_segments.png` | 2 |
| `fig_transition_matrix.png` | 3 |
| `fig_start_transitions.png` | 3 |
| `fig_attribution_comparison.png` | 4 |
| `fig_executive_summary.html` | 6 |

## Consumidores de cada output

| Consumidor | Archivos que lee |
|------------|------------------|
| Notebook Fases 4-5 | `channel_summary` (memoria), matriz en memoria |
| `streamlit_app.py` | `journeys_dataset`, `transition_matrix_probs`, `attribution_comparison`, `scenario_simulations` |
| Presentacion | `fig_executive_summary.html`, `fig_attribution_comparison.png` |

## Columnas clave de `attribution_comparison.csv`

| Columna | Significado |
|---------|-------------|
| `mqls` | Volumen de leads por canal |
| `conversiones_reales` | Deals cerrados (ground truth) |
| `tasa_conv_pct` | Tasa simple de conversion |
| `atrib_first_touch` | Atribucion baseline |
| `removal_effect` | Removal Effect (proporcion) |
| `atrib_markov_norm` | Conversiones atribuidas Markov (suma 842) |
| `rank_tasa`, `rank_markov`, `rank_baseline` | Posiciones en ranking |
