from warranty_manager import (
    add_warranty,
    view_warranties,
    search_warranty,
    view_expiring_warranties,
    view_expired_warranties,
    delete_warranty
)

from utils import get_valid_date, get_valid_amount
from storage import initialize_storage


def display_menu():
    print("\n========== PERSONAL WARRANTY TRACKER ==========")
    print("1. Add Warranty")
    print("2. View All Warranties")
    print("3. Search Warranty")
    print("4. View Expiring Warranties")
    print("5. View Expired Warranties")
    print("6. Delete Warranty")
    print("7. Exit")
    print("===============================================")


def main():
    initialize_storage()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            product_name = input("Enter product name: ").strip()
            brand = input("Enter brand: ").strip()
            purchase_date = get_valid_date("Enter purchase date (YYYY-MM-DD): ")
            expiry_date = get_valid_date("Enter warranty expiry date (YYYY-MM-DD): ")
            price = get_valid_amount("Enter product price: ")
            store = input("Enter store name: ").strip()

            if not product_name:
                print("Product name cannot be empty.")
                continue

            if expiry_date < purchase_date:
                print("Expiry date cannot be before purchase date.")
                continue

            add_warranty(
                product_name,
                brand,
                purchase_date,
                expiry_date,
                price,
                store
            )

        elif choice == "2":
            view_warranties()

        elif choice == "3":
            keyword = input("Enter product name or brand: ").strip()
            search_warranty(keyword)

        elif choice == "4":
            view_expiring_warranties()

        elif choice == "5":
            view_expired_warranties()

        elif choice == "6":
            try:
                warranty_id = int(input("Enter warranty ID to delete: "))
                delete_warranty(warranty_id)
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "7":
            print("Thank you for using Personal Warranty Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
