import psycopg2
from config import load_config

def query_all():
    """Вывод всех записей"""
    sql = "SELECT * FROM phonebooks"
    run_query(sql)

def query_by_name(name):
    """Поиск по имени (частичное совпадение)"""
    sql = "SELECT * FROM phonebooks WHERE name ILIKE %s"
    run_query(sql, (f"%{name}%",))

def query_by_number(number):
    """Поиск по номеру (точное совпадение)"""
    sql = "SELECT * FROM phonebooks WHERE number = %s"
    run_query(sql, (number,))

def query_by_id(entry_id):
    """Поиск по ID"""
    sql = "SELECT * FROM phonebooks WHERE id = %s"
    run_query(sql, (entry_id,))

def run_query(sql, params=None):
    """Универсальное выполнение запроса и вывод результатов"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params or ())
                rows = cur.fetchall()
                if rows:
                    print("\nРезультаты:")
                    for row in rows:
                        print(f"ID: {row[0]}, Name: {row[1]}, Number: {row[2]}")
                else:
                    print("Ничего не найдено.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при запросе:", error)

if __name__ == '__main__':
    print("Выберите фильтр для поиска:")
    print("1 - Все записи")
    print("2 - Поиск по имени")
    print("3 - Поиск по номеру")
    print("4 - Поиск по ID")

    choice = input("Ваш выбор: ")

    if choice == '1':
        query_all()
    elif choice == '2':
        name = input("Введите имя или часть имени: ")
        query_by_name(name)
    elif choice == '3':
        number = input("Введите номер телефона: ")
        query_by_number(number)
    elif choice == '4':
        try:
            entry_id = int(input("Введите ID: "))
            query_by_id(entry_id)
        except ValueError:
            print("Некорректный ID.")
    else:
        print("Неверный выбор.")
