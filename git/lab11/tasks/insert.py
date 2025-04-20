import psycopg2
from config import load_config


def upsert_user_phone(name, surname, phone):
    """Insert new user or update phone if user exists"""
    # Check if user exists
    check_sql = """SELECT id, number FROM phonebooks 
                   WHERE name = %s AND surname = %s"""

    # SQL for insert and update
    insert_sql = """INSERT INTO phonebooks(name, surname, number)
                    VALUES(%s, %s, %s) RETURNING id;"""
    update_sql = """UPDATE phonebooks SET number = %s
                    WHERE name = %s AND surname = %s;"""

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Check if user exists
                cur.execute(check_sql, (name, surname))
                result = cur.fetchone()

                if result:
                    user_id, current_number = result
                    if current_number != phone:
                        # Update if phone is different
                        cur.execute(update_sql, (phone, name, surname))
                        conn.commit()
                        print(f"Updated phone for {name} {surname} from {current_number} to {phone}")
                    else:
                        print(f"Phone number for {name} {surname} is already {phone}")
                else:
                    # Insert new user
                    cur.execute(insert_sql, (name, surname, phone))
                    user_id = cur.fetchone()[0]
                    conn.commit()
                    print(f"Inserted new user {name} {surname} with ID {user_id}")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def upsert_from_console():
    """Get user input and call upsert function"""
    print("Enter user details (or 'exit' to stop):")
    while True:
        name = input("Enter name: ").strip()
        if name.lower() == 'exit':
            break
        surname = input("Enter surname: ").strip()
        phone = input("Enter phone number: ").strip()
        upsert_user_phone(name, surname, phone)


if __name__ == '__main__':
    upsert_from_console()