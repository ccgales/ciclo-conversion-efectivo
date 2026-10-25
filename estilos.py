"""Convención visual del proyecto (colores y signos de cada componente del CCE).

Esta convención se aplica a todas las funcionalidades de la aplicación:

    Componente                        Color     Signo en el bloque de resultado
    --------------------------------  --------  -------------------------------
    DIO - Días de inventario          Verde     (ninguno)
    DSO - Días de cobro               Naranja   +
    DPO - Días de pago                Morado    -
    CCE - Ciclo de conversión         Azul      =

Cualquier funcionalidad nueva (gráficos, línea temporal, escenarios, etc.)
debe importar los colores desde este módulo para mantener la coherencia.
"""

# Colores y signos por componente. Los textos claros/oscuros garantizan
# un buen contraste cuando el color se usa como fondo.
CONVENCION = {
    "DIO": {
        "nombre": "Días de inventario",
        "color_nombre": "Verde",
        "color": "#2E7D32",
        "color_suave": "#C8E6C9",
        "signo": "",
    },
    "DSO": {
        "nombre": "Días de cobro",
        "color_nombre": "Naranja",
        "color": "#EF6C00",
        "color_suave": "#FFE0B2",
        "signo": "+",
    },
    "DPO": {
        "nombre": "Días de pago",
        "color_nombre": "Morado",
        "color": "#7B1FA2",
        "color_suave": "#E1BEE7",
        "signo": "-",
    },
    "CCE": {
        "nombre": "Ciclo de conversión de efectivo",
        "color_nombre": "Azul",
        "color": "#1565C0",
        "color_suave": "#BBDEFB",
        "signo": "=",
    },
}


def color(componente: str) -> str:
    """Color principal (hexadecimal) de un componente: DIO, DSO, DPO o CCE."""
    return CONVENCION[componente]["color"]


def signo(componente: str) -> str:
    """Signo que antecede al valor en el bloque de resultado."""
    return CONVENCION[componente]["signo"]


def css_controles(componentes: list[str]) -> str:
    """Genera el CSS que colorea las cajas de entrada de cada variable.

    Cada caja se identifica por la clase `st-key-caja_<componente>` que
    Streamlit asigna automáticamente al contenedor con `key="caja_<...>"`.
    """
    reglas = []
    for nombre in componentes:
        c = CONVENCION[nombre]["color"]
        suave = CONVENCION[nombre]["color_suave"]
        caja = f".st-key-caja_{nombre.lower()}"
        reglas.append(
            f"""
{caja} {{
    border: 1px solid {c} !important;
    border-top: 6px solid {c} !important;
}}
{caja} label p, {caja} [data-testid="stWidgetLabel"] p {{
    color: {c} !important;
    font-weight: 600;
}}
{caja} [data-testid="stSliderThumbValue"] {{
    color: {c} !important;
    font-weight: 700;
}}
/* Marcador (thumb) del slider: contiene el input[type=range] oculto. */
{caja} [data-testid="stSlider"] div:has(> div > input[type="range"]) {{
    background-color: {c} !important;
}}
/* Riel del slider: elemento hermano anterior al marcador. */
{caja} [data-testid="stSlider"] div:has(+ div > div > input[type="range"]) {{
    background: {suave} !important;
}}
{caja} [data-testid="stNumberInput"] input {{
    color: {c} !important;
    font-weight: 700;
}}
{caja} [data-testid="stNumberInputContainer"] {{
    border-color: {c} !important;
}}
"""
        )
    return "<style>" + "\n".join(reglas) + "</style>"
