def check_availability(cursor):
    cursor.execute("SELECT room_number FROM rooms WHERE is_occupied = 0")
    return [row[0] for row in cursor.fetchall()]

def book_room(cursor, room_number):
    cursor.execute("UPDATE rooms SET is_occupied = 1 WHERE room_number = ?", (room_number,))

def checkout_room(cursor, room_number):
    cursor.execute("UPDATE rooms SET is_occupied = 0 WHERE room_number = ?", (room_number,))
