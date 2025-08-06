# 🚀  APOD Data Pipeline with Airflow & PostgreSQL

This project builds a fully automated ETL pipeline to ingest data from the **NASA Astronomy Picture of the Day (APOD)** API using **Apache Airflow**, store it into **PostgreSQL**, and schedule it using **Astro CLI**.

---

## 🧠 Objective

The goal is to extract daily astronomy data from NASA's APOD API, transform the response, and load it into a PostgreSQL database for persistent storage and further analytics.

---

## 📦 Tech Stack

| Tool           | Purpose                            |
|----------------|-------------------------------------|
| Apache Airflow | Workflow orchestration (ETL)        |
| Astro CLI      | Airflow deployment & management     |
| PostgreSQL     | Persistent database storage         |
| Docker         | Containerized local environment     |
| Python         | Data transformation & scripting     |
| NASA API       | Astronomy Picture of the Day        |

---

## 📂 Project Structure

```bash
ml_ops_proj/
├── dags/
│   └── etl.py              # Airflow DAG for ETL
├── include/
│   └── requirements.txt    # Python dependencies
├── Dockerfile              # Custom image (optional)
├── .env                    # Astro environment config
├── airflow.settings.yaml   # Connection setup
├── README.md               # Project documentation

└── ...





## Improvements

- Add Evidently or Great Expectations for data validation
- Extend support to store images in AWS S3 or GCS
- Visualize APOD entries using a dashboard (e.g., Streamlit or Dash)
- Schedule email alerts with APOD image of the day
