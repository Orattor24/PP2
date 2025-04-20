import psycopg2
from config import load_config

def query_by_id(entry_id, new_name=None, new_number=None):
    """Поиск по ID и обновление записи, если она существует"""
    # Сначала вручную проверим, существует ли запись
    check_sql = "SELECT * FROM phonebooks WHERE id = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(check_sql, (entry_id,))
                result = cur.fetchone()
                if not result:
                    print(f"Запись с ID {entry_id} не найдена. Обновление невозможно.")
                    return  # Выходим, если нет такой записи

                print("Найдена запись:")
                print(f"ID: {result[0]}, Name: {result[1]}, Number: {result[2]}")

                if not new_name and not new_number:
                    print("Нечего обновлять.")
                    return

                updates = []
                values = []

                if new_name:
                    updates.append("name = %s")
                    values.append(new_name)
                if new_number:
                    updates.append("number = %s")
                    values.append(new_number)

                values.append(entry_id)

                update_sql = f"""
                UPDATE phonebooks
                SET {', '.join(updates)}
                WHERE id = %s
                """

                cur.execute(update_sql, tuple(values))
                print(f"Запись с ID {entry_id} успешно обновлена.")

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при обновлении:", error)

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
    print("Обновление записи в таблице phonebooks.")

    try:
        entry_id = int(input("Введите ID записи для обновления: "))

        # Сначала проверим, существует ли запись
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM phonebooks WHERE id = %s", (entry_id,))
                result = cur.fetchone()
                if not result:
                    print(f"Запись с ID {entry_id} не найдена. Обновление невозможно.")
                else:
                    print("Найдена запись:")
                    print(f"ID: {result[0]}, Name: {result[1]}, Number: {result[2]}")

                    new_name = input("Введите новое имя (оставьте пустым, если не менять): ").strip()
                    new_number = input("Введите новый номер (оставьте пустым, если не менять): ").strip()

                    query_by_id(entry_id,
                                new_name if new_name else None,
                                new_number if new_number else None)
    except ValueError:
        print("Некорректный ID.")

