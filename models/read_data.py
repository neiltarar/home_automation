import psycopg2

def insert_weather_data(sql, params):
    # Connect to postgresql database
    conn = psycopg2.connect("dbname= home_automation user=pi")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a query
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()