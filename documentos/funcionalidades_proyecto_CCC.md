\# Documento de Requerimientos Funcionales del Proyecto



Este documento describe las funcionalidades que desarrollaremos en el proyecto \*\*Ciclo Conversión Efectivo CCC\*\*, utilizando \*\*Cursor AI\*\* como entorno de desarrollo.  



El enfoque que seguimos es \*\*pedagógico\*\*: queremos ilustrar cómo un proyecto puede dividirse en distintas etapas (\*sprints\*), cada una con un entregable funcional. En un entorno real, muchas de estas funcionalidades podrían desarrollarse de forma iterativa o integrada, pero aquí las mantendremos separadas para fines de enseñanza.



\---



\## Aplicación de Simulación del Ciclo de Conversión de Efectivo (CCE)

\## 1. Introducción

El objetivo de la aplicación es proporcionar una herramienta interactiva y didáctica que permita a usuarios financieros, analistas, gerentes y estudiantes simular el comportamiento del Ciclo de Conversión de Efectivo (CCE) mediante la manipulación dinámica de sus variables y la visualización gráfica inmediata de los resultados.

La aplicación deberá facilitar el análisis del impacto que tienen los días de inventario, los días de cobranza y los días de pago sobre la liquidez operacional de una empresa.



\---



\## 2. Objetivos de Negocio

•	Comprender el comportamiento del Ciclo de Conversión de Efectivo.

•	Identificar oportunidades de optimización del capital de trabajo.

•	Evaluar escenarios financieros hipotéticos.

•	Facilitar procesos de capacitación financiera.

•	Permitir simulaciones en tiempo real sin requerir conocimientos avanzados de análisis financiero.



\---



\## 3. Fórmula Base

La aplicación utilizará la fórmula estándar:

CCE = DIO + DSO − DPO

Donde:

Variable	Descripción

DIO	Days Inventory Outstanding (Días de Inventario)

DSO	Days Sales Outstanding (Días de Cobro)

DPO	Days Payable Outstanding (Días de Pago)



\---



\# 4. Arquitectura Funcional

La solución estará dividida en módulos funcionales independientes para facilitar la evolución futura del producto.



\# Funcionalidad 1

Simulador Dinámico de Variables de Entrada

Objetivo

Permitir al usuario modificar los componentes del ciclo mediante controles intuitivos y observar en tiempo real el impacto sobre el resultado final.



\---



\# Requerimientos Funcionales

\# RF-001 Ingreso Dinámico de Variables

El sistema deberá permitir modificar:

•	Días de Inventario (DIO)

•	Días de Cobro (DSO)

•	Días de Pago (DPO)

mediante:

•	Slider horizontal

•	Campo numérico editable

•	Botones + y -



\---



\# RF-002 Rangos Configurables

Los sliders deberán permitir configurar:

Variable	Mínimo	Máximo

DIO	0	365

DSO	0	365

DPO	0	365



\---



\# RF-003 Sincronización

Cuando el usuario:

•	Modifique el slider

el valor numérico deberá actualizarse automáticamente.

Cuando modifique el valor numérico:

•	El slider deberá moverse automáticamente.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\# RF-004 Cálculo Automático

Cada vez que cambie una variable, el sistema deberá recalcular:

CCE = DIO + DSO - DPO

sin necesidad de presionar botones.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\# RF-005 Visualización del Resultado

Mostrar:

Ciclo de Conversión de Efectivo

45 días en una tarjeta destacada.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\# RF-006 Indicador Visual por Rangos

Aplicar colores al resultado:

Resultado	Color

≤ 0	Verde

1 - 30	Verde Claro

31 - 60	Amarillo

61 - 90	Naranja

> 90	Rojo

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\# Reglas de Negocio

\# RN-001 Escenario Excelente

Si:

CCE <= 0

Mostrar:

Excelente. La empresa recupera efectivo antes de tener que desembolsar recursos a proveedores.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\# RN-002 Escenario Saludable

Si:

CCE > 0 y <= 30

Mostrar:

El ciclo es eficiente y la recuperación del efectivo es rápida.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\# RN-003 Escenario Moderado

Si:

CCE > 30 y <= 60

Mostrar:

El ciclo es aceptable, aunque existen oportunidades de optimización.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\# RN-004 Escenario de Riesgo

Si:

CCE > 60 y <= 90

Mostrar:

Se recomienda revisar las políticas de inventario y cobranza.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\# RN-005 Escenario Crítico

Si:

CCE > 90

Mostrar:

El efectivo permanece inmovilizado durante un periodo prolongado. Existe riesgo de presión sobre la liquidez.





\# Funcionalidad 2

Visualización Gráfica Dinámica del Ciclo

Objetivo

Representar visualmente cómo interactúan los tres componentes que conforman el Ciclo de Conversión de Efectivo.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Requerimientos Funcionales

RF-007 Gráfico Horizontal

Mostrar gráfico de barras horizontales para:

Inventario (DIO)

Cobro (DSO)

Pago (DPO)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RF-008 Actualización en Tiempo Real

Cada modificación sobre los sliders deberá actualizar automáticamente la gráfica.

Sin recargar la pantalla.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RF-009 Escala Dinámica

La longitud de las barras deberá corresponder proporcionalmente al valor ingresado.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RF-010 Colores Diferenciados

Componente	Color

DIO	Azul

DSO	Verde

DPO	Naranja

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RF-011 Etiquetas Numéricas

Cada barra deberá mostrar:

Inventario: 45 días

Cobro: 30 días

Pago: 20 días

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Diseño Conceptual

Inventario  ██████████████████ 45

Cobro       ████████████       30

Pago        █████████          20

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\# Funcionalidad 3

\# Línea Temporal del Ciclo de Conversión

Objetivo

Mostrar gráficamente el recorrido del efectivo a través de la operación de la empresa.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Requerimientos Funcionales

RF-012 Timeline Financiero

Representar:

Compra Inventario

&#x20;     │

&#x20;     ▼

Almacenamiento

&#x20;     │

&#x20;     ▼

Venta

&#x20;     │

&#x20;     ▼

Cobranza

&#x20;     │

&#x20;     ▼

Ingreso de efectivo

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RF-013 Integración Dinámica

Los días de cada tramo deberán ajustarse automáticamente según los sliders.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RF-014 Marcador de Resultado

Mostrar visualmente dónde termina el ciclo.

Ejemplo:

0 -------- 45 -------- 75 --------- 55

Compra     Venta      Cobro      CCE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\# Funcionalidad 4

Panel de Indicadores Financieros

Objetivo

Brindar una interpretación financiera más avanzada.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Indicadores

RF-015 Clasificación Automática

Categorizar:

•	Excelente

•	Bueno

•	Aceptable

•	Riesgoso

•	Crítico

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RF-016 Semáforo Financiero

Mostrar:

🟢 Verde

🟡 Amarillo

🟠 Naranja

🔴 Rojo

según el resultado obtenido.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RF-017 Score Financiero

Generar una puntuación de 0 a 100.

Ejemplo:

CCE	Score

≤ 0	100

30	80

60	60

90	40

>120	20

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\# Funcionalidad 5

Comparación de Escenarios

Objetivo

Permitir el análisis de estrategias de mejora.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Requerimientos

RF-018 Crear Escenarios

Permitir registrar:

•	Escenario Actual

•	Escenario Optimista

•	Escenario Conservador

•	Escenario Personalizado

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RF-019 Comparación Gráfica

Mostrar los CCE de cada escenario.

Ejemplo:

Actual         ████████████ 55

Optimista      ██████ 25

Conservador    ████████████████ 75

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\# Funcionalidad 6

Recomendador Financiero Inteligente

Objetivo

Proporcionar recomendaciones accionables.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RF-020 Análisis Automático

Evaluar cuál variable impacta más el resultado.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RF-021 Recomendaciones

Ejemplos:

DIO alto

Considere optimizar niveles de inventario y rotación de productos.

DSO alto

Revise políticas de crédito y procesos de cobranza.

DPO bajo

Evalúe oportunidades para negociar mayores plazos con proveedores.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\# Funcionalidad 7

Dashboard Ejecutivo

Objetivo

Proporcionar una visión integral para directivos.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Componentes

•	Resultado actual del CCE

•	Gráfico horizontal

•	Semáforo financiero

•	Tendencia

•	Recomendaciones

•	Comparación de escenarios

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Criterios de Éxito

La aplicación deberá:

✅ Recalcular resultados en tiempo real.

✅ Actualizar gráficos automáticamente.

✅ Mostrar interpretación financiera contextual.

✅ Permitir análisis de escenarios.

✅ Facilitar la comprensión visual del ciclo de conversión de efectivo.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MVP (Primera Versión Recomendada)

Para una primera entrega, se recomienda implementar únicamente:

1\.	Simulador dinámico mediante sliders.

2\.	Cálculo automático del CCE.

3\.	Mensajes interpretativos automáticos.

4\.	Gráfico de barras horizontales dinámico.

5\.	Indicador visual tipo semáforo.

Estas funcionalidades entregan aproximadamente el 70% del valor de negocio y constituyen una base sólida para evolucionar posteriormente hacia escenarios, recomendaciones y dashboard ejecutivo.





\---



\## Nota final



Estas funcionalidades se desarrollarán \*\*en tres sprints\*\*, cada uno enfocado en una parte específica del proyecto.  

Al mantenerlas separadas, los estudiantes podrán comprender mejor cómo se construye progresivamente un sistema, desde los cálculos básicos hasta las visualizaciones avanzadas y el contexto financiero.  



Este enfoque permite practicar no solo la programación con \*\*Python, Streamlit y Plotly\*\*, sino también la organización profesional de un proyecto de desarrollo con \*\*Cursor AI\*\*.



