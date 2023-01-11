import psycopg2
from psycopg2.extras import execute_values

def export_to_db(config_data):
    
    """
    Exports configuration into DB
    """
    
    conn = psycopg2.connect(
        host = '',
        dbname = '',
        user = '',
        password = '',
        port = ''
    )

    cur = conn.cursor()
    
    create_table = """ CREATE TABLE config (
                id serial PRIMARY KEY,
                id_1 INT,
                connection INT,
                name VARCHAR(255) NOT NULL,
                description VARCHAR(255),
                config json,
                type VARCHAR(50),
                infra_type VARCHAR(50),
                port_channel_id INTEGER,
                max_frame_size INTEGER) """ 



    cur.execute(create_table)

    # Get all keys from Dictionary
    columns = config_data[0].keys()

    # Use the keys as column headers
    query = "INSERT INTO config ({}) VALUES %s".format(','.join(columns))

    # Extract dict values into list of lists
    values = [[value for value in config.values()] for config in config_data]

    # Execute queries
    execute_values(cur, query, values)
    conn.commit()


    cur.close()
    conn.close()