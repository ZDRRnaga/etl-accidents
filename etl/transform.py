import pandas as pd
from loguru import logger

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Iniciando transformacion de datos")

    # Normalizar nombres de columnas
    df.columns = df.columns.str.lower().str.strip()

    # Validaciones
    assert (df["speed_limit"] > 0).all(), "Speed limit invalido"
    assert (df["num_lanes"] > 0).all(), "Numero de carriles invalido"
    assert df["accident_risk"].between(0, 1).all(), "Riesgo de accidente fuera de rango"

    logger.info("Transformacion completada")
    return df