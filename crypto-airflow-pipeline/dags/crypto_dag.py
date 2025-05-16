from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from crypto_pipeline.fetch_crypto_data import get_crypto_prices
from crypto_pipeline.save_data import save_to_csv
import psycopg2
import matplotlib.pyplot as plt 


def save_to_database(df):
    conn = psycopg2.connect(
        host='localhost',
        database='crypto_db',
        user='airflow',
        password='airflow'
    )
    cursor = conn.cursor()

    for i, row in df.iterrows():
        cursor.execute("""
        INSERT INTO crypto_price (name, price_usd, date)
        VALUES (%s, %s, %s)
        """, (row['name'], row['price_usd'], row['date']))


    conn.commit()
    

    cursor.close()
    conn.close()

    print("Data inserted into Postgres")


default_args = {
    'owner': 'tanzeel',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': True,
    'email': ['tanzeelprof1705@gmail.com']
}


def check_data_quality(df):
    if df.isnull().sum().any():
        raise ValueError("Data contains missing values")

    if (df['price_usd'] <= 0).any():
        raise ValueError("Data contains non-positive values")    

    print("Data quality checks passed.")


def plot_data(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['price_usd'], label='Bitcoin Price', color='blue')
    plt.title('Bitcoin Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price in USD')
    plt.legend()
    # plt.savefig('/opt/airflow/plots/bitcoin_price_plot.png')


def fetch_and_save():
    df = get_crypto_prices()


    check_data_quality(df)


    save_to_csv(df)


    save_to_database(df)


    plot_data(df)



with DAG(
    dag_id='crypto_price_pipeline',
    default_args=default_args,
    start_date=datetime(2025, 5, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['crypto', 'beginner']
) as dag:


    run_task = PythonOperator(
        task_id='fetch_and_store_crypto_data',
        python_callable=fetch_and_save
    )

    run_task
