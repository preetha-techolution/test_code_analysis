from rooms import check_availability, book_room
from customers import add_customer

def book_room_flow(cursor, conn):
    available = check_availability(cursor)
    
    if not available:
        print("No rooms available.")
        return

    print("Available rooms:", available)
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")

    try:
        room_number = int(input("Choose room number: "))
        if room_number not in available:
            raise ValueError("Room not available")

        add_customer(cursor, name, phone, room_number)
        book_room(cursor, room_number)
        conn.commit()
        print("Room booked successfully.")

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An error occurred while booking:", e)
