import csv
import sqlite3

'''
create table and put in all the columns neeeded. 

'''
def create_table():
    conn = sqlite3.connect("housing.db")
    c = conn.cursor()
    
    c.execute (""" CREATE TABLE IF NOT EXISTS housing_data (
        price INTEGER,
        area INTEGER,
        bedrooms INTEGER,
        bathrooms INTEGER,
        stories INTEGER,
        mainroad VARCHAR(3),
        guestroom VARCHAR(3),
        basement VARCHAR(3),
        hotwaterheating VARCHAR(3),
        airconditioning VARCHAR(3),
        parking INTEGER,
        prefarea VARCHAR(3),
        furnishingstatus TEXT
        ) """)
    conn.commit()

'''
use a placeholder and the join method to quickly
the number of '?' needed.
Insert all the data from the csv to the database.
'''
def insert_items():
    conn = sqlite3.connect("housing.db")
    c = conn.cursor()
    
    placeholders =', '.join(['?'] * 13)
    c.executemany(f"INSERT INTO  housing_data Values({placeholders})", read_csv())
    conn.commit()
    
def show_all():
    conn = sqlite3.connect("housing.db")
    c = conn.cursor()
    
    c.execute("SELECT * FROM housing_data")
    record = c.fetchall()
    print(f"price area bedrooms bathrooms stories mainroad guestroom basement hotwaterheating airconditioning parking prefarea furnishingstatus")
    for r in record:
        print(f"{r[0]} {r[1]} {r[2]} {r[3]} {r[4]} {r[5]} {r[6]} {r[7]} {r[8]} {r[9]} {r[10]} {r[11]} {r[12]}")
''' 
1. Open the csv file.
2. Change the file data to the sqlite format.
3. Return data from csv.
'''
def read_csv():
    with open("Housing.csv", "rt") as file:
        reader = csv.reader(file)
        next(reader)
    
        data = []
        for list_items in reader:
            data.append(tuple(list_items))
            
        return data
        

create_table()
insert_items()
show_all()