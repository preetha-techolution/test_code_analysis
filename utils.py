def print_customers(customers):
    if not customers:
        print("No customers found.")
    else:
        print("\nCurrent Customers:")
        for cust in customers:
            print(f"ID: {cust[0]}, Name: {cust[1]}, Phone: {cust[2]}, Room: {cust[3]}, Check-In: {cust[4]}")
