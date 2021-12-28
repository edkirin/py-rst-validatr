from pydantic import BaseModel
from typing import List
from faker import Faker


fake = Faker()


class Address(BaseModel):
    address: str
    city: str
    postal_code: str

    @staticmethod
    def create() -> "Address":
        return Address(
            address=fake.address(),
            city=fake.city(),
            postal_code=fake.postcode(),
        )


class Employee(BaseModel):
    first_name: str
    last_name: str
    address: Address

    @staticmethod
    def create() -> "Employee":
        return Employee(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=Address.create(),
            email=fake.email(),
        )


class Company(BaseModel):
    name: str
    description: str
    address: Address
    ceo: Employee
    employees: List[Employee]
    number_of_employees: int
    exists_since: int

    @staticmethod
    def create(number_of_employees: int) -> "Company":
        return Company(
            name=fake.company(),
            description=fake.bs(),
            address=Address.create(),
            ceo=Employee.create(),
            employees=[Employee.create() for n in range(number_of_employees)],
            number_of_employees=number_of_employees,
            exists_since=fake.year(),
        )


class CompanyAddressBook(BaseModel):
    year: int
    companies: List[Company]
    number_of_companies: int

    @staticmethod
    def create(number_of_companies: int, number_of_employees: int) -> "CompanyAddressBook":
        return CompanyAddressBook(
            year=2022,
            companies=[
                Company.create(number_of_employees=number_of_employees)
                for _ in range(number_of_companies)
            ],
            number_of_companies=number_of_companies,
        )
