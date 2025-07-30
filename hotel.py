import datetime

class Hotel:
    def __init__(self, total_rooms=10):
        self.total_rooms = total_rooms
        self.rooms = {i: None for i in range(1, total_rooms + 1)}
        self.customers = {}

    def check_availability(self):
        print("\nAvailable Rooms:")
        available = [room for room, guest in self.rooms.items() if guest is None]
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
            if room not in self.rooms or self.rooms[room] is not None:
                print("Room not available or invalid.")
                return
            customer_id = len(self.customers) + 1
            self.rooms[room] = customer_id
            self.customers[customer_id] = {
                "name": name,
                "phone": phone,
                "room": room,
                "checkin": datetime.datetime.now()
            }
            print(f"Room {room} booked successfully for {name}.")
        except ValueError:
            print("Invalid input. Room number should be an integer.")

    def view_customers(self):
        if not self.customers:
            print("No customers found.")
            return
        print("\nCurrent Customers:")
        for cid, info in self.customers.items():
            print(f"ID: {cid}, Name: {info['name']}, Room: {info['room']}, Phone: {info['phone']}, Check-in: {info['checkin']}")

    def checkout(self):
        try:
            room = int(input("Enter room number to checkout: "))
            customer_id = self.rooms.get(room)
            if customer_id is None:
                print("Room is not occupied.")
                return
            customer = self.customers.pop(customer_id)
            self.rooms[room] = None
            checkout_time = datetime.datetime.now()
            stay_duration = checkout_time - customer["checkin"]
            print(f"{customer['name']} has checked out of room {room}. Stay duration: {stay_duration}")
        except ValueError:
            print("Invalid input. Room number should be an integer.")

def main():
    hotel = Hotel(total_rooms=5)

    while True:
        print("\n--- Hotel Management System ---")
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
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
