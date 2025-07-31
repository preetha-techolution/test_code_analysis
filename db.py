import sqlite3

DB_NAME = "hotel.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            room_number INTEGER PRIMARY KEY,
            is_occupied INTEGER DEFAULT 0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            room_number INTEGER,
            checkin_time TEXT,
            FOREIGN KEY (room_number) REFERENCES rooms (room_number)
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM rooms")
    if cursor.fetchone()[0] == 0:
        for i in range(1, 6):
            cursor.execute("INSERT INTO rooms (room_number) VALUES (?)", (i,))
    conn.commit()
