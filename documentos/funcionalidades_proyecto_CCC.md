# Documento de Requerimientos Funcionales del Proyecto

Este documento describe las funcionalidades que desarrollaremos en el proyecto *Ciclo Conversión Efectivo CCC*, utilizando *Cursor AI* como entorno de desarrollo.  

El enfoque que seguimos es pedagógico: queremos ilustrar cómo un proyecto puede dividirse en distintas etapas (sprints), cada una con un entregable funcional. En un entorno real, muchas de estas funcionalidades podrían desarrollarse de forma iterativa o integrada, pero aquí las mantendremos separadas para fines de enseñanza.

---

## Aplicación de Simulación del Ciclo de Conversión de Efectivo (CCE)

## 1. Introducción

El objetivo de la aplicación es proporcionar una herramienta interactiva y didáctica que permita a usuarios financieros, analistas, gerentes y estudiantes simular el comportamiento del Ciclo de Conversión de Efectivo (CCE) mediante la manipulación dinámica de sus variables y la visualización gráfica inmediata de los resultados.

La aplicación deberá facilitar el análisis del impacto que tienen los días de inventario, los días de cobranza y los días de pago sobre la liquidez operacional de una empresa.

---

## 2. Objetivos de Negocio
1. Comprender el comportamiento del Ciclo de Conversión de Efectivo.
2. Identificar oportunidades de optimización del capital de trabajo.
3. Evaluar escenarios financieros hipotéticos.
4. Facilitar procesos de capacitación financiera.
5. Permitir simulaciones en tiempo real sin requerir conocimientos avanzados de análisis financiero.

---

## 3. Fórmula Base
La aplicación utilizará la fórmula estándar:
CCE = DIO + DSO − DPO

Donde:
Variable	Descripción
1. DIO	    Days Inventory Outstanding (Días de Inventario)
2. DSO	    Days Sales Outstanding (Días de Cobro)
3. DPO	    Days Payable Outstanding (Días de Pago)

---

## 4. Arquitectura Funcional
La solución estará dividida en módulos funcionales independientes para facilitar la evolución futura del producto.


# Funcionalidad 1

## Simulador Dinámico de Variables de Entrada
Objetivo:
Permitir al usuario modificar los componentes del ciclo mediante controles intuitivos y observar en tiempo real el impacto sobre el resultado final.

---

## Requerimientos Funcionales

### RF-001 Ingreso Dinámico de Variables
El sistema deberá permitir modificar:
1. Días de Inventario (DIO)
2. Días de Cobro (DSO)
3. Días de Pago (DPO)

mediante:
1. Slider horizontal
2. Campo numérico editable

### RF-002 Rangos Configurables
Los sliders deberán permitir configurar
Variable	Mínimo	Máximo
1. DIO	        0	    365
2. DSO	        0	    365
3. DPO	        0	    365

### RF-003 Sincronización
Cuando el usuario:
1. Modifique el slider el valor numérico deberá actualizarse automáticamente.
Cuando modifique el valor numérico:
2. El slider deberá moverse automáticamente.

### RF-004 Cálculo Automático
Cada vez que cambie una variable, el sistema deberá recalcular
CCE = DIO + DSO - DPO
sin necesidad de presionar botones

### RF-005 Visualización del Resultado
Mostrar:
Ciclo de Conversión de Efectivo
45 días en una tarjeta destacada

### RF-006 Indicador Visual por Rangos
Aplicar colores al resultado:
Resultado       Color
1. ≤ 0	        Verde
2. 1 - 30	    Verde Claro
3. 31 - 60	    Amarillo
4. 61 - 90	    Naranja
5. > 90	        Rojo

## Reglas de Negocio

### RN-001 Escenario Excelente
Si CCE <= 0
Mostrar:
Excelente. La empresa recupera efectivo antes de tener que desembolsar recursos a proveedores

### RN-002 Escenario Saludable
Si CCE > 0 y <= 30
Mostrar:
El ciclo es eficiente y la recuperación del efectivo es rápida

### RN-003 Escenario Moderado
Si CCE > 30 y <= 60
Mostrar:
El ciclo es aceptable, aunque existen oportunidades de optimización

### RN-004 Escenario de Riesgo
Si CCE > 60 y <= 90
Mostrar:
Se recomienda revisar las políticas de inventario y cobranza

### RN-005 Escenario Crítico
Si CCE > 90
Mostrar -
El efectivo permanece inmovilizado durante un periodo prolongado. Existe riesgo de presión sobre la liquidez.


# Funcionalidad 2

## Visualización Gráfica Dinámica del Ciclo
Objetivo:
Representar visualmente cómo interactúan los tres componentes que conforman el Ciclo de Conversión de Efectivo

## Requerimientos Funcionales

### RF-007 Gráfico Horizontal
Mostrar gráfico de barras horizontales para:
1. Inventario  (DIO)
2. Cobro       (DSO)
3. Pago        (DPO)
4. Ciclo conversión efectivo (CCE)

### RF-008 Actualización en Tiempo Real
Cada modificación sobre los sliders deberá actualizar automáticamente la gráfica
Sin recargar la pantalla.

### RF-009 Escala Dinámica
La longitud de las barras deberá corresponder proporcionalmente al valor ingresado.

### RF-010 Colores Diferenciados
Componente  Color
1. CCE      Azul
2. DIO      Verde
3. DSO      Naranja
4. DPO      Morado

### RF-011 Etiquetas Numéricas
Cada barra deberá mostrar
1. Ciclo conversión efectivo: 26 días
2. Inventario: 54 días
3. Cobro: 38 días
4. Pago: 66 días

## Diseño Conceptual
1. CCE                          ████ 26
2. Inventario  ███████████           54
3. Cobro                  ██████████ 38
4. Pago        █████████████████     66

# Funcionalidad 3

## Línea Temporal del Ciclo de Conversión
Objetivo:
Mostrar gráficamente el recorrido del efectivo a través de la operación de la empresa

## Requerimientos Funcionales

### RF-012 Timeline Financiero
Representar:
Compra Inventario
▼
Almacenamiento
▼
Venta
▼
Cobranza
▼
Ingreso de efectivo

### RF-013 Integración Dinámica
Los días de cada tramo deberán ajustarse automáticamente según los sliders.

### RF-014 Marcador de Resultado
Mostrar visualmente dónde termina el ciclo
Ejemplo:
0 -------- 45 -------- 75 --------- 55
Compra     Venta      Cobro      CCE

# Funcionalidad 4

## Panel de Indicadores Financieros
Objetivo:
Brindar una interpretación financiera más avanzada

## Indicadores

### RF-015 Clasificación Automática
Categorizar:
1. Excelente
2. Bueno
3. Aceptable
4. Riesgoso
5. Crítico

### RF-016 Semáforo Financiero
Mostrar:
1. 🟢 Verde
2. 🟡 Amarillo
3. 🟠 Naranja
4. 🔴 Rojo
según el resultado obtenido.

### RF-017 Score Financiero
Generar una puntuación de 0 a 100
Ejemplo:
CCE         Score
1.  ≤ 0	    100
2.  30	    80
3.  60	    60
4.  90	    40
5.  >120	20

# Funcionalidad 5

## Comparación de Escenarios
Objetivo:
Permitir el análisis de estrategias de mejora.

## Requerimientos

### RF-018 Crear Escenarios
Permitir registrar:
1.	Escenario Actual
2.	Escenario Optimista
3.	Escenario Conservador
4.	Escenario Personalizado

### RF-019 Comparación Gráfica
Mostrar los CCE de cada escenario
Ejemplo:
1. Actual         ████████████ 55
2. Optimista      ██████ 25
3. Conservador    ████████████████ 75

# Funcionalidad 6

## Recomendador Financiero Inteligente
Objetivo:
Proporcionar recomendaciones accionables.

### RF-020 Análisis Automático
Evaluar cuál variable impacta más el resultado.

### RF-021 Recomendaciones
Ejemplos:
1. DIO alto:
Considere optimizar niveles de inventario y rotación de productos.
2. DSO alto:
Revise políticas de crédito y procesos de cobranza.
3. DPO bajo:
Evalúe oportunidades para negociar mayores plazos con proveedores.

# Funcionalidad 7

## Dashboard Ejecutivo
Objetivo:
Proporcionar una visión integral para directivos.

## Componentes
1. Resultado actual del CCE
2. Gráfico horizontal
3. Semáforo financiero
4. Tendencia
5. Recomendaciones
6. Comparación de escenarios

---

# Criterios de Éxito
La aplicación deberá:
1. Recalcular resultados en tiempo real.
2. Actualizar gráficos automáticamente.
3. Mostrar interpretación financiera contextual.
4. Permitir análisis de escenarios.
5. Facilitar la comprensión visual del ciclo de conversión de efectivo.

---

# MVP (Primera Versión Recomendada)
Para una primera entrega, se recomienda implementar únicamente:
1.	Simulador dinámico mediante sliders.
2.	Cálculo automático del CCE.
3.	Mensajes interpretativos automáticos.
4.	Gráfico de barras horizontales dinámico.
5.	Indicador visual tipo semáforo.

Estas funcionalidades entregan aproximadamente el 70% del valor de negocio y constituyen una base sólida para evolucionar posteriormente hacia escenarios, recomendaciones y dashboard ejecutivo.

---

## Nota final
Estas funcionalidades se desarrollarán \*\*en tres sprints\*\*, cada uno enfocado en una parte específica del proyecto.  

Al mantenerlas separadas, los estudiantes podrán comprender mejor cómo se construye progresivamente un sistema, desde los cálculos básicos hasta las visualizaciones avanzadas y el contexto financiero.  

Este enfoque permite practicar no solo la programación con Python, Streamlit y Plotly, sino también la organización profesional de un proyecto de desarrollo con Cursor AI.
