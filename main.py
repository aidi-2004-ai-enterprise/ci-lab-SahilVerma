import pandas as pd
import seaborn as sns

def load_penguin_data():
    """Load penguin dataset and return DataFrame shape"""
    # Enter your code here
    df = sns.load_dataset("penguins")
    return df.shape

if __name__ == "__main__":
    shape = load_penguin_data()
    print("Hello from ci-lab-sahilverma!")
    print(f"Penguin dataset shape: {shape}")