import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
        """
        Description: This function is used to drop existing tables.
        Arguments:
            cur: The cursor object to execute the query. 
            conn: Connection to the database. 
        Returns:
            None 
        """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
        """
        Description: This function is used to create tables.
        Arguments:
            cur: The cursor object to execute the query. 
            conn: Connection to the database. 
        Returns:
            None 
        """    
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
        """
        Description: This function utilises the configuration file and executes drop and create table functions.
        Arguments:
            None
        Returns:
            None 
        """        
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()