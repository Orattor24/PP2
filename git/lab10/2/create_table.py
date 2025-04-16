import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database """
    commands = [
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        """
    ]#
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("Database error:", error)

if __name__ == '__main__':
    create_tables()
