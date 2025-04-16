import psycopg2
from config import load_config

def update_phonebook_entry(entry_id, new_name=None, new_number=None):
    """Обновить имя и/или номер записи в таблице phonebooks по ID"""
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

    sql = f"""
    UPDATE phonebooks
    SET {', '.join(updates)}
    WHERE id = %s
    """

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, tuple(values))
                if cur.rowcount > 0:
                    print(f"Запись с ID {entry_id} успешно обновлена.")
                else:
                    print(f"Запись с ID {entry_id} не найдена.")
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при обновлении:", error)

if __name__ == '__main__':
    print("Обн#овление записи в таблице phonebooks.")
    try:
        entry_id = int(input("Введите ID записи для обновления: "))
        new_name = input("Введите новое имя (оставьте пустым, если не менять): ").strip()
        new_number = input("Введите новый номер (оставьте пустым, если не менять): ").strip()

        # передаём None, если строка пустая
        update_phonebook_entry(entry_id,
                               new_name if new_name else None,
                               new_number if new_number else None)
    except ValueError:
        print("Некорректный ID.")
