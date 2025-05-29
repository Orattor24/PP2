import psycopg2
from config import load_config


def validate_phone_number(phone):
    """Базовая проверка номера телефона"""
    # Убрать все не цифорные персонажи
    cleaned = ''.join(c for c in phone if c.isdigit())

    # Проверка номер ли это телефона
    if len(cleaned) < 7 or len(cleaned) > 15:
        return False, "В номере телефона от 7-15 чисел"

    if cleaned.startswith('0'):
        return False, "Ни один номер телефона не начинается с 0"

    return True, "Доступный номер телефона"


def bulk_insert_users(user_list):
    insert_sql = """INSERT INTO phonebooks(name, surname, number)
                    VALUES(%s, %s, %s) RETURNING id;"""
    config = load_config()
    success_count = 0
    error_entries = []

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for user in user_list:
                    name, surname, phone = user

                    # доступный номер телефона?
                    is_valid, validation_msg = validate_phone_number(phone)

                    if not is_valid:
                        error_entries.append((user, validation_msg))
                        continue

                    # попытка добавить в бд
                    try:
                        cur.execute(insert_sql, (name, surname, phone))
                        entry_id = cur.fetchone()[0]
                        success_count += 1
                    except psycopg2.IntegrityError as e:
                        error_entries.append((user, f"Database error: {e}"))
                    except Exception as e:
                        error_entries.append((user, f"Unexpected error: {e}"))

                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        return (0, [(None, f"Проблема с соединением: {error}")])

    return (success_count, error_entries)


def get_user_list_from_console():
    """Получаем список пользователей из консоли"""
    user_list = []
    print("Введи детали пользователя (или 'exit' для выхода):")
    print("Формат для ввода: имя,фамилия,номер")
    while True:
        user_input = input("Введи пользователя (или 'exit'): ").strip()
        if user_input.lower() == 'exit':
            break

        parts = [part.strip() for part in user_input.split(',')]
        if len(parts) != 3:
            print("Неверный формат, пожалуйста введите: имя,фамилия,номер")
            continue

        user_list.append(tuple(parts))

    return user_list


if __name__ == '__main__':
    users = get_user_list_from_console()
    if users:
        success_count, errors = bulk_insert_users(users)

        print(f"\nРезультат:")
        print(f"Успешная вставка: {success_count}")
        print(f"Не получилось вставить: {len(errors)}")

        if errors:
            print("\nОшибка:")
            for user_data, error_msg in errors:
                if user_data:
                    print(f"User: {user_data[0]} {user_data[1]}, Phone: {user_data[2]}")
                print(f"Error: {error_msg}\n")