import re
from us.states import lookup  # https://github.com/unitedstates/python-us
from usaddress import parse  # https://github.com/datamade/usaddress
import addressmaker


class Property:
    def __init__(self, address, square_feet, property_type, sales_status):
        self.update_address(address)
        self.square_feet = square_feet
        self.property_type = property_type
        self.sales_status = addressmaker.sales_status(sales_status)

    def update_address(self, address):
        parsed_address = parse(address)
        zip_code = addressmaker.zip_code(parsed_address)
        while not addressmaker.valid_zip(zip_code):
            self.zip_code = input('Invalid zip code. Enter a valid US zip code: ')
            zip_code = self.zip_code
        else:
            self.zip_code = zip_code
        self.street_address = addressmaker.street_address(parsed_address)
        self.city = addressmaker.city(parsed_address, self.zip_code)
        self.state = lookup(addressmaker.state(parsed_address, self.zip_code))

    def __str__(self):
        address = [self.street_address, self.city, str(self.state), self.zip_code]  # self.state
        address_asString = ', '.join(address)

        return f'Address: {address_asString}, ' \
               f'Square Feet: {self.square_feet}, ' \
               f'Home Style: {self.property_type}, ' \
               f'Sales Status: {self.sales_status}'

    # Note: no verification is done if record is manually edited, though is re-validated on reading from CSV file.
    # This solves database incongruities but can introduce errors into database,
    # and will be annoying for user if the database has incorrect information (incorrect cities for zip, etc).
    def update_street_address(self, street_address):
        self.street_address = street_address

    def update_city(self, city):
        self.city = city

    def update_state(self, state):
        self.state = lookup(state)

    def update_zip(self, zip_code):
        zip_code = re.sub(r'[0-9\-]', '', zip_code)
        while not addressmaker.valid_zip(zip_code):
            self.zip_code = input('Invalid zip code. Enter a valid US zip code: ')
            zip_code = self.zip_code
        else:
            self.zip_code = zip_code

    def update_square_footage(self, square_feet):
        if square_feet.isnumeric():
            self.square_feet = square_feet

    def update_property_type(self, property_type):
        self.property_type = property_type

    def update_sales_status(self, sales_status):
        self.sales_status = addressmaker.sales_status(sales_status)
