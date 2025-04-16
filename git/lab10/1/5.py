import psycopg2
from config import load_config

def delete_by_name(name):
    """Удалить записи по имени"""
    sql = "DELETE FROM phonebooks WHERE name ILIKE %s"
    run_delete(sql, (f"%{name}%",), "имени")

def delete_by_number(number):
    """Удалить записи по номеру"""
    sql = "DELETE FROM phonebooks WHERE number = %s"
    run_delete(sql, (number,), "номеру")

def run_delete(sql, params, by):
    """Универсальная функция удаления"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                deleted = cur.rowcount
                conn.commit()
                if deleted:
                    print(f"Удалено записей по {by}: {deleted}")
                else:
                    print(f"Ничего не найдено по {by}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при удалении:", error)

if __name__ == '__main__':
    print("Удаление из phonebooks:")
    print("1 - Удалить по имени")
    print("2 - Удалить по номеру")

    choice = input("Ваш выбор: ")

    if choice == '1':
        name = input("Введите имя (или часть): ")
        delete_by_name(name)
    elif choice == '2':
        number = input("Введите номер телефона: ")
        delete_by_number(number)
    else:
        print("Неверный выбор.")
