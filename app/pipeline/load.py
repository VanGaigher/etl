import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import os
import pandera as pa


def load_settings_postgres():
    """ Loading the settings from environment variables"""
    dotenv_path = Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)
    
    settings = {
        "db_host": os.getenv("POSTGRES_HOST"),
        "db_user": os.getenv("POSTGRES_USER"),
        "db_pass": os.getenv("POSTGRES_PASSWORD"),
        "db_name": os.getenv("POSTGRES_DB"),
        "db_port": os.getenv("POSTGRES_PORT"),    
    }
    return settings


def load_dataframe_postgres(data_frame: pd.DataFrame, table_name: str):

    settings = load_settings_postgres()
    
    # creating a connection string based settings
    connection_string = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}?client_encoding=utf8"
    
    # creating engine to connection
    engine = create_engine(connection_string)
    
    with engine.connect() as conn, conn.begin():
        
        data_frame.to_sql(table_name, engine, if_exists='replace', index=False)
      
    return print(" Loading done successfully!")

