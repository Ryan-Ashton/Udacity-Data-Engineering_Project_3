import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
        """
        Description: This function utilises SQL queries which copies tables for the staging phase.
        Arguments:
            cur: The cursor object to execute the query. 
            conn: Connection to the database. 
        Returns:
            None 
        """    
    
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
        """
        Description: This function transforms tables utilising insert queries.
        Arguments:
            cur: The cursor object to execute the query. 
            conn: Connection to the database. 
        Returns:
            None 
        """        
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
        """
        Description: This function executes the staging and inserting of tables into Redshift utilising the configuration file.
        Arguments:
            None
        Returns:
            None 
        """        
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()