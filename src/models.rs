use serde::{Deserialize, Serialize};


#[derive(Serialize, Deserialize)]
pub struct Address {
    address: String,
    city: String,
    postal_code: String,
}

#[derive(Serialize, Deserialize)]
pub struct Employee {
    first_name: String,
    last_name: String,
    address: Address,
}

#[derive(Serialize, Deserialize)]
pub struct Company {
    pub name: String,
    description: String,
    address: Address,
    ceo: Employee,
    employees: Vec<Employee>,
    number_of_employees: u32,
    exists_since: u16,
}

#[derive(Serialize, Deserialize)]
pub struct CompanyAddressBook {
    pub year: u16,
    pub companies: Vec<Company>,
    pub number_of_companies: u32,
}
