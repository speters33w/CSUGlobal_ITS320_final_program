# PropertyMinder

This program was written in Python 3.6.

It is the final project for CSU Global ITS320. The project was designed for Java, this is a Python version of the following:

**Final program**:

- Create a home inventory class that will be used by a National  Builder to maintain inventory of available houses in the country. The  following attributes should be present in your home class:
- private int squarefeet
- private string address
- private string city
- private string state
- private int zipcode
- private string Modelname
- private string salestatus (sold, available, under contract)

Your program should have appropriate methods such as:

- constructor
- add a new home
- remove a home
- update home attributes
- At the end of your program, be sure that it allows the user to output all home inventory to a text file.
- Be sure that your final program includes your source code and  screenshots of the application, executing the application, and the  results.

**This program uses third party dependencies which much be downloaded and imported**, and should be run in a virtual environment.

The dependencies can be imported via an IDE or pip install. See details at PyPl.org.

These dependencies are:

pandas
https://pypi.org/project/pandas/
https://pandas.pydata.org/

us 
https://pypi.org/project/us/
https://github.com/unitedstates/python-us

usaddress
https://pypi.org/project/usaddress/
https://github.com/datamade/usaddress

uszipcode
https://pypi.org/project/uszipcode/
https://github.com/MacHu-GWU/uszipcode-project



The program will ask for a CSV file with the following header:

```
Street Address,City,State,Zip,Square Feet,Property Type,Sales Status
```

It validates the city and State against an active US zip code database, and allows overriding in case of database errors.

Everything in the instructions is accomplished through command console, save it uses a GUI file dialog to open and save the database.

**To run the program, run main.py**

Stephan Peters

stephan.peters@csuglobal.edu, speters33w@gmail.com

