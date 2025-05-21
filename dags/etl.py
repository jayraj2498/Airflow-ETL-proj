from airflow import DAG 
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task 
from airflow.providers.postgres.hooks.postgres import PostgresHook 
from airflow.utils.dates import days_ago 
import json 


# Define the DAG

with DAG(
    dag_id='nasa_data_apod_postgres',
    start_date=days_ago(1),
    schedule_interval='@daily',
    catchup=False,
) as dag :
    
    
    
    #step 1 : to crete table if it is not exist 
    @task 
    
    
    
    
    
    # step 2 : extract the nasa api data (APOD data )- Astronomy picture of the day data [extract pipeline]
    
    
    
    
    #step 3 : transform the data (pick the info i need to save) 
    
    
    
    #step 4 : we loading the data into postgere 
    
    
    
    # step 5 : to check the our task is working fine we check it to with DBviewver 
    # DBviewver : it is the tool which help us to conn to any kind of DB 
    
    
    
    # step 6 : Define the dependencies 




