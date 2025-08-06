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

    

    

    def close(self):
        self.conn.close()

def main():
    hotel = HotelDB()

    while True:
        print("\n--- Hotel Management System (DB Powered) ---")
        print("1. Book Room")
        print("3. Check Room Availability")
        print("4. Checkout")
       

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
