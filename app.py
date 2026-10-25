"""Funcionalidad 1: Simulador dinámico de variables de entrada del CCE.

Ejecución:
    streamlit run app.py
"""

import plotly.graph_objects as go
import streamlit as st

from calculos import (
    ESCENARIOS,
    RANGOS,
    calcular_cce,
    clasificar_cce,
    todos_los_escenarios,
)
from estilos import CONVENCION, color, css_controles, signo

st.set_page_config(
    page_title="Simulador del Ciclo de Conversión de Efectivo",
    page_icon=":material/currency_exchange:",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Definición de las variables de entrada (RF-001)
# ---------------------------------------------------------------------------
VARIABLES = {
    "DIO": {
        "etiqueta": "Días de inventario (DIO)",
        "ayuda": "Days Inventory Outstanding: días promedio que el inventario "
        "permanece almacenado antes de venderse.",
        "valor_inicial": 45,
    },
    "DSO": {
        "etiqueta": "Días de cobro (DSO)",
        "ayuda": "Days Sales Outstanding: días promedio que tarda la empresa "
        "en cobrar sus ventas a crédito.",
        "valor_inicial": 30,
    },
    "DPO": {
        "etiqueta": "Días de pago (DPO)",
        "ayuda": "Days Payable Outstanding: días promedio que tarda la empresa "
        "en pagar a sus proveedores.",
        "valor_inicial": 20,
    },
}


def clave_slider(nombre: str) -> str:
    return f"{nombre.lower()}_slider"


def clave_numero(nombre: str) -> str:
    return f"{nombre.lower()}_numero"


# ---------------------------------------------------------------------------
# RF-003: sincronización entre slider y campo numérico.
# Los callbacks se ejecutan antes de dibujar los widgets, por lo que es
# seguro copiar el valor del control modificado hacia el otro control.
# ---------------------------------------------------------------------------
def sincronizar(origen: str, destino: str, nombre: str) -> None:
    valor = st.session_state[origen]
    # Si el usuario borra el campo numérico, el valor llega como None: se ignora.
    if valor is None:
        return
    limites = RANGOS[nombre]
    # Se restringe al rango permitido para mantener ambos controles coherentes.
    valor = max(limites["minimo"], min(limites["maximo"], int(valor)))
    st.session_state[origen] = valor
    st.session_state[destino] = valor


# Estado inicial: ambos controles de cada variable parten del mismo valor.
for nombre, datos in VARIABLES.items():
    st.session_state.setdefault(clave_slider(nombre), datos["valor_inicial"])
    st.session_state.setdefault(clave_numero(nombre), datos["valor_inicial"])


def crear_indicador(cce: float) -> go.Figure:
    """RF-006: medidor (gauge) que colorea el CCE según el rango."""
    # Eje visible del medidor. El valor numérico exacto se muestra siempre en
    # la tarjeta; fuera de este eje la aguja queda en el extremo.
    eje_min, eje_max = -100, 200

    # Tramos de color alineados con los límites definidos en calculos.py.
    limites = [eje_min] + [limite for limite, _ in ESCENARIOS] + [eje_max]
    escenarios = todos_los_escenarios()
    tramos = [
        {"range": [limites[i], limites[i + 1]], "color": escenarios[i].color_fondo}
        for i in range(len(escenarios))
    ]

    figura = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=cce,
            # El valor del CCE usa el azul de la convención de colores.
            number={"suffix": " días", "font": {"size": 44, "color": color("CCE")}},
            gauge={
                "axis": {"range": [eje_min, eje_max], "tickvals": [-100, 0, 30, 60, 90, 200]},
                "bar": {"color": "#1F2933", "thickness": 0.35},
                "steps": tramos,
                "borderwidth": 0,
            },
        )
    )
    figura.update_layout(height=300, margin={"l": 30, "r": 30, "t": 30, "b": 10})
    return figura


# ---------------------------------------------------------------------------
# Encabezado
# ---------------------------------------------------------------------------
st.title("Simulador del ciclo de conversión de efectivo")
st.caption(
    "Modifica los días de inventario, cobro y pago. El resultado se recalcula "
    "automáticamente con la fórmula **CCE = DIO + DSO − DPO**."
)

# ---------------------------------------------------------------------------
# RF-001, RF-002 y RF-003: controles (slider + campo numérico sincronizados)
# ---------------------------------------------------------------------------
st.subheader("Variables de entrada")

# Convención de colores: cada caja de entrada toma el color de su variable
# (DIO verde, DSO naranja, DPO morado). Ver estilos.py.
st.html(css_controles(list(VARIABLES)))

columnas_entrada = st.columns(3)

for columna, (nombre, datos) in zip(columnas_entrada, VARIABLES.items()):
    limites = RANGOS[nombre]
    with columna.container(border=True, key=f"caja_{nombre.lower()}"):
        st.slider(
            datos["etiqueta"],
            min_value=limites["minimo"],
            max_value=limites["maximo"],
            step=1,
            key=clave_slider(nombre),
            help=datos["ayuda"],
            on_change=sincronizar,
            args=(clave_slider(nombre), clave_numero(nombre), nombre),
        )
        st.number_input(
            f"Valor de {nombre} (días)",
            min_value=limites["minimo"],
            max_value=limites["maximo"],
            step=1,
            key=clave_numero(nombre),
            on_change=sincronizar,
            args=(clave_numero(nombre), clave_slider(nombre), nombre),
        )

# ---------------------------------------------------------------------------
# RF-004: cálculo automático (se ejecuta en cada interacción, sin botones)
# ---------------------------------------------------------------------------
dio = st.session_state[clave_slider("DIO")]
dso = st.session_state[clave_slider("DSO")]
dpo = st.session_state[clave_slider("DPO")]

cce = calcular_cce(dio, dso, dpo)
escenario = clasificar_cce(cce)

# ---------------------------------------------------------------------------
# RF-005, RF-006 y RN-001 a RN-005: resultado, color y mensaje
# ---------------------------------------------------------------------------
st.subheader("Resultado")
col_tarjeta, col_grafico = st.columns([1, 1], vertical_alignment="center")

with col_tarjeta:
    # Tarjeta destacada: se usa HTML porque Streamlit no ofrece una tarjeta
    # nativa con color de fondo configurable por valor.
    st.html(
        f"""
        <div style="background:{escenario.color_fondo}; color:{escenario.color_texto};
                    border-radius:12px; padding:24px 28px;">
            <div style="font-size:1rem; font-weight:600; opacity:0.9;">
                Ciclo de conversión de efectivo
            </div>
            <div style="font-size:3.6rem; font-weight:700; line-height:1.15;">
                {cce:,.0f} días
            </div>
            <div style="font-size:1.1rem; font-weight:600; margin-bottom:8px;">
                Escenario: {escenario.nombre} ({escenario.color_nombre})
            </div>
            <div style="font-size:1rem;">{escenario.mensaje}</div>
        </div>
        """
    )

with col_grafico:
    st.plotly_chart(
        crear_indicador(cce),
        key="grafico_cce",
        alt=f"Medidor del ciclo de conversión de efectivo: {cce:,.0f} días, "
        f"escenario {escenario.nombre}.",
    )

def bloque_resultado(componente: str, valor: float) -> str:
    """Tarjeta HTML de un componente con su color y signo de la convención."""
    datos = CONVENCION[componente]
    prefijo = f"{signo(componente)} " if signo(componente) else ""
    return f"""
    <div style="background:{datos['color']}; color:#FFFFFF; border-radius:12px;
                padding:16px 20px; height:100%;">
        <div style="font-size:0.9rem; font-weight:600; opacity:0.95;">
            {componente} · {datos['nombre']}
        </div>
        <div style="font-size:2.4rem; font-weight:700; line-height:1.2;">
            {prefijo}{valor:,.0f} días
        </div>
    </div>
    """


# Bloque de resultado: DIO + DSO - DPO = CCE, con colores y signos fijos.
st.subheader("Bloque de resultado")
bloques = st.columns(4)
for columna, (componente, valor) in zip(
    bloques, [("DIO", dio), ("DSO", dso), ("DPO", dpo), ("CCE", cce)]
):
    columna.html(bloque_resultado(componente, valor))

# Leyenda de rangos (referencia de RF-006)
with st.expander("Ver leyenda de rangos y colores"):
    st.table(
        {
            "Escenario": [e.nombre for e in todos_los_escenarios()],
            "Rango del CCE": [e.rango for e in todos_los_escenarios()],
            "Color": [e.color_nombre for e in todos_los_escenarios()],
        }
    )
