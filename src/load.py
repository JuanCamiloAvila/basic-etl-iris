import pandas as pd
import psycopg2

def load_to_postgres(csv_path, db_params):
    df = pd.read_csv(csv_path)
    print("Rows to insert:", len(df))
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    for i, row in df.iterrows():
        try:
            cur.execute(
                "INSERT INTO iris (sepal_length, sepal_width, petal_length, petal_width, species) VALUES (%s, %s, %s, %s, %s)",
                (row['sepal_length'], row['sepal_width'], row['petal_length'], row['petal_width'], row['species'])
            )
        except Exception as e:
            print(f"Failed on row {i}: {e}")
    conn.commit()
    cur.close()
    conn.close()
    print("Data loaded into PostgreSQL")
