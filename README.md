<<<<<<< HEAD
This project was generated using the command `astro dev init` via the Astronomer CLI.  
Below is a summary of the project structure and instructions to run Apache Airflow locally.

---

## 📂 Project Contents

- **`dags/`**: Contains your Airflow DAGs.
  - `example_astronauts.py`: A sample ETL pipeline that:
    - Fetches data from the Open Notify API (astronauts in space).
    - Uses **TaskFlow API**.
    - Demonstrates **dynamic task mapping**.

- **`Dockerfile`**: Defines the Astro Runtime Docker image.  
  You can add commands here to customize runtime behavior.

- **`include/`**: For any extra project files (default: empty).

- **`packages.txt`**: Add any OS-level dependencies here (default: empty).

- **`requirements.txt`**: List your required Python packages here (default: empty).

- **`plugins/`**: For custom or community plugins (default: empty).

- **`airflow_settings.yaml`**:  
  Add local Airflow Connections, Variables, and Pools here instead of entering them manually in the UI.

---

## 🛠️ Run Airflow Locally

1. Start Airflow with:
   ```bash
   astro dev start 














This will create 4 Docker containers:

postgres: Airflow metadata database

webserver: Airflow UI

scheduler: Monitors and runs tasks

triggerer: Triggers deferred tasks

To check if containers are running: 
=======
# Airflow-ETL-proj
>>>>>>> fa61f3070e75f179420cc1895106fcba623da596
