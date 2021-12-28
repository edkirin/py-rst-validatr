from models import CompanyAddressBook

OUT_JSON_FILE = "/tmp/address_book.json"


if __name__ == '__main__':
    print("Creating data...")
    orders = CompanyAddressBook.create(
        number_of_companies=10000,
        number_of_employees=100,
    )

    print(f"Writing data to '{OUT_JSON_FILE}'...")
    with open(OUT_JSON_FILE, "w") as f:
        f.write(orders.json())

    print("Done.")
