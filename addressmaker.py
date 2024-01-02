"""
Returns the probable US street address, city, State, and zip code as parsed by usaddress,
https://github.com/datamade/usaddress
then verified through uszipcode.
https://github.com/MacHu-GWU/uszipcode-project
"""
import re
from pandas import Series  # https://pandas.pydata.org/
from us.states import lookup  # https://github.com/unitedstates/python-us
from uszipcode import SearchEngine  # https://github.com/MacHu-GWU/uszipcode-project


# Defines property address based on the parsed data.
def street_address(address):
    street = []
    for pair in address:
        if 'AddressNumber' in pair:
            street.append(pair[0])
        if 'StreetName' in pair:
            street.append(pair[0])
        if 'StreetNamePostType' in pair:
            street.append(pair[0])

    return re.sub(r'[^a-zàáéġñöA-Z0-9\'\- ]', '', ' '.join(street))


# Verifies address matches zip code
def city(address, zip_code):
    place_name = []
    for pair in address:
        if 'PlaceName' in pair:
            place_name.append(pair[0])
    # regex expression will fail in Hawaii. https://en.wikipedia.org/wiki/List_of_U.S._cities_with_diacritics
    entered_city = re.sub(r'[^a-zàáéġñöA-Z0-9\'\- ]', '', ' '.join(place_name))
    verify = SearchEngine().by_zipcode(zip_code[:5]).to_OrderedDict()
    # print(verify)
    zip_data = Series(verify)
    city_list = zip_data['common_city_list']
    if entered_city not in city_list:
        if entered_city != '':
            print('The city for this property does not match city in zip code database: ')
            print(' '.join([value[0] for value in address]))
            print('Enter 0 to retain', entered_city)
            i = 1
            for cities in city_list:
                print('Enter', i, 'to use', cities)
            index = -1
            entry = input('? ')
            if entry.isnumeric():
                index = int(entry) - 1
            if index != -1:
                entered_city = city_list[index]
        else:
            print('No city was entered')
            print('Enter 1 to update to', zip_data['major_city'])
            if input() == '1':
                entered_city = zip_data['major_city']
            else:
                print('Enter the city manually.')
                print('Suggestions:', city_list)
                entered_city = input()

    return entered_city


# Verifies State matches zip code
def state(address, zip_code):
    state_abbreviation = []
    for pair in address:
        if 'StateName' in pair:
            state_abbreviation.append(pair[0])
    # This will return the two character State code, e.g. 'NY'
    entered_state = re.sub(r'[^A-Z]', '', ' '.join(state_abbreviation))
    verify = SearchEngine().by_zipcode(zip_code[:5]).to_OrderedDict()
    zip_data = Series(verify)
    # This will be the full State name, e.g. 'New York'
    state_from_zip = zip_data['state']
    if lookup(entered_state) != lookup(state_from_zip):
        print('State does not match State in zip code database')
        print('State entered was:', entered_state)
        print('Enter 1 to update to', zip_data['state'])
        if input() == '1':
            entered_state = zip_data['state']

    return entered_state


# Defines zip code based on the parsed data.
def zip_code(address):
    zipcode = []
    for pair in address:
        if 'ZipCode' in pair:
            zipcode.append(pair[0])

    return ' '.join(zipcode)


# Verifies a valid US zip code or zip+4 format
def valid_zip(zip_code):
    if re.match(r'\d{5}$', zip_code):
        return True
    elif len(zip_code) == 10 and re.match(r'\d\d\d\d\d-\d\d\d\d', zip_code):
        return True

    return False


# Simplifies sales status for uniformity
def sales_status(status):
    if status[0].upper() == 'A':
        return 'Available'
    elif status[0].upper() == 'S':
        return 'Sold'
    elif status[0:3].upper() == 'UND' or status[0].upper() == 'C':
        return 'Under Contract'

    return 'Unknown'


# Searches for an address in the database based on the first few characters of a street address.
# Returns a Property object.
def search_streetaddress(term, database):
    possible_matches = []
    for property_listing in database:
        if property_listing.street_address.upper().startswith(term):
            possible_matches.append(property_listing)
    if len(possible_matches) == 1:
        print('Match found! \n', possible_matches[0])

        return possible_matches[0]

    if len(possible_matches) > 1:
        print('Multiple possibilities found. \n')
        match = []
        i = 0
        for match in possible_matches:
            print('Enter', i, 'to select', match, '\n')
            i += 1
        while True:
            selection = input('Enter your selection: ')
            if selection.isnumeric() and int(selection) < len(possible_matches):
                return match[i]

            print('Invalid selection.')
    print('No matches found')

    return possible_matches  # None
