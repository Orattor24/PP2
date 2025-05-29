import psycopg2
from config import load_config


def query_with_pagination(limit=5, offset=0, name_filter=None, surname_filter=None, number_filter=None):

    base_sql = "SELECT * FROM phonebooks" #берем все из датабазы
    count_sql = "SELECT COUNT(*) FROM phonebooks" #количество береем

    filters = [] #какие фильртры есть
    params = [] #Условия для фильтров

    # Фильтруем по всяким признакам
    if name_filter:
        filters.append("name ILIKE %s")
        params.append(f"%{name_filter}%")
    if surname_filter:
        filters.append("surname ILIKE %s")
        params.append(f"%{surname_filter}%")
    if number_filter:
        filters.append("number = %s")
        params.append(number_filter)

    where_clause = " WHERE " + " AND ".join(filters) if filters else ""

    # Добавляем нумерацию страниц для очереди
    paginated_sql = f"{base_sql}{where_clause} ORDER BY id LIMIT %s OFFSET %s"
    count_sql += where_clause

    config = load_config()
    records = []
    total_count = 0

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Получить окончательное количество
                cur.execute(count_sql, params)
                total_count = cur.fetchone()[0]

                # Результат страницы
                cur.execute(paginated_sql, params + [limit, offset])
                records = cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка в очереди:", error)
        return ([], 0)

    return (records, total_count)


def display_paginated_results():
    """Тут сделай интерактивный интерфейс для управления"""
    limit = 5  #Обычный размер карты
    offset = 0
    current_page = 1
    total_pages = 1

    # Фильтры
    name_filter = None
    surname_filter = None
    number_filter = None

    while True:
        # список с введеными параметрами фильтра
        records, total_count = query_with_pagination(
            limit=limit,
            offset=offset,
            name_filter=name_filter,
            surname_filter=surname_filter,
            number_filter=number_filter
        )

        total_pages = max(1, (total_count + limit - 1) // limit)

        #Результаты всего этого выводится
        print("\n=== Номерная книжка ===")
        print(f"Страница {current_page} из {total_pages} (Всего: {total_count} записей)")
        print("------------------------")

        if records:
            for record in records:
                print(f"ID: {record[0]}, Name: {record[1]}, Surname: {record[2]}, Number: {record[3]}")
        else:
            print("Не найдено записей.")

        # Меню
        print("\nНастройки:")
        print("n - Следующая страница")
        print("p - Предыдущая страница")
        print("f - Применить фильтр")
        print("c - Очистить фильтр")
        print("l - Изменить размер страницы")
        print("q - Выход")

        choice = input("Твой выбор: ").lower()

        if choice == 'n' and current_page < total_pages:
            offset += limit
            current_page += 1
        elif choice == 'p' and current_page > 1:
            offset -= limit
            current_page -= 1
        elif choice == 'f':
            name_filter = input("Фильтровать по имени (пропуск сделай, если нечего менять): ").strip() or None
            surname_filter = input("Фильтровать по фамилии (пропуск сделай, если нечего менять): ").strip() or None
            number_filter = input("Фильтровать по номеру (пропуск сделай, если нечего менять): ").strip() or None
            offset = 0  # После изменений чтобы вернуться на первую страницу
            current_page = 1
        elif choice == 'c':
            name_filter = None
            surname_filter = None
            number_filter = None
            offset = 0
            current_page = 1
        elif choice == 'l':
            try:
                new_limit = int(input(f"Текущий размер страницы: {limit}. Введи новый размер: "))
                if new_limit > 0:
                    limit = new_limit
                    offset = 0  # Вернуться на 1 страницу если изменили размер страницы
                    current_page = 1
                else:
                    print("Размер страницы должен быть положительным")
            except ValueError:
                print("Ошибка какая то ")
        elif choice == 'q':
            break
        else:
            print("Неверный размер или нет больше доступных")


if __name__ == '__main__':
    display_paginated_results()