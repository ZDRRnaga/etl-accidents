# ETL Pipeline – Accidentes de Tránsito (CSV → PostgreSQL)

## Descripción
Pipeline ETL desarrollado en **Python** que procesa un dataset de accidentes de tránsito obtenido de Kaggle.  
El proceso extrae datos desde un archivo CSV, aplica validaciones y transformaciones de calidad de datos, y los carga en una base de datos **PostgreSQL** para su análisis.

Este proyecto tiene como objetivo demostrar habilidades prácticas en **ingeniería de datos**, diseño de pipelines ETL y manejo de bases de datos relacionales.

---

## Tecnologías
- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- psycopg2
- Loguru
- python-dotenv

---

## Flujo ETL
1. **Extract**: Lectura del CSV con Pandas.  
2. **Transform**: Normalización de columnas y validaciones de calidad de datos.  
3. **Load**: Carga eficiente de más de 500,000 registros en PostgreSQL.

---
## Ejecución

- pip install -r requirements.txt
- python main.py

---

## Resultados

- Pipeline ETL reproducible y escalable.
- Carga exitosa de ~517k registros en PostgreSQL.
- Base de datos lista para análisis SQL.

---

## Autor

Zuriel Damian Reynaga Rojas
