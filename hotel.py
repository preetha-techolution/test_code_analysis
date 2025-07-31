import sqlite3
import datetime

DB_NAME = "hotel.db"

class HotelDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self._initialize_tables()

    def _initialize_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS rooms (
                room_number INTEGER PRIMARY KEY,
                is_occupied INTEGER DEFAULT 0
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                room_number INTEGER,
                checkin_time TEXT,
                checkout_time TEXT,
                FOREIGN KEY (room_number) REFERENCES rooms (room_number)
            )
        ''')
        self.conn.commit()

        # Populate rooms if not already
        self.cursor.execute("SELECT COUNT(*) FROM rooms")
        if self.cursor.fetchone()[0] == 0:
            for i in range(1, 6):  # Initialize 5 rooms
                self.cursor.execute("INSERT INTO rooms (room_number) VALUES (?)", (i,))
            self.conn.commit()

    def check_availability(self):
        self.cursor.execute("SELECT room_number FROM rooms WHERE is_occupied = 0")
        available = [row[0] for row in self.cursor.fetchall()]
        print("\nAvailable Rooms:")
        if not available:
            print("No rooms available.")
        else:
            print("Rooms:", available)

    def book_room(self):
        name = input("Enter customer name: ")
        phone = input("Enter phone number: ")
        self.check_availability()

        try:
            room = int(input("Enter room number to book: "))
            self.cursor.execute("SELECT is_occupied FROM rooms WHERE room_number = ?", (room,))
            result = self.cursor.fetchone()

            if not result or result[0] == 1:
                print("Room not available or invalid.")
                return

            checkin_time = datetime.datetime.now().isoformat()
            self.cursor.execute('''
                INSERT INTO customers (name, phone, room_number, checkin_time)
                VALUES (?, ?, ?, ?)
            ''', (name, phone, room, checkin_time))
            self.cursor.execute("UPDATE rooms SET is_occupied = 1 WHERE room_number = ?", (room,))
            self.conn.commit()
            print(f"Room {room} booked successfully for {name}.")
        except ValueError:
            print("Invalid input. Room number should be an integer.")

    def view_customers(self):
        self.cursor.execute("SELECT id, name, phone, room_number, checkin_time FROM customers WHERE checkout_time IS NULL")
        customers = self.cursor.fetchall()
        if not customers:
            print("No active customers.")
            return
        print("\nCurrent Customers:")
        for row in customers:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Room: {row[3]}, Check-in: {row[4]}")


    def close(self):
        self.conn.close()

def main():
    hotel = HotelDB()

    while True:
        print("\n--- Hotel Management System (DB Powered) ---")
        print("1. Book Room")
        print("2. View Customers")
        print("3. Check Room Availability")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            hotel.book_room()
        elif choice == '2':
            hotel.view_customers()
        elif choice == '3':
            hotel.check_availability()
        elif choice == '4':
            hotel.checkout()
        elif choice == '5':
            print("Exiting system.")
            hotel.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
