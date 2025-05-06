import pandas as pd
from pathlib import Path

def read_data():
    data_path = Path(__file__).parents[1] / "data"
    
    df = pd.read_csv(data_path / "OECD PISA data.csv")
    
    return df

if __name__ == "__main__":
    df = read_data()
    print(df.columns)