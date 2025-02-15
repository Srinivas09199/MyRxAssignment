'''Design an immutable class with following attributes 
String name; 
String Id, 
Date dateOfJoining 
List<Address> addresses;'''
from dataclasses import dataclass, field
from typing import List
from datatime import date

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str
    zipcode: str

@dataclass(frozen=True)
class Employee:
    name: str
    Id: str
    date_of_joining: date
    addresses: List[Address] = field(default_factory=list)
    
if __name__ == '__main__':
    address1 = Address('203 Gachibowli St', 'Hyderabad', 'TG', '500032')
    address2 = Address('201 Telecomerce St', 'Hyderabad', 'TG', '500032')
    
    employee = Employee(
        name = 'Raghu', 
        Id = '501', 
        date_of_joining = date(2021, 6, 19), 
        addresses = [address1, address2]
    )
print(employee)