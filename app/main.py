from pipeline.extract import extract_data_from_bigquery

query = """SELECT * FROM etl-project-416319.project_1.retail_df"""

df = extract_data_from_bigquery(query)
print(df)