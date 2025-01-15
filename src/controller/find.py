import pandas as pd
from getpass import getpass
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import psycopg
from sqlalchemy.orm import Session
from sqlalchemy import text
import psycopg

from src.controller.connector import open_connection


def find_by_id(item):
    connection_url = f'postgresql://postgres:Datacraft@localhost:5432/hoteldb'
    engine = create_engine(connection_url)

    # check connection:
    with engine.connect() as conn_alchemy:
        print("SQLAlchemy connected!")


    try:
        sel_stmt = f'SELECT * FROM meta WHERE "id" = {item};'
        complete_df = pd.read_sql(sel_stmt, engine)
        print(complete_df)
    except Exception as error:
        print(f'{error}')

find_by_id(1)
