import pandas as pd
from loguru import logger

def extract_csv(path: str) -> pd.DataFrame:
    logger.info(f"Extrayendo datos desde {path}")
    df = pd.read_csv(path)
    logger.info(f"Filas extraidas: {len(df)}")
    return df