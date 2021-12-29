use serde::{Deserialize, Serialize};


type Error = Box<dyn std::error::Error>;


#[derive(Serialize, Deserialize, Debug)]
pub struct Address {
    address: String,
    city: String,
    postal_code: String,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct Employee {
    first_name: String,
    last_name: String,
    address: Address,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct Company {
    pub name: String,
    description: String,
    address: Address,
    ceo: Employee,
    employees: Vec<Employee>,
    number_of_employees: u32,
    exists_since: u16,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct CompanyAddressBook {
    pub year: u16,
    pub companies: Vec<Company>,
    pub number_of_companies: u32,
}


impl CompanyAddressBook {
    pub fn create_data_from_json(json_data: &str) -> Result<CompanyAddressBook, Error> {
        let value: CompanyAddressBook = serde_json::from_str(json_data)?;
        Ok(value)
    }
}
