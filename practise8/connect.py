import psycopg2
from config import load_config

def get_connection():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = load_config()
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Connection error: {error}")
        return None