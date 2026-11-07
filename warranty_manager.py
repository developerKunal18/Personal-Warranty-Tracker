from datetime import date, timedelta

from storage import load_warranties, save_warranties
from utils import get_warranty_status, get_days_remaining
from config import UPCOMING_DAYS


def add_warranty(product_name, brand, purchase_date, expiry_date, price, store):
    warranties = load_warranties()

    warranty = {
        "id": max([item["id"] for item in warranties], default=0) + 1,
        "product_name": product_name,
        "brand": brand,
        "purchase_date": purchase_date,
        "expiry_date": expiry_date,
        "price": price,
        "store": store
    }

    warranties.append(warranty)
    save_warranties(warranties)

    print("\nWarranty added successfully!")


def view_warranties():
    warranties = load_warranties()

    if not warranties:
        print("\nNo warranty records found.")
        return

    print("\n" + "-" * 100)
    print(
        f"{'ID':<5} {'Product':<20} {'Brand':<15} "
        f"{'Purchase Date':<15} {'Expiry Date':<15} {'Status':<15}"
    )
    print("-" * 100)

    for item in warranties:
        status = get_warranty_status(item["expiry_date"])

        print(
            f"{item['id']:<5} "
            f"{item['product_name']:<20} "
            f"{item['brand']:<15} "
            f"{item['purchase_date']:<15} "
            f"{item['expiry_date']:<15} "
            f"{status:<15}"
        )

    print("-" * 100)


def search_warranty(keyword):
    warranties = load_warranties()

    results = [
        item for item in warranties
        if keyword.lower() in item["product_name"].lower()
        or keyword.lower() in item["brand"].lower()
    ]

    if not results:
        print("\nNo matching warranties found.")
        return

    print("\nSearch Results:")

    for item in results:
        print(
            f"ID: {item['id']} | "
            f"Product: {item['product_name']} | "
            f"Brand: {item['brand']} | "
            f"Expiry: {item['expiry_date']} | "
            f"Status: {get_warranty_status(item['expiry_date'])}"
        )


def view_expiring_warranties():
    warranties = load_warranties()
    today = date.today()
    last_day = today + timedelta(days=UPCOMING_DAYS)

    expiring = [
        item for item in warranties
        if today <= date.fromisoformat(item["expiry_date"]) <= last_day
    ]

    if not expiring:
        print(f"\nNo warranties expiring within {UPCOMING_DAYS} days.")
        return

    print(f"\nWarranties expiring within {UPCOMING_DAYS} days:")

    for item in expiring:
        days_left = get_days_remaining(item["expiry_date"])

        print(
            f"ID: {item['id']} | "
            f"Product: {item['product_name']} | "
            f"Expiry: {item['expiry_date']} | "
            f"Days Left: {days_left}"
        )


def view_expired_warranties():
    warranties = load_warranties()

    expired = [
        item for item in warranties
        if get_warranty_status(item["expiry_date"]) == "Expired"
    ]

    if not expired:
        print("\nNo expired warranties found.")
        return

    print("\nExpired Warranties:")

    for item in expired:
        print(
            f"ID: {item['id']} | "
            f"Product: {item['product_name']} | "
            f"Expiry: {item['expiry_date']}"
        )


def delete_warranty(warranty_id):
    warranties = load_warranties()

    updated_warranties = [
        item for item in warranties
        if item["id"] != warranty_id
    ]

    if len(updated_warranties) == len(warranties):
        print("\nWarranty ID not found.")
        return

    save_warranties(updated_warranties)
    print("\nWarranty deleted successfully.")
