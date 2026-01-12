import business_logic

def main_menu():
    print("--- Library Management System ---")
    while True:
        choice = input("\n1. Add Book\n2. View Books\n3. Exit\nSelect: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            result = business_logic.add_new_book(title)
            print(result)
        elif choice == '2':
            books = business_logic.list_inventory()
            for b in books:
                print(f"- {b['title']} [{b['status']}]")
        elif choice == '3':
            break

if __name__ == "__main__":
    main_menu()
    