# Simulador del Ciclo de Conversión de Efectivo (CCE)

Implementación de la **Funcionalidad 1: Simulador dinámico de variables de entrada**, definida en `documentos/funcionalidades_proyecto_CCC.md`. La aplicación está desarrollada con Python, Streamlit y Plotly.

## Qué hace

El usuario modifica tres variables y la aplicación recalcula el resultado de forma automática, sin botones:

| Variable | Descripción | Rango (días) |
|----------|-------------|--------------|
| DIO | Días de inventario | 0 - 365 |
| DSO | Días de cobro | 0 - 365 |
| DPO | Días de pago | 0 - 365 |

**Fórmula:** `CCE = DIO + DSO − DPO`

## Estructura del proyecto

```
ciclo_conversion/
├── app.py              # Interfaz Streamlit y gráfico Plotly
├── calculos.py         # Fórmula, rangos, clasificación y mensajes (sin dependencias de UI)
├── estilos.py          # Convención de colores y signos del proyecto
├── requirements.txt    # Dependencias
└── documentos/         # Requerimientos funcionales
```

## Requerimientos cubiertos

| Código | Implementación |
|--------|----------------|
| RF-001 | Cada variable tiene un slider horizontal y un campo numérico editable. |
| RF-002 | Los rangos se definen en el diccionario `RANGOS` de `calculos.py` (0 a 365 por defecto). |
| RF-003 | Slider y campo numérico se sincronizan en ambos sentidos mediante callbacks sobre `st.session_state`. |
| RF-004 | El CCE se recalcula en cada cambio con `calcular_cce()`. |
| RF-005 | Tarjeta destacada con el CCE en días, más métricas de DIO, DSO, DPO y CCE. |
| RF-006 | La tarjeta y un medidor de Plotly se colorean según el rango del resultado. |
| RN-001 a RN-005 | Mensaje interpretativo automático según el escenario. |

### Convención de colores del proyecto

Cada componente del ciclo tiene un color fijo, que también se usa en las cajas de entrada (borde, etiquetas, marcador del slider y campo numérico) y en el bloque de resultado. **Esta convención se mantendrá en todas las funcionalidades futuras**; los valores están centralizados en `estilos.py`.

| Componente | Color | Hex | Signo en el bloque de resultado |
|------------|-------|-----|---------------------------------|
| DIO · Días de inventario | Verde | `#2E7D32` | (ninguno) |
| DSO · Días de cobro | Naranja | `#EF6C00` | `+` |
| DPO · Días de pago | Morado | `#7B1FA2` | `-` |
| CCE · Ciclo de conversión de efectivo | Azul | `#1565C0` | `=` |

El bloque de resultado se lee como la fórmula: `45 días`, `+ 30 días`, `- 20 días`, `= 55 días`.

Los colores del semáforo (RF-006) son independientes de esta convención y solo se usan en la tarjeta de interpretación y en el medidor.

### Rangos de color y escenarios

| CCE (días) | Escenario | Color |
|------------|-----------|-------|
| ≤ 0 | Excelente | Verde |
| 1 - 30 | Saludable | Verde claro |
| 31 - 60 | Moderado | Amarillo |
| 61 - 90 | Riesgo | Naranja |
| > 90 | Crítico | Rojo |

## Ejecución

Desde la carpeta del proyecto, con el entorno virtual activo:

```powershell
python -m venv .venv                  # solo la primera vez
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

La aplicación se abre en `http://localhost:8501`.

## Notas de diseño

- Valores iniciales: DIO = 45, DSO = 30, DPO = 20 (CCE = 55 días). Se pueden cambiar en el diccionario `VARIABLES` de `app.py`.
- El CCE puede ser negativo (por ejemplo, DPO mayor que DIO + DSO). Se interpreta como escenario **Excelente**.
- El medidor de Plotly muestra el eje de -100 a 200 días para que los tramos de color sean legibles. Si el CCE sale de ese eje, la aguja queda en el extremo, pero el valor exacto siempre se muestra en la tarjeta y en las métricas.
- Si el usuario borra el campo numérico, la aplicación conserva el último valor válido; los valores escritos fuera de rango se ajustan al mínimo o máximo permitido.
- La lógica financiera está separada de la interfaz en `calculos.py`, para reutilizarla en las siguientes funcionalidades (gráfico horizontal, línea temporal, escenarios, etc.).

## Alcance

Este entregable incluye únicamente la Funcionalidad 1. Las funcionalidades 2 a 7 del documento (gráfico de barras, línea temporal, indicadores, escenarios, recomendador y dashboard) quedan fuera de esta versión.
