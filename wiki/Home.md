# Wiki — Atribucion Multicanal Olist

Documentacion del proyecto de atribucion multicanal sobre el funnel de marketing B2B de Olist.

## Proposito

Determinar que canal de marketing aporta valor real a las conversiones (sellers cerrados), mas alla de la tasa de conversion simple por canal. El modelo principal usa cadenas de Markov de orden 1 y la metrica **Removal Effect**.

## Indice

| Pagina | Contenido |
|--------|-----------|
| [Estructura del repositorio](Estructura-del-repositorio.md) | Carpetas, archivos y convenciones |
| [Metodologia CRISP-DM](Metodologia-CRISP-DM.md) | Fases 1 a 6 y entregables |
| [Modelo Markov y Removal Effect](Modelo-Markov-y-Removal-Effect.md) | Definicion matematica y limitaciones |
| [Ejecucion y reproduccion](Ejecucion-y-reproduccion.md) | Instalacion, notebook y orden de ejecucion |
| [Outputs y artefactos](Outputs-y-artefactos.md) | CSV, figuras e informes en `output/` |
| [Dashboard Streamlit](Dashboard-Streamlit.md) | Uso del dashboard interactivo |

## Referencias en el repositorio

- Notebook: `Atribucion_Multicanal_Fases_1_2_3.ipynb` (raiz del proyecto)
- Glosario: `docs/GLOSARIO.txt`
- Informe tecnico: `docs/INFORME_TECNICO_Y_RECOMENDACIONES.txt`

## Resumen de datos

| Metrica | Valor |
|---------|-------|
| MQLs | 8.000 |
| Conversiones | 842 |
| Tasa global | 10,53 % |
| Periodo MQLs | Jun 2017 – May 2018 |
| Canales | 11 + `(not set)` |

## Limitacion principal

Cada lead registra un unico touchpoint (`origin`). Los modelos First-touch, Last-touch y Linear son equivalentes. El diferencial analitico esta en el Removal Effect y las simulaciones de escenarios.
