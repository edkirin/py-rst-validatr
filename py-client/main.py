from models import CompanyAddressBook
from time import perf_counter
import json

JSON_DATA_FILE = "/tmp/address_book.json"


def create_data():
    print("Creating data...")
    t = perf_counter()

    orders = CompanyAddressBook.create(
        number_of_companies=10000,
        number_of_employees=100,
    )
    print(f"[T] object creation: {perf_counter() - t}")

    print(f"Writing data to '{JSON_DATA_FILE}'...")
    with open(JSON_DATA_FILE, "w") as f:
        f.write(orders.json())

    print(f"[T] write file: {perf_counter() - t}")

    print("Done.")


def benchmark_read():
    print(f"Reading '{JSON_DATA_FILE}'...")
    t = perf_counter()

    with open(JSON_DATA_FILE, "r") as f:
        data = f.read()

    print(f"[T] read file: {perf_counter() - t}")

    print("Converting to dict...")
    address_book_dict = json.loads(data)
    print(f"[T] conversion to dict: {perf_counter() - t}")

    print("Creating CompanyAddressBook object...")
    address_book = CompanyAddressBook(**address_book_dict)
    print(f"[T] object creation: {perf_counter() - t}")
    print(f"Number of company objects: {len(address_book.companies)}")

    print("Done.")


if __name__ == '__main__':
    # create_data()
    benchmark_read()
