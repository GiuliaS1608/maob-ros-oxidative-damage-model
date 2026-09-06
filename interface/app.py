
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Cinética da MAO-B | Dinâmica Oxidativa",
    layout="wide"
)


st.markdown("""
<style>
    :root {
        --teal: #2E7D78;
        --teal-soft: rgba(46,125,120,0.12);
        --blue: #3A6EA5;
        --blue-soft: rgba(58,110,165,0.12);
        --amber: #B9852D;
        --amber-soft: rgba(185,133,45,0.12);
        --orange: #C46E35;
        --orange-soft: rgba(196,110,53,0.12);
        --red: #A64A4A;
        --red-soft: rgba(166,74,74,0.12);
        --border: rgba(90,90,90,0.34);
    }

    html, body, .stApp {
        font-family: "Trebuchet MS", "Segoe UI", Arial, sans-serif;
    }

    .main-title,
    .subtitle,
    .model-card,
    .model-small,
    .info-card,
    .scenário-card,
    .parameter-card,
    .summary-card,
    .chart-title,
    .sidebar-head,
    h1, h2, h3, h4, h5, h6,
    p, label {
        font-family: "Trebuchet MS", "Segoe UI", Arial, sans-serif;
    }

    .block-container {
        max-width: 1280px;
        padding-top: 3.25rem;
        padding-bottom: 3rem;
    }

    .hero {
        padding: 1.25rem 1.35rem;
        border-radius: 18px;
        background:
            linear-gradient(135deg, var(--teal-soft), rgba(128,128,128,0.04));
        border: 1.35px solid var(--border);
        margin-top: 0.45rem;
        margin-bottom: 1rem;
    }

    .main-title {
        font-size: 2.05rem;
        font-weight: 700;
        line-height: 1.22;
        margin: 0;
        letter-spacing: -0.02em;
    }

    .subtitle {
        margin-top: 0.45rem;
        font-size: 0.98rem;
        line-height: 1.5;
        opacity: 0.74;
        max-width: 900px;
    }

    .model-card {
        border-radius: 16px;
        padding: 1rem 0.7rem;
        min-height: 94px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        text-align: center;
        font-weight: 700;
        border: 1.35px solid var(--border);
        background: var(--secondary-background-color);
        white-space: nowrap;
    }

    .model-card.dopamine {
        border-top: 4px solid var(--blue);
        background: linear-gradient(180deg, var(--secondary-background-color), var(--blue-soft));
    }

    .model-card.maob {
        border-top: 4px solid var(--teal);
        background: linear-gradient(180deg, var(--secondary-background-color), var(--teal-soft));
    }

    .model-card.h2o2 {
        border-top: 4px solid var(--amber);
        background: linear-gradient(180deg, var(--secondary-background-color), var(--amber-soft));
    }

    .model-card.ros {
        border-top: 4px solid var(--orange);
        background: linear-gradient(180deg, var(--secondary-background-color), var(--orange-soft));
    }

    .model-card.damage {
        border-top: 4px solid var(--red);
        background: linear-gradient(180deg, var(--secondary-background-color), var(--red-soft));
    }

    .model-small {
        font-size: 0.80rem;
        opacity: 0.65;
        margin-top: 0.18rem;
        font-weight: 500;
    }

    .arrow-box {
        min-height: 94px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        opacity: 0.45;
    }

    .info-card,
    .scenário-card,
    .parameter-card,
    .result-card {
        background: var(--secondary-background-color);
        border: 1.35px solid var(--border);
        border-radius: 15px;
    }

    .info-card {
        padding: 0.85rem;
        text-align: center;
    }

    .info-card-title {
        font-size: 1rem;
        font-weight: 700;
    }

    .info-card-text {
        font-size: 0.82rem;
        opacity: 0.68;
        margin-top: 0.15rem;
    }

    .scenário-card {
        padding: 1rem 1.05rem;
        border-left: 5px solid var(--teal);
        margin-bottom: 0.6rem;
    }

    .parameter-card {
        padding: 0.58rem 0.72rem;
        min-height: 72px;
        margin-bottom: 0.45rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    .parameter-label {
        font-size: 0.78rem;
        opacity: 0.68;
        margin-bottom: 0.18rem;
    }

    .parameter-value {
        font-size: 1.12rem;
        font-weight: 600;
        line-height: 1.10;
        white-space: nowrap;
    }

    .summary-card {
        background: var(--secondary-background-color);
        border: 1.35px solid var(--border);
        border-radius: 13px;
        padding: 0.58rem 0.72rem;
        min-height: 72px;
        margin-bottom: 0.45rem;
    }

    .summary-label {
        font-size: 0.78rem;
        opacity: 0.68;
        margin-bottom: 0.18rem;
    }

    .summary-value {
        font-size: 1.12rem;
        font-weight: 600;
        line-height: 1.10;
        white-space: nowrap;
    }

    .chart-title {
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
        opacity: 0.90;
    }

    .chart-tag {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        margin-right: 0.4rem;
        vertical-align: middle;
    }

    .tag-blue { background: var(--blue); }
    .tag-amber { background: var(--amber); }
    .tag-orange { background: var(--orange); }
    .tag-red { background: var(--red); }

    .result-card {
        padding: 0.75rem 0.85rem 0.5rem 0.85rem;
        margin-bottom: 0.8rem;
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid var(--border);
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
    }

    .sidebar-head {
        padding: 0.8rem 0.9rem;
        border-radius: 14px;
        background: linear-gradient(135deg, var(--teal-soft), rgba(128,128,128,0.03));
        border: 1.35px solid var(--border);
        margin-bottom: 0.9rem;
    }

    .sidebar-head-title {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }

    .sidebar-head-text {
        font-size: 0.82rem;
        opacity: 0.68;
        line-height: 1.4;
    }

    div[data-testid="stMetric"] {
        background: var(--secondary-background-color);
        border: 1.35px solid var(--border);
        border-radius: 14px;
        padding: 0.8rem;
    }

    div[data-testid="stExpander"] {
        border-radius: 13px;
        border-color: var(--border);
    }

    .stAlert {
        border-radius: 14px;
    }

    h2, h3 {
        letter-spacing: -0.01em;
    }

    .equation-gap {
        height: 0.55rem;
    }

    .sidebar-section-title {
        font-size: 0.80rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        opacity: 0.60;
        margin-top: 0.55rem;
        margin-bottom: 0.30rem;
    }

    section[data-testid="stSidebar"] .stButton > button,
    section[data-testid="stSidebar"] div[role="radiogroup"] > label,
    section[data-testid="stSidebar"] div[data-testid="stToggle"] {
        border-radius: 10px;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] > div,
    section[data-testid="stSidebar"] div[data-testid="stExpander"] {
        border-color: rgba(90,90,90,0.34);
    }

    section[data-testid="stSidebar"] {
        border-right: 1.3px solid rgba(90,90,90,0.28);
    }

    .sidebar-head {
        padding: 0.65rem 0.15rem 0.35rem 0.15rem;
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
        margin-bottom: 0.45rem;
    }

    .sidebar-head-title {
        font-size: 1.08rem;
        font-weight: 700;
        margin-bottom: 0.12rem;
    }

    .sidebar-head-text {
        font-size: 0.80rem;
        opacity: 0.62;
        line-height: 1.35;
    }

    .sidebar-minimal-title {
        font-size: 1.28rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        margin-bottom: 0.18rem;
    }

    .sidebar-minimal-text {
        font-size: 0.82rem;
        line-height: 1.42;
        opacity: 0.62;
        margin-bottom: 1.15rem;
        max-width: 245px;
    }

    .sidebar-field-label {
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.045em;
        text-transform: uppercase;
        opacity: 0.58;
        margin-top: 0.20rem;
        margin-bottom: 0.40rem;
    }

    .sidebar-rule {
        height: 1px;
        background: rgba(128,128,128,0.24);
        margin: 1.05rem 0 0.95rem 0;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        border: 1.35px solid rgba(105,105,105,0.34);
        border-radius: 10px;
        min-height: 42px;
    }

    section[data-testid="stSidebar"] div[data-testid="stSlider"] {
        padding-top: 0.15rem;
    }

    section[data-testid="stSidebar"] div[data-testid="stCheckbox"] {
        margin-top: 0.65rem;
    }

    section[data-testid="stSidebar"] div[data-testid="stExpander"] {
        border: 1.2px solid rgba(105,105,105,0.28);
        border-radius: 10px;
        margin-bottom: 0.35rem;
    }

    section[data-testid="stSidebar"] .sidebar-head {
        display: none;
    }

    .mediator-arrow {
        min-height: 94px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        line-height: 1.05;
    }

    .mediator-label {
        font-size: 0.88rem;
        font-weight: 700;
        opacity: 0.90;
        margin-bottom: 0.10rem;
    }

    .mediator-sub {
        font-size: 0.68rem;
        opacity: 0.58;
        white-space: nowrap;
        margin-bottom: 0.20rem;
    }

    .mediator-symbol {
        font-size: 1.45rem;
        opacity: 0.48;
    }

    .scenário-explanation {
        margin-top: 0.45rem;
        padding: 0.90rem 1rem;
        border: 1.35px solid rgba(90,90,90,0.28);
        border-radius: 13px;
        background: var(--secondary-background-color);
        line-height: 1.5;
    }

    .scenário-explanation-title {
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.035em;
        text-transform: uppercase;
        opacity: 0.60;
        margin-bottom: 0.30rem;
    }

    .scenário-explanation-text {
        font-size: 0.90rem;
        opacity: 0.84;
    }
</style>
""", unsafe_allow_html=True)


BASAL = {
    "Km": 229.0,
    "Vmax": 100.0,
    "P": 50.0,
    "Ks": 0.7,
    "alpha": 1.0,
    "Kh": 0.5,
    "beta": 0.8,
    "Kr": 0.7,
    "gamma": 0.6,
    "Kd": 0.9,
    "S0": 200.0,
    "H0": 0.0,
    "R0": 0.0,
    "D0": 0.0,
}


SCENARIOS = {
    "Basal": {},
    "Atividade MAO-B aumentada": {"Vmax": 500.0},
    "Produção aumentada de dopamina": {"P": 90.0},
    "Deficiência antioxidante": {"Kh": 0.2, "Kr": 0.3},
    "Reparo reduzido": {"Kd": 0.2},
}


SCENARIO_INFO = {
    "Basal": {
        "alteracao": "Nenhuma alteração: valores de referência.",
        "observar": "Observe a aproximação das quatro variáveis a um regime estacionário."
    },
    "Atividade MAO-B aumentada": {
        "alteracao": "Vmax*: 100 -> 500 \u00b5M min\u207b\u00b9.",
        "observar": "Observe a queda mais intensa de dopamina e a elevação subsequente de H\u2082O\u2082, ROS e dano."
    },
    "Produção aumentada de dopamina": {
        "alteracao": "P: 50 -> 90 \u00b5M min\u207b\u00b9.",
        "observar": "Observe o maior nível de dopamina e como a maior disponibilidade de substrato intensifica a cascata."
    },
    "Deficiência antioxidante": {
        "alteracao": "Kh: 0,5 -> 0,2 min\u207b\u00b9 e Kr: 0,7 -> 0,3 min\u207b\u00b9.",
        "observar": "Observe que a dopamina quase não muda, enquanto H\u2082O\u2082, ROS e dano permanecem mais elevados."
    },
    "Reparo reduzido": {
        "alteracao": "Kd: 0,9 -> 0,2 min\u207b\u00b9.",
        "observar": "Observe que S(t), H(t) e R(t) permanecem semelhantes ao basal, mas D(t) aumenta."
    },
    "Personalizado": {
        "alteracao": "Definida pelo usuário.",
        "observar": "Compare com o basal e identifique em qual etapa da cascata a perturbação aparece primeiro."
    },
}


def derivadas(y, p):
    S, H, R, D = y
    v_maob = p["Vmax"] * S / (p["Km"] + S)

    dS = p["P"] - v_maob - p["Ks"] * S
    dH = p["alpha"] * v_maob - p["Kh"] * H
    dR = p["beta"] * H - p["Kr"] * R
    dD = p["gamma"] * R - p["Kd"] * D

    return np.array([dS, dH, dR, dD], dtype=float)


def rk4(p, t_final=20.0, h=0.05):
    n = int(round(t_final / h)) + 1
    t = np.linspace(0.0, t_final, n)
    y = np.zeros((n, 4), dtype=float)
    y[0] = [p["S0"], p["H0"], p["R0"], p["D0"]]

    for i in range(n - 1):
        yi = y[i]
        k1 = derivadas(yi, p)
        k2 = derivadas(yi + h * k1 / 2.0, p)
        k3 = derivadas(yi + h * k2 / 2.0, p)
        k4 = derivadas(yi + h * k3, p)
        y[i + 1] = yi + h * (k1 + 2*k2 + 2*k3 + k4) / 6.0

    return t, y


def interpretar(cenário):
    textos = {
        "Basal":
            "No cenário basal, as variáveis tendem a um regime estacionário determinado pelo balanço entre produção e remoção. "
            "O sistema representa uma condição de referência em que a dinâmica oxidativa permanece controlada.",

        "Atividade MAO-B aumentada":
            "O aumento de Vmax* intensifica o consumo de dopamina pela MAO-B. Como a formação de H\u2082O\u2082 depende da atividade enzimática, "
            "essa perturbação é transmitida para as etapas seguintes, elevando ROS e dano oxidativo.",

        "Produção aumentada de dopamina":
            "O aumento de P eleva a disponibilidade de dopamina. Com mais substrato disponível, aumenta o fluxo pela reação mediada pela MAO-B, "
            "favorecendo maior formação de H\u2082O\u2082, ROS e dano oxidativo.",

        "Deficiência antioxidante":
            "A redução de Kh e Kr diminui a remoção de H\u2082O\u2082 e a neutralização de ROS. Assim, a carga oxidativa permanece elevada por mais tempo, "
            "mesmo sem alteração direta na dinâmica da dopamina.",

        "Reparo reduzido":
            "A redução de Kd diminui a remoção do dano já formado. Como Kd atua apenas na equação de D(t), as trajetórias de dopamina, H\u2082O\u2082 e ROS "
            "permanecem semelhantes ao basal, enquanto o dano oxidativo aumenta.",

        "Personalizado":
            "No modo personalizado, a interpretação depende dos parâmetros modificados. Compare as curvas com o basal e observe em qual variável "
            "a diferença aparece primeiro; isso ajuda a identificar como a perturbação se propaga pela cascata."
    }
    return textos[cenário]


def percentual(final, basal_final):
    if np.isclose(basal_final, 0.0):
        return None
    return 100.0 * (final - basal_final) / basal_final



SCENARIO_EXPLANATIONS = {
    "Basal": (
        "Representa a condição de referência do modelo, com os parâmetros basais. "
        "A dinâmica tende a um regime estável, servindo como base para comparar os demais cenários."
    ),
    "Atividade MAO-B aumentada": (
        "Simula aumento da atividade da MAO-B por meio do aumento de Vmax*. "
        "Com maior capacidade de metabolização da dopamina, cresce a formação de H2O2, "
        "o que eleva ROS e, consequentemente, o dano oxidativo."
    ),
    "Produção aumentada de dopamina": (
        "Simula maior entrada de dopamina no sistema pelo aumento de P. "
        "A maior disponibilidade de substrato sustenta a reação mediada pela MAO-B e pode intensificar "
        "a cascata H2O2 → ROS → dano oxidativo."
    ),
    "Deficiência antioxidante": (
        "Simula redução da capacidade de remoção de H2O2 e de neutralização de ROS, "
        "com menores valores de Kh e Kr. A dopamina tende a permanecer próxima do comportamento basal, "
        "enquanto H2O2, ROS e dano oxidativo permanecem mais elevados."
    ),
    "Reparo reduzido": (
        "Simula menor capacidade de reparo ou remoção do dano oxidativo por redução de Kd. "
        "Nesse cenário, a dinâmica de dopamina, H2O2 e ROS permanece essencialmente igual à basal, "
        "mas o dano oxidativo se acumula mais."
    ),
    "Personalizado": (
        "Permite alterar manualmente os parâmetros do modelo para explorar combinações não contempladas "
        "nos cenários prontos e observar como cada modificação afeta a dinâmica do sistema."
    ),
}

st.sidebar.markdown(
    """
    <div class="sidebar-minimal-title">Simulação</div>
    <div class="sidebar-minimal-text">
        Configure o cenário e o tempo antes de explorar os resultados.
    </div>
    """,
    unsafe_allow_html=True
)

opcoes = [
    "Basal",
    "Atividade MAO-B aumentada",
    "Produção aumentada de dopamina",
    "Deficiência antioxidante",
    "Reparo reduzido",
    "Personalizado"
]

st.sidebar.markdown(
    '<div class="sidebar-field-label">Cenário</div>',
    unsafe_allow_html=True
)

cenário = st.sidebar.selectbox(
    "Cenário",
    options=opcoes,
    index=0,
    label_visibility="collapsed"
)

p = BASAL.copy()

if cenário != "Personalizado":
    p.update(SCENARIOS.get(cenário, {}))


if cenário == "Personalizado":
    st.sidebar.markdown('<div class="sidebar-rule"></div>', unsafe_allow_html=True)
    st.sidebar.markdown(
        '<div class="sidebar-field-label">Parâmetros personalizados</div>',
        unsafe_allow_html=True
    )

    with st.sidebar.expander("Dopamina", expanded=True):
        p["Vmax"] = st.slider(
            "Vmax*",
            min_value=10.0,
            max_value=600.0,
            value=100.0,
            step=10.0,
            help="Atividade efetiva da MAO-B."
        )
        st.caption("Maior Vmax* intensifica o consumo de dopamina pela MAO-B.")

        p["P"] = st.slider(
            "P",
            min_value=0.0,
            max_value=120.0,
            value=50.0,
            step=5.0,
            help="Taxa de produção basal de dopamina."
        )
        st.caption("Maior P aumenta a entrada/produção de dopamina no sistema.")

        p["Ks"] = st.slider(
            r"$K_s$",
            min_value=0.0,
            max_value=2.0,
            value=0.7,
            step=0.05,
            help="Constante de remoção fisiológica de dopamina por vias adicionais à MAO-B."
        )
        st.caption("Maior Ks aumenta a remoção de dopamina por mecanismos representados fora da reação da MAO-B.")

    with st.sidebar.expander("H\u2082O\u2082"):
        p["alpha"] = st.slider(
            "alpha",
            0.0, 2.0, 1.0, 0.05,
            help="Fator efetivo que relaciona a atividade da MAO-B à formação de H\u2082O\u2082."
        )
        st.caption(r"$\alpha$ controla quanto da atividade da MAO-B é traduzida em formação de $H_2O_2$.")

        p["Kh"] = st.slider(
            r"$K_h$",
            0.05, 1.5, 0.5, 0.05,
            help="Constante efetiva de remoção de H\u2082O\u2082."
        )
        st.caption(r"Maior Kh representa remoção mais rápida de $H_2O_2$; menor Kh representa menor capacidade antioxidante nessa etapa.")

    with st.sidebar.expander("ROS"):
        p["beta"] = st.slider(
            "beta",
            0.0, 2.0, 0.8, 0.05,
            help="Fator efetivo de formação de ROS a partir de H\u2082O\u2082."
        )
        st.caption(r"$\beta$ controla a intensidade com que $H_2O_2$ contribui para a formação de ROS.")

        p["Kr"] = st.slider(
            r"$K_r$",
            0.05, 1.5, 0.7, 0.05,
            help="Constante efetiva de neutralização de ROS."
        )
        st.caption("Maior Kr representa neutralização mais rápida de ROS; menor Kr favorece sua persistência.")

    with st.sidebar.expander("Dano e reparo"):
        p["gamma"] = st.slider(
            "gamma",
            0.0, 2.0, 0.6, 0.05,
            help="Fator efetivo que relaciona ROS à formação de dano oxidativo."
        )
        st.caption(r"$\gamma$ controla quanto o nível de ROS contribui para a geração de dano oxidativo.")

        p["Kd"] = st.slider(
            r"$K_d$",
            0.05, 1.5, 0.9, 0.05,
            help="Constante efetiva de reparo ou remoção do dano oxidativo."
        )
        st.caption("Maior Kd representa reparo/remoção mais eficiente; menor Kd favorece o acúmulo de dano.")

    with st.sidebar.expander("Condição inicial"):
        p["S0"] = st.slider(
            "S(0)",
            0.0, 500.0, 200.0, 10.0,
            help="Concentração inicial de dopamina usada no início da simulação."
        )
        st.caption("S(0) define a concentração de dopamina no instante inicial da simulação.")


default_t = 20.0 if cenário in ["Deficiência antioxidante", "Reparo reduzido"] else 10.0

st.sidebar.markdown('<div class="sidebar-rule"></div>', unsafe_allow_html=True)
st.sidebar.markdown(
    '<div class="sidebar-field-label">Tempo de simulação</div>',
    unsafe_allow_html=True
)

t_final = st.sidebar.slider(
    "Tempo final da simulação (min)",
    min_value=5.0,
    max_value=30.0,
    value=default_t,
    step=1.0,
    label_visibility="collapsed"
)

st.sidebar.caption(f"{t_final:.0f} min")

comparar = st.sidebar.checkbox(
    "Comparar com cenário basal",
    value=True
)


st.markdown(
    """
    <div class="hero">
        <div class="main-title">Simulador de Cinética da MAO-B e Dinâmica Oxidativa</div>
        <div class="subtitle">
            <b>Modelo dinâmico e semiquantitativo da produção de ROS e do dano oxidativo.</b><br>
            Explore como alterações na atividade da MAO-B, na disponibilidade de dopamina,
            na defesa antioxidante e no reparo celular modificam a dinâmica temporal do sistema.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="scenário-card">
        Modelo dinâmico e semiquantitativo: H<sub>2</sub>O<sub>2</sub>, ROS e dano oxidativo
        são índices relativos em unidades arbitrárias, e não concentrações intracelulares absolutas.
    </div>
    """,
    unsafe_allow_html=True
)


st.subheader("Estrutura do modelo")

c1, a1, c2, a2, c3, a3, c4 = st.columns(
    [1.45, 0.62, 1.45, 0.34, 1.45, 0.34, 1.45]
)

with c1:
    st.markdown(
        '<div class="model-card dopamine">Dopamina<div class="model-small">S(t)</div></div>',
        unsafe_allow_html=True
    )

with a1:
    st.markdown(
        """
        <div class="mediator-arrow">
            <div class="mediator-label">MAO-B</div>
            <div class="mediator-sub">Michaelis-Menten</div>
            <div class="mediator-symbol">→</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        '<div class="model-card h2o2"><span class="chem-formula">H<sub>2</sub>O<sub>2</sub></span><div class="model-small">H(t)</div></div>',
        unsafe_allow_html=True
    )

with a2:
    st.markdown('<div class="arrow-box">→</div>', unsafe_allow_html=True)

with c3:
    st.markdown(
        '<div class="model-card ros">ROS<div class="model-small">R(t)</div></div>',
        unsafe_allow_html=True
    )

with a3:
    st.markdown('<div class="arrow-box">→</div>', unsafe_allow_html=True)

with c4:
    st.markdown(
        '<div class="model-card damage">Dano oxidativo<div class="model-small">D(t)</div></div>',
        unsafe_allow_html=True
    )



st.write("")

r1, r2, r3 = st.columns(3)

with r1:
    st.markdown(
        '<div class="info-card"><div class="info-card-title">K<sub>h</sub></div>'
        '<div class="info-card-text">remoção de H<sub>2</sub>O<sub>2</sub></div></div>',
        unsafe_allow_html=True
    )

with r2:
    st.markdown(
        '<div class="info-card"><div class="info-card-title">K<sub>r</sub></div>'
        '<div class="info-card-text">neutralização de ROS</div></div>',
        unsafe_allow_html=True
    )

with r3:
    st.markdown(
        '<div class="info-card"><div class="info-card-title">K<sub>d</sub></div>'
        '<div class="info-card-text">reparo/remoção do dano</div></div>',
        unsafe_allow_html=True
    )


st.markdown('<div class="equation-gap"></div>', unsafe_allow_html=True)

with st.expander("Ver sistema de equações"):
    st.latex(r"\frac{dS}{dt}=P-\frac{V_{\max}^{*}S}{K_m+S}-K_sS")
    st.latex(r"\frac{dH}{dt}=\alpha\frac{V_{\max}^{*}S}{K_m+S}-K_hH")
    st.latex(r"\frac{dR}{dt}=\beta H-K_rR")
    st.latex(r"\frac{dD}{dt}=\gamma R-K_dD")


st.subheader("Cenário selecionado")

st.markdown(
    f"""
    <div class="scenário-explanation">
        <div class="scenário-explanation-title">O que este cenário representa</div>
        <div class="scenário-explanation-text">{SCENARIO_EXPLANATIONS[cenário]}</div>
    </div>
    """,
    unsafe_allow_html=True
)



st.markdown(
    f"""
    <div class="scenário-card">
        <b>{cenário}</b><br>
        <span style="opacity:0.72">{SCENARIO_INFO[cenário]["alteracao"]}</span>
        <br><br>
        <b>O que observar</b><br>
        <span style="opacity:0.72">{SCENARIO_INFO[cenário]["observar"]}</span>
    </div>
    """,
    unsafe_allow_html=True
)


if cenário != "Personalizado":
    st.subheader("Parâmetros do cenário")

    cols = st.columns(4)

    labels_html = {
        "Km": "K<sub>m</sub>",
        "Vmax*": "V<sub>max</sub>*",
        "P": "P",
        "Ks": "K<sub>s</sub>",
        "Kh": "K<sub>h</sub>",
        "Kr": "K<sub>r</sub>",
        "Kd": "K<sub>d</sub>",
        "S(0)": "S(0)",
    }

    parâmetros = [
        ("Km", p["Km"], "\u00b5M"),
        ("Vmax*", p["Vmax"], "\u00b5M min\u207b\u00b9"),
        ("P", p["P"], "\u00b5M min\u207b\u00b9"),
        ("Ks", p["Ks"], "min\u207b\u00b9"),
        ("Kh", p["Kh"], "min\u207b\u00b9"),
        ("Kr", p["Kr"], "min\u207b\u00b9"),
        ("Kd", p["Kd"], "min\u207b\u00b9"),
        ("S(0)", p["S0"], "\u00b5M"),
    ]

    cols = st.columns(4)
    for i, (nome, valor, unidade) in enumerate(parâmetros):
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class="parameter-card">
                    <div class="parameter-label">{labels_html[nome]}</div>
                    <div class="parameter-value">{valor:g} {unidade}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

# Integra o cenário selecionado e o cenário basal no mesmo intervalo de tempo.
t, y = rk4(p, t_final=t_final, h=0.05)
t_b, y_b = rk4(BASAL, t_final=t_final, h=0.05)

st.subheader("Resultados")

nomes = [
    ("Dopamina S(t)", "\u00b5M"),
    ("H\u2082O\u2082 H(t)", "u.a."),
    ("ROS R(t)", "u.a."),
    ("Dano oxidativo D(t)", "u.a.")
]

grid = [
    st.columns(2),
    st.columns(2)
]


chart_colors = ["#3A6EA5", "#B9852D", "#C46E35", "#A64A4A"]
tag_classes = ["tag-blue", "tag-amber", "tag-orange", "tag-red"]

for idx, (titulo, unidade) in enumerate(nomes):
    fig, ax = plt.subplots(figsize=(5.0, 2.55))

    bg = st.get_option("theme.backgroundColor")
    secondary = st.get_option("theme.secondaryBackgroundColor")
    text_color = st.get_option("theme.textColor")

    if bg:
        fig.patch.set_facecolor(bg)

    if secondary:
        ax.set_facecolor(secondary)

    if text_color:
        ax.tick_params(colors=text_color)
        ax.xaxis.label.set_color(text_color)
        ax.yaxis.label.set_color(text_color)
        for spine in ax.spines.values():
            spine.set_color(text_color)
            spine.set_alpha(0.18)

    if comparar:
        ax.plot(
            t_b,
            y_b[:, idx],
            linestyle="--",
            linewidth=1.5,
            color="#8A8A8A",
            label="Basal"
        )

    ax.plot(
        t,
        y[:, idx],
        linewidth=2.2,
        color=chart_colors[idx],
        label=cenário
    )

    ax.set_xlabel("Tempo (min)", fontsize=8.5)
    ax.set_ylabel(unidade, fontsize=8.5)
    ax.tick_params(axis="both", labelsize=7.8)
    ax.grid(alpha=0.12, linewidth=0.7)

    legend = ax.legend(frameon=False, fontsize=7.3, loc="best")
    if text_color:
        for txt in legend.get_texts():
            txt.set_color(text_color)

    fig.tight_layout()

    row = 0 if idx < 2 else 1
    col = idx if idx < 2 else idx - 2

    with grid[row][col]:
        st.markdown(
            f"""
            <div class="result-card">
                <div class="chart-title">
                    <span class="chart-tag {tag_classes[idx]}"></span>{titulo}
                </div>
            """,
            unsafe_allow_html=True
        )
        st.pyplot(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    plt.close(fig)


st.subheader("Resumo numérico")

summary_items = [
    ("Dopamina final", y[-1, 0], "\u00b5M"),
    ("H\u2082O\u2082 final", y[-1, 1], "u.a."),
    ("ROS final", y[-1, 2], "u.a."),
    ("Dano final", y[-1, 3], "u.a."),
]

summary_cols = st.columns(4)
for i, (label, value, unit) in enumerate(summary_items):
    with summary_cols[i]:
        st.markdown(
            f"""
            <div class="summary-card">
                <div class="summary-label">{label}</div>
                <div class="summary-value">{value:.2f} {unit}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.subheader("Interpretação didática")

st.success(interpretar(cenário))

st.markdown(
    """
    **Como ler os resultados:** procure primeiro a variável em que a curva do cenário selecionado
    começa a se afastar da curva basal. Isso ajuda a identificar onde a perturbação foi introduzida
    e como seu efeito é transmitido ao longo do sistema.
    """
)


with st.expander("Sobre o caráter semiquantitativo do modelo"):
    st.write(
        "H\u2082O\u2082, ROS e dano oxidativo são representados em unidades arbitrárias. "
        "Assim, os valores devem ser interpretados como índices relativos para comparação entre cenários, "
        "e não como concentrações intracelulares absolutas."
    )

    st.write(
        "O passo numérico utilizado é h = 0,05 min e a integração é realizada "
        "pelo método de Runge-Kutta de quarta ordem (RK4)."
    )


st.caption(
    "Interface didática baseada no modelo matemático da produção de espécies reativas de oxigênio mediada pela MAO-B."
)
