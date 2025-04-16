import psycopg2
import csv
from config import load_config

def insert_from_csv(filename):
    """Insert multiple entries from a CSV file"""
    config = load_config()
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            entries = [(row['name'], row['number']) for row in reader]

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany("INSERT INTO phonebooks(name, number) VALUES (%s, %s)", entries)
                conn.commit()
                print(f"Inserted {len(entries)} entries from {filename}")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    filename = input("Enter CSV file name (e.g., phonebook.csv): ")
    insert_from_csv(filename)
