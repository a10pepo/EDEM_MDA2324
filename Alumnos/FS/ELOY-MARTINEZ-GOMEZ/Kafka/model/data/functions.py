import requests
import datetime
import time
import mysql.connector
from mysql.connector import Error

def db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='myuser',
            password='mypassword',
            database='mydatabase'
        )
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None
def db_connection_docker():
    start_time = time.time()  # Guardar el tiempo de inicio
    while True:
        try:
            connection = mysql.connector.connect(
                host='db',
                user='myuser',
                password='mypassword',
                database='mydatabase'
            )
            print("Database connection successful.")
            return connection
        except Error as e:
            elapsed_time = time.time() - start_time
            print(f"Error connecting to the database: {e}. Retrying...")

            if elapsed_time >= 60:
                print("Connection attempt timed out after 60 seconds.")
                return None

            time.sleep(5)

def execute_query(db, query):
    results = None  # Inicializa 'results' para evitar UnboundLocalError
    if db == "docker":
        conn = db_connection_docker()
    else:
        conn = db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()  # Recuperar todos los resultados
        conn.commit()
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()
        conn.close()

    return results

def convert_to_sql_values(value):
    value = str(value)
    value = value.replace("[", "")
    value = value.replace("]", "")
    value = value +";"
    return value

def get_candle_prices(date):
    date_str = date.strftime("%Y-%m-%d")
    # Define the API endpoint URL
    url = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/minute/" + date_str + "/" + date_str + "?apiKey=IhAj4BvqTLLrHmNZgfMYbqS0yhkLpMKm"

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    sql_last_id = "SELECT id FROM candle_prices ORDER BY id DESC LIMIT 1;"
    last_id = execute_query('prueba', sql_last_id)
    last_id = last_id[0][0] if last_id else 0
    print(last_id)
    
    if response.status_code == 200:
        data = response.json()
        candle_prices = []
        counter = last_id
        for item in data["results"]:
            counter += 1
            values = [counter]
            for value in item:
                if value == "t":
                    price = item[value]
                    price = datetime.datetime.fromtimestamp(price / 1000)
                    price = price.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    price = item[value]
                values.append(price)
            values = tuple(values)
            candle_prices.append(values)
    else:
        # Handle the error
        print("Error:", response.status_code)

    candle_prices_str = convert_to_sql_values(candle_prices)
    return candle_prices_str
