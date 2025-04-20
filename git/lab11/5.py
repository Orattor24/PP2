import psycopg2
from config import load_config

def delete_by_name(name):
    """Удалить конкретную запись по имени (если совпадений несколько — выбор)"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Найдём все подходящие записи
                cur.execute("SELECT id, name, number FROM phonebooks WHERE name ILIKE %s", (f"{name}%",))

                results = cur.fetchall()

                if not results:
                    print("Ничего не найдено по имени.")
                    return

                # Показать список найденных записей
                print("Найденные записи:")
                for i, row in enumerate(results):
                    print(f"{i + 1}. ID: {row[0]}, Имя: {row[1]}, Номер: {row[2]}")

                # Спросить пользователя, какую запись удалить
                choice = input("Введите номер записи, которую нужно удалить (или '0' для отмены): ")
                if not choice.isdigit() or not (0 <= int(choice) <= len(results)):
                    print("Неверный ввод.")
                    return

                index = int(choice)
                if index == 0:
                    print("Удаление отменено.")
                    return

                # Получить ID выбранной записи
                record_id = results[index - 1][0]
                cur.execute("DELETE FROM phonebooks WHERE id = %s", (record_id,))
                conn.commit()
                print("Запись удалена.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при удалении:", error)


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
