import psycopg2
from config import load_config


def upsert_user_phone(name, surname, phone):
    """Вставляем нового пользователя или же обновляем если существует"""
    # Проверка есть ли пользователь
    check_sql = """SELECT id, number FROM phonebooks 
                   WHERE name = %s AND surname = %s"""

    # Команды чтобы вставить / обновить
    insert_sql = """INSERT INTO phonebooks(name, surname, number)
                    VALUES(%s, %s, %s) RETURNING id;"""
    update_sql = """UPDATE phonebooks SET number = %s
                    WHERE name = %s AND surname = %s;"""

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Проверка существования
                cur.execute(check_sql, (name, surname))
                result = cur.fetchone()
                #Если все таки правда. То обновляем
                if result:
                    user_id, current_number = result
                    if current_number != phone:
                        # Update if phone is different
                        cur.execute(update_sql, (phone, name, surname))
                        conn.commit()
                        print(f"Обновление пользователя {name} {surname} номер телефона с {current_number} на {phone}")
                    else:
                        print(f"Номер телефона для {name} {surname} стал {phone}")
                else:
                    # Вставка нового пользователя
                    cur.execute(insert_sql, (name, surname, phone))
                    user_id = cur.fetchone()[0]
                    conn.commit()
                    print(f"Добавлен новый пользователь {name} {surname} у которого айди {user_id}")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка:", error)


def upsert_from_console():
    """Забираем инпуты"""
    print("Вводим информацию (или введи команду 'exit' чтобы остановить):")
    while True:
        name = input("Введи имя: ").strip()
        if name.lower() == 'exit':
            break
        surname = input("Фамилия: ").strip()
        phone = input("Номер телефона: ").strip()
        upsert_user_phone(name, surname, phone)


if __name__ == '__main__':
    upsert_from_console()