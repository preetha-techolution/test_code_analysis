import datetime

def add_customer(cursor, name, phone, room_number):
    checkin_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO customers (name, phone, room_number, checkin_time)
        VALUES (?, ?, ?, ?)
    ''', (name, phone, room_number, checkin_time))

def list_customers(cursor):
    cursor.execute("SELECT * FROM customers WHERE checkout_time IS NULL")
    return cursor.fetchall()

def checkout_customer(cursor, room_number):
    checkout_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        UPDATE customers
        SET checkout_time = ?
        WHERE room_number = ? AND checkout_time IS NULL
    ''', (checkout_time, room_number))
