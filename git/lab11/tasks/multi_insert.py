import psycopg2
from config import load_config


def validate_phone_number(phone):
    """Basic phone number validation"""
    # Remove all non-digit characters
    cleaned = ''.join(c for c in phone if c.isdigit())

    # Check for reasonable length (7-15 digits is typical for int'l numbers)
    if len(cleaned) < 7 or len(cleaned) > 15:
        return False, "Phone number should be 7-15 digits long"

    # Check if it starts with a valid country code or local prefix
    # This is a simple example - adjust based on your requirements
    if cleaned.startswith('0'):
        return False, "Phone numbers shouldn't start with 0 (use country code)"

    return True, "Valid phone number"


def bulk_insert_users(user_list):
    """
    Insert multiple users with phone validation
    Args:
        user_list: List of tuples (name, surname, phone)
    Returns:
        tuple: (success_count, error_entries)
        where error_entries is list of (user_data, error_message)
    """
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

                    # Validate phone number
                    is_valid, validation_msg = validate_phone_number(phone)

                    if not is_valid:
                        error_entries.append((user, validation_msg))
                        continue

                    # Try to insert
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
        return (0, [(None, f"Connection error: {error}")])

    return (success_count, error_entries)


def get_user_list_from_console():
    """Get list of users from console input"""
    user_list = []
    print("Enter user details (or 'exit' to stop):")
    print("Format for each user: name,surname,phone")
    while True:
        user_input = input("Enter user (or 'exit'): ").strip()
        if user_input.lower() == 'exit':
            break

        parts = [part.strip() for part in user_input.split(',')]
        if len(parts) != 3:
            print("Invalid format. Please use: name,surname,phone")
            continue

        user_list.append(tuple(parts))

    return user_list


if __name__ == '__main__':
    users = get_user_list_from_console()
    if users:
        success_count, errors = bulk_insert_users(users)

        print(f"\nResults:")
        print(f"Successfully inserted: {success_count}")
        print(f"Failed to insert: {len(errors)}")

        if errors:
            print("\nError details:")
            for user_data, error_msg in errors:
                if user_data:
                    print(f"User: {user_data[0]} {user_data[1]}, Phone: {user_data[2]}")
                print(f"Error: {error_msg}\n")