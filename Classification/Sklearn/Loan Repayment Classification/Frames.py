import pandas as pd

def load_csv_df_from(file):
    data = pd.read_csv(file)
    return data