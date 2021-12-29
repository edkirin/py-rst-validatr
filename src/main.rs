mod models;

use std::fs::File;
use std::io::prelude::*;
use models::CompanyAddressBook;
use std::time::Instant;

const JSON_DATA_FILENAME: &str = "/tmp/address_book.json";


fn read_from_file(filename: &str) -> Result<String, std::io::Error> {
    let mut file = File::open(filename)?;
    let mut data = String::new();
    file.read_to_string(&mut data)?;
    Ok(data)
}


fn main() {
    let start = Instant::now();
    match read_from_file(JSON_DATA_FILENAME) {
        Ok(json_data) => {
            println!("[T] read_from_file: {:?}", start.elapsed());
            let start = Instant::now();
            match CompanyAddressBook::create_data_from_json(&json_data) {
                Ok(address_book) => {
                    println!("[T] create_data_from_json: {:?}", start.elapsed());
                    println!(
                        "'{}' file size: {}MB",
                         JSON_DATA_FILENAME,
                        std::fs::metadata(JSON_DATA_FILENAME).unwrap().len() / 1024 / 1024
                    );
                    println!("Number of company objects: {}", address_book.number_of_companies);

                    // for company in address_book.companies {
                    //     println!("{}", company.name);
                    // }
                }
                Err(err) => {
                    println!("Error parsing json: {}", err);
                }
            }
        }
        Err(err) => {
            println!("Error reading file '{}': {}", JSON_DATA_FILENAME, err);
        }
    }
}
