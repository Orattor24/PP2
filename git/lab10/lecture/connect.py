import psycopg2
from config import load_config

def connect():
    """Подключение к серверу PostgreSQL"""
    try:
        # Загрузка параметров подключения
        config = load_config()
        # Подключение к серверу PostgreSQL
        with psycopg2.connect(**config) as conn:
            print('Подключение к серверу PostgreSQL успешно установлено.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(f'Ошибка: {error}')

if __name__ == '__main__':
    connect()
