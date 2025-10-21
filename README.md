# **Pipeline de Datos: Limpieza, Integración y Visualización de Ventas**

### **Descripción**

Este proyecto implementa un flujo completo de análisis de datos utilizando Python, PostgreSQL y Power BI.
El objetivo principal es crear un sistema que permita limpiar, integrar y visualizar información de clientes, productos y ventas para obtener una visión analítica del negocio.

### **Objetivos del Proyecto**

Construir un pipeline de datos desde archivos crudos hasta una base de datos relacional (PostgreSQL).

Realizar limpieza y transformación de los datos con Python (pandas).

Integrar las tablas clientes, productos y ventas en Power BI.

Crear relaciones y dashboards interactivos para el análisis de comportamiento de clientes y ventas.

Documentar el flujo de trabajo para mostrar habilidades en análisis, automatización y visualización de datos.

### **Tecnologías Utilizadas**

-> Python (pandas, psycopg2)

-> PostgreSQL

-> Power BI

-> Excel/CSV

-> GitHub

# Diagrama de flujo del Pipeline

```mermaid
flowchart TD
    A["Fuentes de Datos (Excel, CSV, Ventas brutas)"] --> B["Limpieza y Transformación con Python (Pandas)"]
    B --> C["Carga en Base de Datos PostgreSQL"]
    C --> D["Visualización y Análisis en Power BI"]
    D --> E["Reportes e Insights para la toma de decisiones"]

    subgraph Pipeline_de_Ventas
        A --> B --> C --> D --> E
    end

