"""
Dashboard de Atribución Multicanal — Olist Marketing Funnel
Generado desde Atribucion_Multicanal_Fases_1_2_3.ipynb (Fase 6)
Ejecutar: streamlit run streamlit_app.py
"""
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title='Atribución Multicanal Olist', layout='wide')
st.title('Atribución Multicanal — Olist Marketing Funnel')
st.caption('Modelo Markov (Removal Effect) + modelos baseline | Dataset: 8.000 MQLs, 842 conversiones')

# --- Carga de datos ---
@st.cache_data
def load_data():
    journeys = pd.read_csv(OUTPUT_DIR / 'journeys_dataset.csv')
    trans = pd.read_csv(OUTPUT_DIR / 'transition_matrix_probs.csv', index_col=0)
    comparison = pd.read_csv(OUTPUT_DIR / 'output/attribution_comparison.csv', index_col=0)
    scenarios = pd.read_csv(OUTPUT_DIR / 'output/scenario_simulations.csv'
    return journeys, trans, comparison, scenarios

journeys, trans_prob_app, comparison, scenarios = load_data()
TOTAL_CONV = int(journeys['converted'].sum())
ABSORBING = {'Conversion', 'Non_Conversion'}


def get_channels(pm):
    row = pm.loc['Start'].dropna()
    return [c for c in row.index if c not in ABSORBING and row[c] > 0]


def global_p_conv(pm, channels=None):
    channels = channels or get_channels(pm)
    return sum(pm.loc['Start', c] * pm.loc[c, 'Conversion'] for c in channels
               if c in pm.columns and c in pm.index)


def removal_effect_app(pm, channel, channels=None):
    channels = channels or get_channels(pm)
    p_base = global_p_conv(pm, channels)
    mat = pm.copy()
    mat.loc['Start', channel] = 0.0
    remaining = [c for c in channels if c != channel]
    s = mat.loc['Start', remaining].sum()
    if s > 0:
        mat.loc['Start', remaining] /= s
    p_without = global_p_conv(mat, remaining)
    return (p_base - p_without) / p_base if p_base > 0 else 0.0


CHANNELS = get_channels(trans_prob_app)
P_BASE = global_p_conv(trans_prob_app, CHANNELS)

# --- KPIs ---
col1, col2, col3, col4 = st.columns(4)
col1.metric('MQLs', f'{len(journeys):,}')
col2.metric('Conversiones', f'{TOTAL_CONV:,}')
col3.metric('Tasa global', f'{journeys["converted"].mean()*100:.2f}%')
col4.metric('P(conv) Markov', f'{P_BASE*100:.2f}%')

tab1, tab2, tab3, tab4 = st.tabs([
    'Comparativa de atribución', 'Journey (Sankey)', 'Grafo de transiciones', 'Simulador'
])

with tab1:
    st.subheader('Atribución por canal')
    st.dataframe(
        comparison[[
            'mqls', 'conversiones_reales', 'tasa_conv_pct',
            'atrib_first_touch', 'removal_effect', 'atrib_markov_norm'
        ]].style.format({
            'tasa_conv_pct': '{:.2f}%',
            'removal_effect': '{:.2%}',
            'atrib_markov_norm': '{:.1f}',
        }),
        use_container_width=True,
    )
    fig_bar = go.Figure()
    top = comparison.head(10)
    fig_bar.add_trace(go.Bar(
        name='Baseline (real)', x=top.index, y=top['conversiones_reales'], marker_color='#66c2a5'
    ))
    fig_bar.add_trace(go.Bar(
        name='Markov (norm.)', x=top.index, y=top['atrib_markov_norm'], marker_color='#fc8d62'
    ))
    fig_bar.update_layout(barmode='group', title='Conversiones atribuidas por canal', xaxis_tickangle=-45)
    st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    st.subheader('Sankey — Flujo Start → Canal → Resultado')
    start_row = trans_prob_app.loc['Start'].dropna()
    ch_cols = [c for c in start_row.index if c not in ABSORBING]
    labels = ['Start'] + list(ch_cols) + ['Conversion', 'Non_Conversion']
    label_idx = {l: i for i, l in enumerate(labels)}
    sources, targets, values = [], [], []
    for ch in ch_cols:
        v = start_row[ch] * len(journeys)
        if v > 0:
            sources.append(label_idx['Start'])
            targets.append(label_idx[ch])
            values.append(v)
        if ch in trans_prob_app.index:
            for end in ['Conversion', 'Non_Conversion']:
                if end in trans_prob_app.columns:
                    v2 = start_row[ch] * trans_prob_app.loc[ch, end] * len(journeys)
                    if v2 > 0:
                        sources.append(label_idx[ch])
                        targets.append(label_idx[end])
                        values.append(v2)
    fig_sankey = go.Figure(data=[go.Sankey(
        node=dict(label=labels, pad=15, thickness=18),
        link=dict(source=sources, target=targets, value=values),
    )])
    fig_sankey.update_layout(title='Journey agregado (volumen de MQLs)', height=500)
    st.plotly_chart(fig_sankey, use_container_width=True)

with tab3:
    st.subheader('Probabilidades de transición por canal')
    heat = trans_prob_app.loc[
        [c for c in CHANNELS if c in trans_prob_app.index],
        [c for c in ['Conversion', 'Non_Conversion'] if c in trans_prob_app.columns]
    ]
    fig_hm = go.Figure(data=go.Heatmap(
        z=heat.values, x=heat.columns, y=heat.index,
        colorscale='RdYlGn', text=np.round(heat.values, 3), texttemplate='%{text}',
    ))
    fig_hm.update_layout(title='P(canal → Conversion | Non_Conversion)', height=450)
    st.plotly_chart(fig_hm, use_container_width=True)

with tab4:
    st.subheader('Simulador de escenarios — Presupuesto por canal')
    st.write('Ajusta el peso relativo de entrada (Start → canal). Los pesos se normalizan automáticamente.')
    weights = {}
    cols = st.columns(3)
    for i, ch in enumerate(CHANNELS):
        default = float(trans_prob_app.loc['Start', ch]) if ch in trans_prob_app.columns else 0.0
        with cols[i % 3]:
            weights[ch] = st.slider(ch, 0.0, 1.0, default, 0.01, key=f'sl_{ch}')
    w_sum = sum(weights.values())
    if w_sum > 0:
        norm_w = {k: v / w_sum for k, v in weights.items()}
        mat_sim = trans_prob_app.copy()
        for ch, w in norm_w.items():
            mat_sim.loc['Start', ch] = w
        p_sim = global_p_conv(mat_sim, CHANNELS)
        st.metric('P(conversión) simulada', f'{p_sim*100:.2f}%')
        st.metric('Conversiones estimadas', f'{int(round(p_sim * len(journeys))):,}')
        delta = p_sim - P_BASE
        st.metric('Δ vs escenario base', f'{delta*100:+.2f} pp')
    else:
        st.warning('Asigna al menos un peso > 0 a algún canal.')

    st.divider()
    st.subheader('Escenarios pre-calculados (Fase 5)')
    st.dataframe(scenarios, use_container_width=True)

st.sidebar.markdown('### Documentación')
st.sidebar.info(
    '**Modelo:** Cadena de Markov orden 1 + Removal Effect.\n\n'
    '**Limitación:** un touchpoint por lead; baseline = Markov en ranking individual, '
    'pero Removal Effect mide impacto marginal del mix.\n\n'
    '**Fuente:** Olist Marketing Funnel (Kaggle).'
)
