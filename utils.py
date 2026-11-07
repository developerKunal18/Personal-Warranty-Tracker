from datetime import datetime, date
from config import DATE_FORMAT


def get_valid_date(prompt):
    while True:
        value = input(prompt).strip()

        try:
            parsed_date = datetime.strptime(value, DATE_FORMAT).date()
            return parsed_date.isoformat()
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD format.")


def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            return amount
        except ValueError:
            print("Please enter a valid amount.")


def get_warranty_status(expiry_date):
    expiry = date.fromisoformat(expiry_date)
    today = date.today()

    if expiry < today:
        return "Expired"

    if expiry == today:
        return "Expires Today"

    return "Active"


def get_days_remaining(expiry_date):
    expiry = date.fromisoformat(expiry_date)
    return (expiry - date.today()).days
