# Análisis de Incidentes por Tipo de Arma y Municipio

Este proyecto es una aplicación web interactiva creada en **Python** utilizando **Streamlit** para analizar un DataFrame que contiene información sobre incidentes registrados en diferentes municipios, tipos de arma, y otros factores relevantes. La aplicación permite a los usuarios aplicar filtros y visualizar gráficos dinámicos para analizar los datos según sus necesidades.

## Características

- **Filtros interactivos**: Los usuarios pueden aplicar filtros por rango de fechas, tipo de arma y municipio.
- **Visualización de datos**: Se generan gráficos dinámicos que muestran la evolución y distribución de los incidentes según los filtros aplicados.
  - Gráfico de barras que muestra el número de incidentes por tipo de arma.
  - Gráfico de líneas que muestra la evolución de los incidentes a lo largo del tiempo.
  - Gráfico de pastel que muestra la distribución de incidentes por municipio.
- **Interfaz fácil de usar**: La aplicación permite una navegación sencilla para ajustar y aplicar filtros con un sidebar interactivo.

## Estructura del DataFrame

La aplicación analiza los datos de un archivo CSV que debe tener la siguiente estructura:

| Columna         | Descripción                                      |
|-----------------|--------------------------------------------------|
| `DEPARTAMENTO`  | Nombre del departamento                          |
| `MUNICIPIO`     | Nombre del municipio                             |
| `CODIGO DANE`   | Código DANE del municipio                        |
| `ARMA MEDIO`    | Tipo de arma utilizada                           |
| `FECHA HECHO`   | Fecha en que ocurrió el incidente (YYYY-MM-DD)   |
| `GENERO`        | Género de la persona involucrada                 |
| `AGRUPA EDAD`   | Grupo de edad de la persona involucrada          |
| `CANTIDAD`      | Número de incidentes                             |

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener las siguientes dependencias instaladas:

- **Python 3.x**
- **Streamlit** para la interfaz gráfica interactiva.
- **Pandas** para la manipulación de datos.
- **Matplotlib** o **Plotly** para la creación de gráficos.

Puedes instalarlas ejecutando el siguiente comando:

```bash
pip install streamlit pandas matplotlib
```

## Ejecución de la Aplicación

Para ejecutar la aplicación en tu máquina local:

1. Clona este repositorio o descarga el archivo `app.py`.
2. Asegúrate de que los datos que deseas analizar estén en un archivo CSV llamado `data.csv` y que tengan el formato correcto (mencionado anteriormente).
3. En la terminal, navega hasta el directorio donde se encuentra el archivo `app.py` y ejecuta el siguiente comando:

```bash
streamlit run app.py
```

4. La aplicación se abrirá en tu navegador web predeterminado. Allí podrás interactuar con los filtros y explorar los gráficos generados.

## Uso de la Aplicación

1. **Seleccionar el rango de fechas**: Utiliza el deslizador en la barra lateral para elegir el rango de años entre 2017 y 2024.
2. **Seleccionar el tipo de arma**: Escoge uno o varios tipos de armas en la lista de selección.
3. **Seleccionar el municipio**: Filtra los incidentes por uno o varios municipios en la lista.
4. **Ver resultados**: Los gráficos en la vista principal se actualizarán automáticamente en función de los filtros seleccionados. También se mostrará una tabla con los datos filtrados.

## Gráficos Incluidos

- **Gráfico de barras**: Muestra la cantidad total de incidentes por tipo de arma seleccionada.
- **Gráfico de líneas**: Visualiza la evolución de los incidentes a lo largo del tiempo según el rango de fechas seleccionado.
- **Gráfico de pastel**: Muestra la distribución de incidentes entre los diferentes municipios seleccionados.

## Personalización

Si deseas modificar o agregar más gráficos o filtros, puedes editar el archivo `app.py`. Por ejemplo, para agregar un filtro por género o grupo de edad, puedes modificar la sección de filtros en el sidebar.

## Contribución

Si deseas contribuir al proyecto, siéntete libre de hacer un fork del repositorio y enviar tus pull requests. Cualquier mejora en la funcionalidad, rendimiento o diseño de la interfaz será bienvenida.
