import pandas as pd
from getpass import getpass
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import psycopg
from sqlalchemy.orm import Session
from sqlalchemy import text

# connection sqlalchemy:

# pw = getpass('Please enter password: ')
connection_url = f'postgresql://postgres:Datacraft@localhost:5432/hoteldb'
engine = create_engine(connection_url)

# check connection:
with engine.connect() as conn_alchemy:
    print("SQLAlchemy connected!")


# connection psycopg:
# pw = getpass('Please enter password: ')
with psycopg.connect(
    host='localhost',
    port='5432',
    user='postgres',
    password='Datacraft',
    dbname='hoteldb',
    autocommit=True
) as connection:
    print("psycopg connected!")
