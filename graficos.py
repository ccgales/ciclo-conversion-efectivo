"""Gráficos Plotly de la aplicación.

Funcionalidad 2: gráfico de barras horizontales del ciclo de conversión de
efectivo (RF-007 a RF-011).
"""

import plotly.graph_objects as go

from estilos import color


def crear_grafico_barras(dio: float, dso: float, dpo: float, cce: float) -> go.Figure:
    """Construye el gráfico horizontal del CCE siguiendo el diseño conceptual.

    Orden de arriba hacia abajo (RF-011): CCE, Inventario, Cobro y Pago.

    Disposición de las barras (cascada), como en el diseño conceptual:
        - Inventario (DIO): inicia en 0.
        - Cobro (DSO):      inicia donde termina Inventario.
        - Pago (DPO):       inicia en 0.
        - CCE:              inicia donde termina Pago y llega hasta donde termina
                            Cobro; es decir, ocupa el tramo entre DPO y DIO + DSO.

    Así se aprecia cómo interactúan los componentes: el CCE es la parte del
    ciclo operativo (DIO + DSO) que el plazo de pago (DPO) no alcanza a cubrir.

    La longitud de cada barra es proporcional a su valor en días (RF-009).

    Estilo visual: gráfico limpio, sin eje X ni líneas guía; cada barra muestra
    su valor ("54 días") en blanco, alineado al extremo derecho dentro de la barra.
    """
    fin_cobro = dio + dso

    # Cada barra: (nombre en el eje, inicio, largo, valor mostrado, color).
    # Si el CCE es negativo (DPO > DIO + DSO), la barra ocupa igualmente el tramo
    # entre ambos extremos y la etiqueta muestra el valor con su signo.
    barras = [
        ("Ciclo de Conversión de Efectivo", min(dpo, fin_cobro), abs(cce), cce, color("CCE")),
        ("Días de Inventario", 0, dio, dio, color("DIO")),
        ("Días de Cuentas por Cobrar", dio, dso, dso, color("DSO")),
        ("Días de Cuentas por Pagar", 0, dpo, dpo, color("DPO")),
    ]

    # Mínimo de 10 días para evitar un eje sin longitud cuando todo vale cero.
    maximo = max(fin_cobro, dpo, 10)

    # Ancho mínimo (en días) para que el texto "NN días" quepa dentro de la barra.
    ancho_minimo_texto = maximo * 0.1

    figura = go.Figure()
    for nombre, inicio, largo, valor, color_barra in barras:
        cabe_dentro = largo >= ancho_minimo_texto
        figura.add_trace(
            go.Bar(
                y=[nombre],
                x=[largo],
                base=[inicio],
                orientation="h",
                marker={"color": color_barra},
                text=[f"{valor:,.0f} días"],
                # Texto blanco dentro de la barra, pegado a su extremo derecho.
                textposition="inside" if cabe_dentro else "outside",
                insidetextanchor="end",
                # Si la barra es demasiado corta (valores muy pequeños o cero), el
                # texto blanco no se vería sobre el fondo claro: se coloca fuera de
                # la barra en oscuro para que siga siendo legible.
                textfont={
                    "size": 16,
                    "color": "#FFFFFF" if cabe_dentro else "#1F2933",
                },
                constraintext="none",
                cliponaxis=False,
                hovertemplate=f"{nombre}<br>{valor:,.0f} días<extra></extra>",
                showlegend=False,
            )
        )

    figura.update_layout(
        height=280,
        margin={"l": 10, "r": 10, "t": 10, "b": 10},
        bargap=0.3,
        # Eje X oculto: la longitud de las barras y su etiqueta bastan para leerlo.
        xaxis={
            "visible": False,
            "range": [0, maximo * 1.02],
        },
        # Eje Y invertido: la primera barra (CCE) queda en la parte superior.
        yaxis={
            "title": {"text": "Componentes"},
            "autorange": "reversed",
            "tickfont": {"size": 12},
            "automargin": True,
        },
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return figura
