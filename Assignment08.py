 #------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# PYChang,12.07.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'product.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        PYChang,12.07.2020,Modified code to complete assignment 8
    """
    # --Constructor-- #
    def __init__(self, name, price):
        # --Attributes-- #
        self.__product_name = name
        self.__product_price = price
    # --Properties-- #

    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, product_name_new):
        if not str(product_name_new).isnumeric():
            self.__product_name = product_name_new
        else:
            raise Exception("Name must be string")

    @property
    def product_price(self):
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, product_price_new):
        if not float(product_price_new).isinstance():
            self.__product_price = product_price_new
        else:
            raise Exception("Price must be numeric")

    def __str__(self):
        return self.__product_name + "," + str(self.__product_price)

 # Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        PYChang,12.07.2020,Modified code to complete assignment 8
    """
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        list_of_rows.clear()
        file = open("/Users/pchang/Documents/_PythonClass/Assignment08/product.txt", "r")
        for line in file:
            name, price = line.split(",")
            obj = Product(name, price)
            list_of_rows.append(obj)
        file.close()
        return list_of_rows

    @staticmethod
    def save_data_to_file(file_name, Product):
        file_name = open(file_name, "w")
        for objProd in Product:
            file_name.write(str(objProd) + "\n")
        file_name.close()

    @staticmethod
    def add_data_to_list(name, price, list_of_rows):
        obj = Product(name, price)
        list_of_rows.append(obj)
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    # TODO: Add docstring
    """input and output codes class"""
    # TODO: Add code to show menu to user
    @staticmethod
    def menu_options():
        print("""
        Menu of Options
        1) Show current data
        2) Add a product
        3) Save Data to File
        4) Exit Program
        """)
        print()

    @staticmethod
    def menu_choice():
        user_choice = str(input("Please select 1 to 4 from menu: "))
        print()
        return user_choice

    @staticmethod
    def show_current_data(Product):
        print("---------CURRENT DATA -----------")
        for row in Product:
            print(row)

    @staticmethod
    def input_new_product_and_price():
        thing = input("Enter the name of the product: ")
        dollar = float(input("Enter the price of the product: "))
        return thing, dollar
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

while True:

# Show user a menu of options
    IO.menu_options()
# Get user's menu option choice
    strChoice = IO.menu_choice()
# Show user current data in the list of product objects
    if strChoice == '1':
        (IO.show_current_data(lstOfProductObjects))
# Let user add data to the list of product objects
    if strChoice == '2':
        name, price = IO.input_new_product_and_price()
        FileProcessor.add_data_to_list(name, price, lstOfProductObjects)
# let user save current data to file and exit program
    if strChoice == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
    if strChoice == '4':
        print("You are done!")
        break
