import os
import pandas as pd
from google.cloud import bigquery
import glob
import pandera as pa

def load_settings_big_query():
    """
    This function loads the settings from environment variables.
    """
    # Finding the path to gbq.json file
    json_file_paths = glob.glob(os.path.join(os.getcwd(), "gbq.json"))

    if json_file_paths:
        json_file_path = json_file_paths[0]
        # Setting the JSON file in environment
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file_path
    else:
        print("No gbq.json file found in the current directory.")
        return

def extract_data_from_bigquery(query: str) -> pd.DataFrame:
    """
    This function executes a query in Google BigQuery and returns the result as a DataFrame.

    Args:
        query (str): Query to select the data from BigQuery table.

    Returns:
        pd.DataFrame: DataFrame containing the result of the query.
    """
    # Load settings from environment variables
    load_settings_big_query()

    try:
        # Create BigQuery client
        bigquery_client = bigquery.Client()

        # Execute query and convert result to DataFrame
        result_df = bigquery_client.query(query).to_dataframe()

        return result_df

    except Exception as e:
        print("An error occurred:", e)
        return pd.DataFrame()  # Return an empty DataFrame if an error occurs

if __name__ == '__main__':
       
    # Execute a query to extract data from BigQuery
    query = """SELECT * FROM etl-project-416319.project_1.retail_df"""
    df = extract_data_from_bigquery(query)
    schema_df = pa.infer_schema(df)
    
    with open("schema_df.py","w", encoding ="utf-8") as arquivo:
        arquivo.write(schema_df.to_script())
    
    print(df)
    
    
