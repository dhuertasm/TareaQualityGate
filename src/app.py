import sqlite3
import os

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
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def process_files(directory):
    files = os.listdir(directory)
    for i in range(len(files)):
        file = files[i]
        f = open(os.path.join(directory, file))
        print(f.read())
        f.close()

def files_process(directory):
    files = os.listdir(directory)
    for i in range(len(files)):
        file = files[i]
        f = open(os.path.join(directory, file))
        print(f.read())
        f.close()