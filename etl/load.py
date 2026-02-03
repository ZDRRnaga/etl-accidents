import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

def load_to_database(df, table_name: str):
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    )

    logger.info("Conectando a PostgreSQL")

    with engine.begin() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {table_name}"))

        df.to_sql(
            table_name,
            con=conn,
            if_exists="replace",
            index=False,
            method="multi",
            chunksize=10_000
        )

    logger.info(f"Datos cargados correctamente en tabla '{table_name}'")
