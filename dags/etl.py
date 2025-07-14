from airflow import DAG 
from airflow.providers.http.operators.http import SimpleHttpOperator

from airflow.decorators import task 
from airflow.providers.postgres.hooks.postgres import PostgresHook   # we need to insert  the data inside postgre  
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
    def create_table():
        ## intialize the postgres hook (we use it to intract with postregresql) 
        postgres_hook=PostgresHook(postgres_conn_id='my_postgres_connection')  # postgres_default is the connection id we created in airflow UI
        
        
        ## sql query to create table 
        create_table_query= """ CREATE TABLE IF NOT EXISTS apod_data(
            id serial Primary Key, 
            title Varchar(255) 
            explanation Text , 
            url Text , 
            date Date , 
            media_Type Varchar(50) 
            ) ; 
            
            """
            
        ## exceute the table creation query 
        postgres_hook.run(create_table_query)
    
    
    
    
    # step 2 : extract the nasa api data (APOD data )- Astronomy picture of the day data [extract pipeline]
    # eOnJsgUmtzZXh2QygWeKA5T5DDsGVmcdmbugcbqT
    # https://api.nasa.gov/planetary/apod?api_key=eOnJsgUmtzZXh2QygWeKA5T5DDsGVmcdmbugcbqT
    # 
    # : 
    
    
    extract_apod = SimpleHttpOperator(
        task_id ='extract_apod', 
        http_conn_id = 'nasa_api' ,                                                      # connection id we created in airflow UI for nasa api
        endpoint='planetary/apod',                                                        # nasa api endpoint for astronomy picture of the day
        method='GET',
        data={'api_key': '{{conn.nasa_api.extra_dejson.api_key}}'},                      # Use the API key from the connection
        response_filter = lambda response: response.json(),                             # convert the JSON response
    )
    
    
    
    #step 3 : transform the data (pick the info i need to save) 
    
    @task 
    def transform_apod_data(response): 
        apod_data = {
            'title':response.get('title',''), 
            'explanation':response.get('explanation',''),
            'url':response.get('url',''),
            'date':response.get('date',''),
            'media_type':response.get('media_type','') 
        } 
        
        return apod_data 
    
    
    
    #step 4 : we loading the data into postgere  
    
    @task 
    def load_data_to_postgres(apod_data):
        # initilize the postgres hook 
        postgres_hook = PostgresHook(postgres_conn_id='my_postgres_connection') 
        
        
        ## define the sql insert query  
        
        insert_query = """ 
        Insert into apod_data (title, explanation, url, date, media_type) 
        Values (%s, %s, %s, %s, %s)
        """
    
 
    # excute the sql query  
        postgres_hook.run(insert_query, parameters=(
           apod_data['title'],
           apod_data['explanation'],
           apod_data['url'],
           apod_data['date'],
           apod_data['media_type']
       
        )) 
            
    
    # step 5 : to check the our task is working fine we check it to with DBviewver 
    # DBviewver : it is the tool which help us to conn to any kind of DB 
    
    
    
    
    
    
    # step 6 : Define the dependencies 
    #extract
    create_table() >> extract_apod   # ensure te table is created before extraction 
    api_response = extract_apod.output  # get the output of the extract_apod task 
    # transform
    transformed_data =transform_apod_data(api_response) 
    #load 
    load_data_to_postgres(transformed_data)  # load the transformed data into postgres


