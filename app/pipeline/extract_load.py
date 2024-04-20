import os
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import numpy as np
import glob


def extract_file_from_bigquery(input_dir):
    """
    This function extracts a table from Google BigQuery and saves it into a dataframe.

    Args:
        input_dir (str): Directory path where the CSV file will be saved.
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

    try:
        # Query to extract the table
        selectQuery = """SELECT * FROM etl-project-416319.project_1.retail_df"""
        bigqueryClient = bigquery.Client()
        df = bigqueryClient.query(selectQuery).to_dataframe()

        csv_file_path = os.path.join(input_dir, "ecommerce.csv")

        # Check if file already exists
        if os.path.isfile(csv_file_path):
            overwrite = input("CSV file already exists. Do you want to overwrite it? (yes/no): ")
            if overwrite.lower() != 'yes':
                print("Operation aborted.")
                return
        if not os.path.exists(input_dir):
            os.makedirs(input_dir)
        
        df.to_csv(csv_file_path, index=False)
        print(f"CSV file saved successfully at: {csv_file_path}")

    except Exception as e:
        print("An error occurred:", e)
        
if __name__=='__main__':
    path = 'data/input'
    
    extract_file_from_bigquery(path)