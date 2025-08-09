import requests

def download_iris_csv(out_path):
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    response = requests.get(url)
    with open(out_path, "wb") as file:
        file.write(response.content)
    print(f"Data downloaded and saved as {out_path}")

if __name__ == "__main__":
    download_iris_csv("data/iris.csv")


