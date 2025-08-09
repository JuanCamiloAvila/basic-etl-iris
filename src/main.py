import pandas as pd
from extract import download_iris_csv
from transform import transform_iris
from load import load_to_postgres, db_params

def main():
    input_raw = "data/iris.csv"
    input_final = "data/iris_transformed.csv"
    download_iris_csv(input_raw)
    transform_iris(input_raw, input_final)
    load_to_postgres(input_final, db_params)
if __name__ == "__main__":
    main()
