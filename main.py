"""
Main entry point for the Properties database.
Allows you to add, delete, modify entries, and save the updated database.
Requests you open a database to work with.
It will not create a new database file from scratch, though it can save changes.
A database CSV file will have the following header:

Street Address,City,State,Zip,Square Feet,Property Type,Sales Status

followed by at least one valid address on the next row.

Included CSV files in the project are edited from a CSV file created by Zillow Exporter
https://www.zillowdataexporter.com/
"""

from os import getcwd
from us.states import lookup  # https://github.com/unitedstates/python-us
from csv import DictReader
from csv import DictWriter
from addressmaker import search_streetaddress as search
from property import Property
from tkinter.filedialog import asksaveasfilename
from tkinter import filedialog


# Reads a CSV file and puts them into a [List of Properties]
# Header: Street Address,City,State,Zip,Square Feet,Property Type,Sales Status
def read_file():
    try:
        property_list = filedialog.askopenfilename(initialdir=getcwd(),
                                                   title="Please select a file:",
                                                   filetypes=(("CSV files", "*.csv"),
                                                              ("Text files", "*.txt"),
                                                              ("All files", "*.*")))
        print('\nYou selected', property_list, '\nReading database.')
        with open(property_list, mode='r') as csv_file:  # todo handle corrupt or incorrectly formatted database
            csv_reader = DictReader(csv_file)
            properties = []
            line_count = 0
            # Reads each row in the CSV file, creates a Property from it and adds to the properties working dictionary.
            for row in csv_reader:
                address = f'{row["Street Address"]}, {row["City"]}, {row["State"]}, {row["Zip"]}'
                square_feet = f'{row["Square Feet"]}'
                property_type = f'{row["Property Type"]}'
                sales_status = f'{row["Sales Status"]}'
                properties.append(Property(address, square_feet, property_type, sales_status))
                print(
                    f'{row["Street Address"]}, {row["City"]}, {row["State"]}, {row["Zip"]}. '
                    f'{row["Square Feet"]}, '
                    f'{row["Property Type"]}, '
                    f'{row["Sales Status"]}')
                line_count += 1
            print(f'Processed {line_count} lines. \n')
            csv_file.close()

            return properties

    except FileNotFoundError:
        print('Error reading database. Please try again.')


# Searches for a property based on house number and start of street address if provided.
def property_search(property_list):
    term = input('Enter part of the street address, house number at minimum. '
                 'Use 0 for raw land with no house number. \n')
    return search(term, property_list)


# Adds a property to the current working properties dictionary.
def add_property(properties):
    address = input('Enter the full address or the property. Use 0 for a street number if raw property: \n'
                    'Use format: 123 Main Street, Middletown, PA, 17057 \n')
    square_feet = input('Enter the approximate square footage of homes on the property. \n'
                        'Use 0 for raw property: \n')
    property_type = input('Enter the property type of the property (Single Family, Multi Family, Lot/Land, Condo). \n')
    sales_status = input('Enter the sales status of the property (Available, Sold, under Contract). \n')
    properties.append(Property(address, square_feet, property_type, sales_status))
    main_menu(properties)


# Removes an entry from the database.
def remove_property(properties):
    print('REMOVE PROPERTY\n')
    print('OOPS! Enter any invalid entry to go back without deleting anything.')
    selected_property = property_search(properties)
    if selected_property in properties:
        properties.remove(selected_property)
    if selected_property is not None:
        print('\nREMOVED\n\n', selected_property, '\n\nfrom database.\n')
    main_menu(properties)


# Updates individual components of an address.
# Menu items act like a switch/case statement in other languages.
def update_property(properties):
    print('UPDATE PROPERTY\n')
    print('OOPS! Enter any invalid entry to go back without changing anything.')
    selected_property = property_search(properties)
    while True:
        if selected_property is None:
            break
        print('Use the following selections to edit the address, '
              'square footage, type, or sales status of a property: \n')
        print('\t1: Update street address')
        print('\t2: Update city')
        print('\t3: Update State')
        print('\t4: Update zip code')
        print('\t5: Update square footage')
        print('\t6: Update property type')
        print('\t7: Update sales status')
        print('\n\tAny other key exits the update menu')
        user_entry = input('\n?: ')
        if user_entry == '1':
            if selected_property in properties:
                properties.remove(selected_property)
            selected_property.update_street_address(input('Enter the updated street address: \n'))
            properties.append(selected_property)
        elif user_entry == '2':
            if selected_property in properties:
                properties.remove(selected_property)
            selected_property.update_city(input('Enter the updated city: \n'))
            properties.append(selected_property)
        elif user_entry == '3':
            if selected_property in properties:
                properties.remove(selected_property)
            selected_property.update_state(input('Enter the updated State: \n'))
            properties.append(selected_property)
        elif user_entry == '4':
            if selected_property in properties:
                properties.remove(selected_property)
            selected_property.update_zip(input('Enter the updated zip code: \n'))
            properties.append(selected_property)
        elif user_entry == '5':
            if selected_property in properties:
                properties.remove(selected_property)
            selected_property.update_square_footage(input('Enter the updated square footage: \n'))
            properties.append(selected_property)
        elif user_entry == '6':
            if selected_property in properties:
                properties.remove(selected_property)
            selected_property.update_property_type(input('Enter the updated property type: \n'))
            properties.append(selected_property)
        elif user_entry == '7':
            if selected_property in properties:
                properties.remove(selected_property)
            selected_property.update_sales_status(input('Enter the updated sales status '
                                                        '(Available, Sold, under Contract): \n'))
            properties.append(selected_property)
        else:
            break
    main_menu(properties)


# Prints the records in the database to the console.
# Can be used to verify an edit, addition, or deletion.
def print_properties(properties):
    for property_listing in properties:
        print(property_listing)
    main_menu(properties)


# Saves the records to a database, user can overwrite original database or create a new one.
def save_database(properties):
    database_file = asksaveasfilename(
        filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt"), ("All files", "*.*")],
        defaultextension=".csv")
    with open(database_file, mode='w') as csv_file:
        fieldnames = ['Street Address', 'City', 'State', 'Zip', 'Square Feet', 'Property Type', 'Sales Status']
        database_writer = DictWriter(csv_file, fieldnames=fieldnames)
        # Writes each record to the csv file
        database_writer.writeheader()
        for record in properties:
            state = lookup(str(record.state))
            database_writer.writerow({'Street Address': record.street_address,
                                      'City': record.city,
                                      'State': state.abbr,
                                      'Zip': record.zip_code,
                                      'Square Feet': record.square_feet,
                                      'Property Type': record.property_type,
                                      'Sales Status': record.sales_status})
    csv_file.close()
    main_menu(properties)


# The main menu for the program.
# Allows the user to create, delete, or update records.
def main_menu(properties):
    while True:
        if properties is None:
            break
        print('Use the following selections to edit, add, or delete a property: \n')
        print('\t1: Add a new property')
        print('\t2: Remove an existing property')
        print('\t3: Update an existing property')
        print('\tP: Print the current database')
        print('\tS: Save the updated database')
        print('\tQ: Quit PropertyMinder')
        user_entry = input('\n?: ')
        if user_entry == '1':
            add_property(properties)
            break
        elif user_entry == '2':
            remove_property(properties)
            break
        elif user_entry == '3':
            update_property(properties)
            break
        elif user_entry[0].upper() == 'P':
            print_properties(properties)
            break
        elif user_entry[0].upper() == 'S':
            save_database(properties)
            break
        elif user_entry[0].upper() == 'Q':
            save = input('Save the database? (y/n) \n?: ')
            if save[0].upper() == 'N':
                break
            elif save[0].upper() == 'Y':
                print('\nYou will be returned to the main menu after saving. Select Q again to quit.')
                save_database(properties)
                break
            print('Invalid selection After entering Q, enter Y to save the database, N to quit without saving.')


# Main entry point for the program.
# Prompts user for a CSV database to open, then opens the main menu.
def main():
    print('Welcome to PropertyMinder! \nPlease select a database file.')

    properties = read_file()
    if properties is not None:
        for property_listing in properties:
            print(property_listing)
    else:
        print('Error creating database. Please try again.')
    main_menu(properties)


if __name__ == '__main__':
    main()
