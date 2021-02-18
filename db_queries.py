import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor
import pandas.io.sql as sqlio

def handle_connection(func):
    def wrapper():
        print("HERE")
        connection = _get_connection()
        func(connection=connection, query=query)
        _close_connection()

def _get_connection():
    try:
        global postgres_pool
        postgres_pool = psycopg2.pool.SimpleConnectionPool(1, 20, user="postgres",
            password="postgres", host="127.0.0.1", port="5432", database="postgres", cursor_factory=RealDictCursor
        )

        ps_connection = postgres_pool.getconn()
        print("HERE")
        return ps_connection

    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while connecting to PostgreSQL", error)

def _close_connection():
    if postgres_pool:
        print("CLOSED")
        postgres_pool.closeall

def select(query):
    try:
        connection = _get_connection()
        if connection:
            return sqlio.read_sql_query(query, connection)
    except (Exception, psycopg2.Error) as error :
        print("Error while fetching data from PostgreSQL", error)
    finally:
        _close_connection()

def insert(query, records):
    try:
        print(query)
        print(records)
        connection = _get_connection()
        if connection:
            cursor = connection.cursor()
            result = cursor.executemany(query, records)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into mobile table")
            return result
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into table {}".format(error))
    finally:
        _close_connection()

@handle_connection
def select_2(*args, **kwargs):
    print("SD")
    print(kwargs)
    # try:
    #     cursor = connection.cursor()
    #     cursor.execute(query)
    #     return cursor.fetchall()
    # except (Exception, psycopg2.Error) as error :
    #     print ("Error while fetching data from PostgreSQL", error)
