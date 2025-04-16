import psycopg2
from config import load_config

def insert_phonebook_entry(name, number):
    """Insert a single entry into the phonebooks table"""
    sql = """INSERT INTO phonebooks(name, number)
             VALUES(%s, %s) RETURNING id;"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
      #      with conn.cursor() as cur:
                cur.execute(sql, (name, number))
                entry_id = cur.fetchone()[0]
                conn.commit()
                print(f"Inserted entry with ID {entry_id}")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

def insert_from_console():
    """Insert entries manually from user input"""
    print("Enter 'exit' as name to stop.")
    while True:
        name = input("Enter name: ")
        if name.lower() == 'exit':
            break
        number = input("Enter number: ")
        insert_phonebook_entry(name, number)

if __name__ == '__main__':
    insert_from_console()
