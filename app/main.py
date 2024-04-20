from pipeline.extract import extract_data_from_bigquery
from pipeline.load import load_dataframe_postgres

query = """SELECT * FROM etl-project-416319.project_1.retail_df"""

df = extract_data_from_bigquery(query)
table_name = "ecommerce_original"

load_dataframe_postgres(df, table_name=table_name)