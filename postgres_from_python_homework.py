import psycopg2


def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS clients(
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(60) NOT NULL,
                last_name VARCHAR(60) NOT NULL,
                email VARCHAR(60) UNIQUE NOT NULL);
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phones(
                id SERIAL PRIMARY KEY,
                client_id INTEGER NOT NULL REFERENCES clients(id),
                phone VARCHAR(20) UNIQUE);
        """)
        conn.commit()


def add_client(conn, first_name, last_name, email):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO clients (first_name, last_name, email) VALUES(%s, %s, %s) RETURNING id, firstname, lastname;
        """, (first_name, last_name, email))
        client_id = cur.fetchone()
        conn.commit()


def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO phones(client_id, phone) VALUES(%s, %s);
        """, (client_id, phone))
        conn.commit()


def update_client(conn, client_id, first_name=None, last_name=None, email=None):
    with conn.cursor() as cur:
        if first_name:
            cur.execute("""
                UPDATE clients SET first_name = %s WHERE id = %s;
            """, (first_name, client_id))
        if last_name:
            cur.execute("""
                UPDATE clients SET lastname = %s WHERE id = %s;
            """, (last_name, client_id))
        if email:
            cur.execute("""
                UPDATE clients SET email = %s WHERE id = %s;
            """, (email, client_id))
        conn.commit()


def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM phones WHERE client_id = %s AND phone = %s;
        """, (client_id, phone))
    conn.commit()


def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM phones WHERE client_id = %s;
        """, (client_id,))
        cur.execute("""
            DELETE FROM clients WHERE id = %s;
        """, (client_id,))
        conn.commit()


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        query = """
            SELECT c.id, c.first_name, c.last_name, c.email, p.phone
            FROM clients c
            LEFT JOIN phones p ON c.id = p.client_id
            WHERE 1=1
        """
        params = []
        if first_name:
            query += " AND c.first_name = %s"
            params.append(first_name)
        if last_name:
            query += " AND c.last_name = %s"
            params.append(last_name)
        if email:
            query += " AND c.email = %s"
            params.append(email)
        if phone:
            query += " AND p.phone = %s"
            params.append(phone)
        
        cur.execute(query, params)
        results = cur.fetchall()
        if results:
            print("Найденные клиенты:")
            for row in results:
                print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Email: {row[3]}, Телефон: {row[4]}")
        else:
            print("Клиенты не найдены.")

if __name__ == '__main__':
    with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
        create_tables(conn)

        client1_id = add_client(conn, "Иван", "Иванов", "ivan@example.com")
        client2_id = add_client(conn, "Пётр", "Петров", "petr@example.com")

        add_phone(conn, client1_id, "1234567890")
        add_phone(conn, client1_id, "9876543210")
        add_phone(conn, client2_id, "5555555555")

        update_client(conn, client1_id, first_name="Сергей")
        find_client(conn, first_name="Сергей")

        delete_phone(conn, client1_id, "1234567890")
        find_client(conn, first_name="Сергей")

        delete_client(conn, client2_id)
        find_client(conn, first_name="Пётр")

        find_client(conn, first_name="Иван")
        find_client(conn, phone="5555555555")

conn.close()

