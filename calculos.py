"""Lógica de negocio de la Funcionalidad 1: Simulador dinámico del CCE.

Este módulo no depende de Streamlit ni de Plotly, de modo que las reglas
financieras pueden probarse y reutilizarse en las siguientes funcionalidades.

Fórmula base:
    CCE = DIO + DSO - DPO
"""

from dataclasses import dataclass

# ---------------------------------------------------------------------------
# RF-002: rangos configurables de cada variable (en días).
# Para cambiar un rango basta con modificar este diccionario.
# ---------------------------------------------------------------------------
RANGOS = {
    "DIO": {"minimo": 0, "maximo": 365},
    "DSO": {"minimo": 0, "maximo": 365},
    "DPO": {"minimo": 0, "maximo": 365},
}


@dataclass(frozen=True)
class Escenario:
    """Describe un nivel de interpretación del CCE (RF-006 y RN-001 a RN-005)."""

    nombre: str
    rango: str  # Texto legible del intervalo, por ejemplo "1 - 30 días".
    color_nombre: str  # Nombre del color indicado en los requerimientos.
    color_fondo: str  # Color hexadecimal del indicador visual.
    color_texto: str  # Color de texto con buen contraste sobre el fondo.
    mensaje: str  # Mensaje interpretativo de la regla de negocio.


# Los escenarios se evalúan en orden: el primero cuyo límite superior
# cubra el valor del CCE es el que se aplica.
ESCENARIOS = [
    (
        0,
        Escenario(
            nombre="Excelente",
            rango="≤ 0 días",
            color_nombre="Verde",
            color_fondo="#1B8A3A",
            color_texto="#FFFFFF",
            mensaje=(
                "Excelente. La empresa recupera efectivo antes de tener que "
                "desembolsar recursos a proveedores."
            ),
        ),
    ),
    (
        30,
        Escenario(
            nombre="Saludable",
            rango="1 - 30 días",
            color_nombre="Verde claro",
            color_fondo="#8FD16A",
            color_texto="#1F2933",
            mensaje=(
                "El ciclo es eficiente y la recuperación del efectivo es rápida."
            ),
        ),
    ),
    (
        60,
        Escenario(
            nombre="Moderado",
            rango="31 - 60 días",
            color_nombre="Amarillo",
            color_fondo="#F6D743",
            color_texto="#1F2933",
            mensaje=(
                "El ciclo es aceptable, aunque existen oportunidades de "
                "optimización."
            ),
        ),
    ),
    (
        90,
        Escenario(
            nombre="Riesgo",
            rango="61 - 90 días",
            color_nombre="Naranja",
            color_fondo="#F28C28",
            color_texto="#1F2933",
            mensaje=(
                "Se recomienda revisar las políticas de inventario y cobranza."
            ),
        ),
    ),
]

# Escenario por defecto cuando el CCE supera el último límite (> 90 días).
ESCENARIO_CRITICO = Escenario(
    nombre="Crítico",
    rango="> 90 días",
    color_nombre="Rojo",
    color_fondo="#D32F2F",
    color_texto="#FFFFFF",
    mensaje=(
        "El efectivo permanece inmovilizado durante un periodo prolongado. "
        "Existe riesgo de presión sobre la liquidez."
    ),
)


def calcular_cce(dio: float, dso: float, dpo: float) -> float:
    """RF-004: calcula el Ciclo de Conversión de Efectivo.

    CCE = DIO + DSO - DPO
    """
    return dio + dso - dpo


def clasificar_cce(cce: float) -> Escenario:
    """Devuelve el escenario (color y mensaje) que corresponde al CCE."""
    for limite_superior, escenario in ESCENARIOS:
        if cce <= limite_superior:
            return escenario
    return ESCENARIO_CRITICO


def todos_los_escenarios() -> list[Escenario]:
    """Lista ordenada de todos los escenarios, útil para mostrar la leyenda."""
    return [escenario for _, escenario in ESCENARIOS] + [ESCENARIO_CRITICO]
