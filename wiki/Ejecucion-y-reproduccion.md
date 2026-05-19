# Ejecucion y reproduccion

## Requisitos

- Python 3.10 o superior
- Dependencias en `requirements.txt`

## Instalacion

Desde la raiz del repositorio:

```bash
pip install -r requirements.txt
```

Paquetes principales: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `streamlit`, `jupyter`, `ipykernel`.

## Ejecutar el notebook

1. Abrir `Atribucion_Multicanal_Fases_1_2_3.ipynb` en Jupyter o VS Code/Cursor.
2. Seleccionar un kernel con las dependencias instaladas.
3. Ejecutar **Restart & Run All** en orden.

El notebook asume que el directorio de trabajo es la raiz del proyecto (donde estan `data/` y `output/`).

## Orden interno

Las fases dependen de variables en memoria:

| Fase | Variables clave producidas |
|------|---------------------------|
| 1-2 | `mql`, `deals`, `global_rate` |
| 3 | `df`, `trans_prob`, `channel_summary` |
| 4 | `re_df`, `comparison`, `baseline_df` |
| 5 | `sensitivity`, `scenarios_df` |
| 6 | `streamlit_app.py` (celda `%%writefile`) |

No es posible ejecutar Fase 4 sin haber completado Fase 3 en la misma sesion.

## Regenerar outputs

Al finalizar Fase 3, se crean los archivos base en `output/`. Las fases 4 y 5 anaden tablas y el informe de validacion. La Fase 6 escribe `streamlit_app.py` y `output/fig_executive_summary.html`.

Si solo se necesita el dashboard y los CSV ya existen en `output/`, basta con:

```bash
streamlit run streamlit_app.py
```

## Problemas frecuentes

| Error | Causa | Solucion |
|-------|-------|----------|
| `FileNotFoundError` en `data/` | Directorio de trabajo incorrecto | Ejecutar desde la raiz del repo |
| `ModuleNotFoundError: pandas` | Kernel distinto al entorno con pip | Instalar deps en el kernel activo |
| Streamlit sin datos | Fases 4-5 no ejecutadas | Correr el notebook completo o copiar outputs previos |

## Kernel en VS Code / Cursor

```bash
python -m ipykernel install --user --name=atribucion-olist
```

Seleccionar ese kernel en el notebook.
