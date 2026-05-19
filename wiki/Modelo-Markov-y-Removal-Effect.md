# Modelo Markov y Removal Effect

## Cadena de estados

Cada MQL recorre un journey de tres estados:

```
Start  -->  [canal de marketing]  -->  Conversion | Non_Conversion
```

Estados en la matriz de transicion:

- `Start`: punto de entrada unico.
- Canales: `organic_search`, `paid_search`, `social`, `unknown`, etc.
- `Conversion` y `Non_Conversion`: estados absorbentes.

## Probabilidad de conversion global

```
P(conv) = SUM_c  P(Start -> c) * P(c -> Conversion)
```

Donde `c` recorre los canales con entrada desde `Start`. Con los datos actuales, P(conv) coincide con la tasa observada (10,53 %).

## Removal Effect

Para cada canal `C`:

1. Copiar la matriz de probabilidades.
2. Fijar `P(Start -> C) = 0`.
3. Renormalizar la fila `Start` entre los canales restantes.
4. Recalcular `P(conv)` sin el canal.
5. Calcular:

```
Removal_Effect(C) = (P(conv)_base - P(conv)_sin_C) / P(conv)_base
```

Interpretacion: caida relativa de la tasa de conversion global si ese canal deja de recibir trafico de entrada y su cuota se redistribuye proporcionalmente entre los demas.

## Atribucion en numero de conversiones

- **Raw:** `conversiones_atribuidas(C) = Removal_Effect(C) * 842`
- La suma de valores raw no es 842 (cada efecto es marginal e independiente).
- **Normalizada (comparacion):** se reparte 842 proporcionalmente a los Removal Effects para contrastar con el baseline.

## Modelos baseline

Con un solo touchpoint, First-touch, Last-touch y Linear asignan el 100 % del credito al unico canal registrado. Las conversiones atribuidas por baseline coinciden con las conversiones reales por canal.

## Limitaciones

| Limitacion | Impacto |
|------------|---------|
| Un touchpoint por lead | Baseline equivalente; no hay secuencias multi-canal |
| Markov orden 1 | Solo depende del estado actual |
| Canales pequenos | Estimaciones inestables (usar bootstrap en Fase 5) |
| Periodo fijo 2017-2018 | Patrones pueden no extrapolar a otros periodos |

## Archivo de entrada del modelo

`output/transition_matrix_probs.csv` — matriz validada en Fase 3, lista para Fases 4 y 5.
