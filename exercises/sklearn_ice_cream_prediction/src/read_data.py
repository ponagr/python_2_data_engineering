import pandas as pd
from pathlib import Path

file_path = Path(__file__).parents[1] / "data"

def read_data():
    df = pd.read_csv(file_path / "IceCreamData.csv")
    
    return df

if __name__ == "__main__":
    df = read_data()
    print(df)