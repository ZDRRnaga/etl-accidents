from etl.extract import extract_csv
from etl.transform import transform_data
from etl.load import load_to_database
from loguru import logger

data_path = "data/raw/train.csv"
table_name = "accidents"

def run_etl():
    logger.info("Iniciando pipeline ETL")

    df = extract_csv(data_path)
    df = transform_data(df)
    load_to_database(df, table_name)

    logger.info("Pipeline ETL finalizado con exito")

if __name__ == "__main__":
    run_etl()
