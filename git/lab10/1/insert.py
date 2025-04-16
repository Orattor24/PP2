import psycopg2
from config import load_config


#
def insert_many_phonebook_entries(entries):
    """Вставка нескольких записей в таблицу phonebooks"""
    sql = "INSERT INTO phonebooks(name, number) VALUES(%s, %s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, entries)
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':


    insert_many_phonebook_entries([
        ("Alice", "1234567890"),
        ('Bob', '9876543210'),
        ('Charlie', '5551234567'),
        ('Dave', '4449876543')
    ])
