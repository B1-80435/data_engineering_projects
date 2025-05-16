# 🪂 Crypto Price Data Pipeline using Apache Airflow

An end-to-end data engineering project that automates the extraction, validation, storage, and scheduling of real-time cryptocurrency prices using **Apache Airflow**, **Python**, **Docker**, and **PostgreSQL**.

---

## 🚀 Project Overview

This project builds a **daily ETL pipeline** using Apache Airflow to:

- Fetch real-time crypto prices (Bitcoin & Ethereum) via the [CoinGecko API](https://www.coingecko.com/en/api)
- Perform data quality checks
- Store data in:
  - A local **CSV file**
  - A **PostgreSQL** database
- (Optional) Plot crypto trends using `matplotlib`
- Schedule all tasks via an Airflow **DAG**, with retries and failure email alerts

---

## 📂 Folder Structure

```

crypto-airflow-pipeline/
│
├── dags/
│   └── crypto\_dag.py             ← Airflow DAG definition
│
├── crypto\_pipeline/
│   ├── fetch\_crypto\_data.py      ← API call and data fetching
│   ├── save\_data.py              ← Save to CSV & PostgreSQL
│
├── requirements.txt              ← Project dependencies
├── README.md                     ← Project documentation
└── .gitignore                    ← Python & Airflow ignores

````

---

## 🔧 Technologies Used

| Tool             | Purpose                          |
|------------------|----------------------------------|
| **Python**       | Data fetching, validation, I/O   |
| **Apache Airflow** | Workflow orchestration         |
| **Docker**       | Containerized Airflow environment |
| **PostgreSQL**   | Structured data storage          |
| **CoinGecko API**| Real-time crypto price source    |
| **Pandas**       | Data manipulation                |
| **Matplotlib**   | Optional visualizations          |

---

## 🔁 Workflow / DAG Description

```text
fetch_and_store_crypto_data
    |
    ├── get_crypto_prices()       → fetch BTC/ETH prices from CoinGecko
    ├── check_data_quality()      → null and negative value validation
    ├── save_to_csv()             → backup snapshot locally
    └── save_to_postgres()        → insert data into PostgreSQL
````

Each task has:

* Retries
* Email alerts on failure
* Scheduled execution (@daily)

---

## 📊 Sample Output (in PostgreSQL)

| name     | price\_usd | date                       |
| -------- | ---------- | -------------------------- |
| bitcoin  | 99586.00   | 2025-05-08 15:21:13.951527 |
| ethereum | 1934.93    | 2025-05-08 15:21:13.951527 |

---

## 🧪 How to Run the Project (Local Setup)

> Docker is required (Airflow runs in containers)

```bash
# Clone the repo
git clone https://github.com/<your-username>/crypto-airflow-pipeline.git
cd crypto-airflow-pipeline

# Run Docker containers
docker-compose up -d

# Access Airflow UI
http://localhost:8080
```

* Default Airflow login: `admin` / `admin`
* Trigger the DAG `crypto_price_pipeline` manually or wait for scheduled run

---

## 📬 Future Improvements

* Add Streamlit dashboard to visualize crypto trends
* Extend DAG to track more coins
* Integrate with Kafka for real-time streaming (advanced)

---

## 🙌 Credits

Built with love by **Tanzeel Mansuri**
[LinkedIn](https://linkedin.com/in/tanzeel-mansuri) • [GitHub](https://github.com/B1-80435/data_engineering_projects)

---

## 🏷️ Tags

`#DataEngineering` `#ApacheAirflow` `#Python` `#Docker` `#PostgreSQL` `#CryptoPipeline` `#ETL`

```

