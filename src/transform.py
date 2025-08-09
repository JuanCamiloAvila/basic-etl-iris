import pandas as pd

def transform_iris(input_path, output_path):
    df = pd.read_csv(input_path)
    df['species'] = df['species'].str.upper()  # Make all species uppercase
    df.to_csv(output_path, index=False)
    print(f"Transformed data saved as {output_path}")
    print(df['species'].head())

if __name__ == "__main__":
    transform_iris("data/iris.csv", "data/iris_transformed.csv")