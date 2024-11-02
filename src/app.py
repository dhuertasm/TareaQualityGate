import sqlite3

def suma(x,y):
    return x + y

def valor_retornado():
    flag = True
    if flag:
        return "Hola mundo!"
    else:
        return "Adios mundo!"

def retorar_valor():
    flag = True
    if flag:
        return "Hola mundo!"
    else:
        return "Adios mundo!"

def execute_query(user_input):
    # Esta consulta es vulnerable a SQL Injection
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results