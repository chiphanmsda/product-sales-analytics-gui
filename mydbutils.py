from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser

def read_config(config_file = 'pinnacle_wh.ini', section = 'mysql'):
    parser = ConfigParser()
    parser.read(config_file)
    
    config = {}
    
    if parser.has_section(section):
        # Parse the configuration file.
        items = parser.items(section)
        
        # Construct the parameter dictionary.
        for item in items:
            config[item[0]] = item[1]
            
    else:
        raise Exception(f'Section [{section}] missing ' + \
                        f'in config file {config_file}')
    
    return config
        
def make_connection(config_file = 'pinnacle_wh.ini', section = 'mysql'):
    try:
        db_config = read_config(config_file, section)
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            return conn

    except Error as e:
        print('Connection failed.')
        print(e)
        
        return None

def do_query_multi(sql):
    cursor = None
    
    # Connect to the database.
    conn = make_connection()
        
    if conn != None:
        try:
            cursor = conn.cursor()
            results = cursor.execute(sql, multi=True)
            
        except Error as e:
            print('Query failed')
            print(e)
            
            return [(), 0]

    # Return the fetched data as a list of tuples,
    # one tuple per table row.
    if conn != None:
        for result in cursor.execute(sql, multi=True):
            print(result)
        rows = cursor.fetchall()
        count = cursor.rowcount
            
        conn.close()
        return [rows, count]
    else:
        return [(), 0]
    
def do_query(sql):
    cursor = None
    
    # Connect to the database.
    conn = make_connection()
        
    if conn != None:
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            
        except Error as e:
            print('Query failed')
            print(e)
            
            return [(), 0]

    # Return the fetched data as a list of tuples,
    # one tuple per table row.
    if conn != None:
        rows = cursor.fetchall()
        count = cursor.rowcount
            
        conn.close()
        return [rows, count]
    else:
        return [(), 0]

# def do_query_return_all(sql):
#     cursor = None
    
#     conn = make_connection()

#     try:
#         cursor = conn.cursor()
#         cursor.execute(sql)

#         # Return the all fetched data as a list of tuples,
#         # one tuple per table row.
#         rows = cursor.fetchall()
#         count = cursor.rowcount
        
#         cursor.close()
#         return [rows, count]

#     except Error as e:
#         print('Query failed')
#         print(e)

#         cursor.close()
#         return [(), 0]
