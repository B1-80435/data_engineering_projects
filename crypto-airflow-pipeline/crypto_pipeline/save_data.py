
import os

def save_to_csv(df):
    file_path = 'C:\\Users\\sunbeam\\aaa\\dags\\crypto_pipeline\\crypto_data.csv'

    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, mode='w', header=True, index=False)
