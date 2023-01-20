# initialization of variables
# names of columns in table
header = ["Country", "Code", "Product", "Cost", "Quantity"]
# the width of columns stored ["Country", "Code", "Product", "Cost", "Quantity"]
width_of_column = [15, 10, 25, 8, 8]
# width of column for stored number
width_for_number = 4
# width of column stored multliplication of cost and quantity 
width_for_sum = 10

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_country(self):
        return self.country

    def get_code(self):
        return self.code

    def get_product(self):
        return self.product

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):#
        str_shoe = ""
        str_shoe += self.country +"," + str(self.code) +","+ self.product +","+ str(self.cost) +","+ str(self.quantity)
        return str_shoe

    # function similira to __str__ but can be use for get class as string for manipulation
    def get_class_as_str(self):
        str_shoe = ""
        str_shoe += self.country +"," + str(self.code) +","+ self.product +","+ str(self.cost) +","+ str(self.quantity) 
        return str_shoe

    def get_class_as_list(self):
        return [self.country, self.code, self.product, self.cost, self.quantity ]

    def set_quantity(self, num):
        self.quantity = num


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
  '''
# variable using to determinate first line of file
counter = 0  
try:
    file = open("inventory.txt", "r")
    for line in file:
        # skipping the first line of the file
        if counter > 0:
            str_stock = line
            list_stock = str_stock.split(",")
            # delete "\n" from a end of list_stock[4] by cast to int
            list_stock[4] = int(list_stock[4])
            # create a shoe object and add it to the shoe_list
            shoe_list.append(Shoe(list_stock[0], list_stock[1], list_stock[2], list_stock[3], list_stock[4]))

        counter += 1    # increase counter for going to next line
except FileNotFoundError:
    print("Can't open data base.")
    print("Contact your system administrator to repair the \"inventory.txt\" file.")
    temp_str = input("If you want to start with an empty data base enter \"start\": ").upper()
    if temp_str == "START":
        pass
    else:
        print("Closing the program.")
        exit()

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    choose = input("Add new shoe to the data base.\nFor continue press C-key and enter,\nto abort press any key and enter. ").capitalize()
    if choose == "C":
        print("Add new shoe:")
        country = input("Country: ")
        code = input("Code of shoe: ")
        product = input("Model name of shoe: ")
        cost = input("Cost of one pair: ")
        quantity = input("Quantity: ")

        shoe_list.append(Shoe(country, code, product, cost, quantity))

# printing the frame as a line, the length is taken from the list argument, end of line is True when will be created next column for multliplication of cost and quantity
def print_frame(list, end_of_line):
    sum = 0
    for item in list:
        sum += item
    if end_of_line == True:
        print("+"+(sum+8) * "-"+"+", end="")
    else:
        print("+"+(sum+8) * "-"+"+")

# printing frame for field stored number,
def print_frame_for_number(list):
    print("+" + list * "-", end="")

# printing line and fill it with data from some_list variable,  some_list - it can be Shoe class or list
def print_row(some_list, end_of_line):
    # width of stored
    # cecking argument some_list is list
    # end_of_line is true for end=""
    if isinstance(some_list, list):
        if end_of_line == True:
            print("|"+some_list[0]+(width_of_column[0] - len(some_list[0])) * " ", "|"+some_list[1]+(width_of_column[1] - len(some_list[1])) * " ", "|"+some_list[2]+(width_of_column[2] - len(some_list[2])) * " ", "|"+some_list[3]+(width_of_column[3] - len(some_list[3])) * " ", "|"+str(some_list[4])+(width_of_column[4] - len(str(some_list[4]))) * " "+"|", end="")
        else:
            print("|"+some_list[0]+(width_of_column[0] - len(some_list[0])) * " ", "|"+some_list[1]+(width_of_column[1] - len(some_list[1])) * " ", "|"+some_list[2]+(width_of_column[2] - len(some_list[2])) * " ", "|"+some_list[3]+(width_of_column[3] - len(some_list[3])) * " ", "|"+str(some_list[4])+(width_of_column[4] - len(str(some_list[4]))) * " "+"|")
    elif isinstance(some_list, Shoe):
        # cast Shoe.some_list in some_list
        some_list = some_list.get_class_as_list()
        if end_of_line == True:
            print("|"+some_list[0]+(width_of_column[0] - len(some_list[0])) * " ", "|"+some_list[1]+(width_of_column[1] - len(some_list[1])) * " ", "|"+some_list[2]+(width_of_column[2] - len(some_list[2])) * " ", "|"+some_list[3]+(width_of_column[3] - len(some_list[3])) * " ", "|"+str(some_list[4])+(width_of_column[4] - len(str(some_list[4]))) * " "+"|", end="")
        else:
            print("|"+some_list[0]+(width_of_column[0] - len(some_list[0])) * " ", "|"+some_list[1]+(width_of_column[1] - len(some_list[1])) * " ", "|"+some_list[2]+(width_of_column[2] - len(some_list[2])) * " ", "|"+some_list[3]+(width_of_column[3] - len(some_list[3])) * " ", "|"+str(some_list[4])+(width_of_column[4] - len(str(some_list[4]))) * " "+"|")

# printing field with number
def print_number(num):
    print("|"+str(num)+(width_for_number - len(str(num))) * " ",end="")

def print_frame_for_sum(width):
    print( (width - 1) * "-" + "+")    

def print_frame_for_row(width):
    print( width * "-"  )

def print_sum(width):
    print("Sum" + (width-4) * " " + "|")

def print_cost_and_quantity(width, item):
    sum = int(item.get_quantity()) * int(item.get_cost())
    print(str(sum) + (width-1 -len(str(sum))) * " " + "|")

def view_all(): 
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    ''' 
    # create data base based on shoe _list with header
    # data base is presented in cool table with frames
    number =1
    print_frame_for_number(width_for_number)
    print_frame(width_of_column, False)
    print("|No"+" " * (width_for_number - 2), end="")
    print_row(header, False)
    for item in shoe_list:
        print_frame_for_number(width_for_number)
        print_frame(width_of_column, False)
        print_number(number)
        number += 1
        print_row(item.get_class_as_list(), False)
    print_frame_for_number(width_for_number)
    print_frame(width_of_column, False)

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    min = None
    for item in shoe_list:
        temp = int(item.get_quantity())
        if min == None:
            min = temp
        if min > temp:
            min = temp

    # print("Minimum: ",min)
    # print all shoes with quanity = min
    num = 1
    num_list = 0
    edit_list = []
    for item in shoe_list:

        if item.get_quantity() == min:
            edit_list.append([num, num_list, item])
            print_frame_for_number(width_for_number)
            print_frame(width_of_column, False)
            print_number(num)
            num += 1
            print_row(item, False)
        num_list += 1   # increase this variable to save number of item in list called shoe_list
    print_frame_for_number(width_for_number)
    print_frame(width_of_column, False)
    
    job = True
    while job:
        if (num - 1) > 1:
            print("There is/are",num - 1, "items to restock.")
            edit_number = input("Enter the number of position to restock.\nPress enter if you finish.")
        elif (num - 1) == 1:
            print("There is 1 item to restock.")
            edit_number = 1

        if  num != 1:
            if edit_number == "":
                job = False
            else: 
                # editing stock
                try:
                    edit_number = int(edit_number)
                    if edit_number in range(1, len(edit_list) + 1):
                        for item in edit_list:
                            if item[0] == edit_number:
                                item[2] = restock(item[2])
                                job = False
                    else:
                        print("Something's wrong. This value shoud be between 1 and ",len(edit_list),".")
                except ValueError:
                    print("Something's wrong, enter the integer value.\nThis value shoud be between 1 and ",len(edit_list),".")
        else:
            print("Data base is empty.")
            job = False
            
                
def restock(shoe):
    while True:
        print("Current stock: ", shoe.get_quantity())
        try:
            new_quantity = int(input("Restock: "))
            shoe.set_quantity(shoe.get_quantity()+new_quantity)
            return shoe
            break
        except ValueError:
            print("Something's wrong, try enter integer number.")

def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    print("Searching shoe model by shoe code.")
    if len(shoe_list) == 0:
        print("Data base is empty.")
    else:
        while True:
            print("Press enter to exit from search tool.")
            code = input("Enter shoe code: ").upper()
            if code == "":
                break
            search = False
            
            for item in shoe_list:
                if code == item.get_code():
                    search = True
                    print_frame(width_of_column, False)
                    print_row(item.get_class_as_list(), False)
                    print_frame(width_of_column, False)
            if search == False:
                print("There are no such shoes in stock with shoe code:",code,".")

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    print("Total value for each item:")
    if len(shoe_list) == 0:
        print("Database is empty.\n")
    else:
        # top frame
        print_frame_for_number(width_for_number)
        print_frame(width_of_column, True)
        print_frame_for_sum(width_for_sum)

        # header
        print("|No"+" " * (width_for_number - 2), end="")
        print_row(header, True)
        print_sum(width_for_sum)

        # frame filled by shoes
        number = 1
        for item in shoe_list:
            # print top frame
            print_frame_for_number(width_for_number)
            print_frame(width_of_column, True)
            print_frame_for_sum(width_for_sum)

            #filling pools
            print_number(number)
            number += 1
            print_row(item.get_class_as_list(), True)
            print_cost_and_quantity(width_for_sum, item)

        # print last botom frame
        print_frame_for_number(width_for_number)
        print_frame(width_of_column, True)
        print_frame_for_sum(width_for_sum)

def highest_qty():
    max = None
    for item in shoe_list:
        if max == None:
            max = item.get_quantity()
        if max < item.get_quantity():
            max = item.get_quantity()

    if  max != None:
        # print all shoes with quanity = min
        num = 1
        num_list = 0
        edit_list = []
        print("Sale of products")
        for item in shoe_list:

            if item.get_quantity() == max:
                edit_list.append([num, num_list, item])
                print_frame_for_number(width_for_number)
                print_frame(width_of_column, False)
                print_number(num)
                num += 1
                print_row(item, False)
            num_list += 1   # increase this variable to save number of item in list called shoe_list
        print_frame_for_number(width_for_number)
        print_frame(width_of_column, False)

def write_shoes_data():
    file = open("inventory.txt", "w")
    file.writelines("Country,Code,Product,Cost,Quantity\n")
    for item in shoe_list:

        file.write(item.get_class_as_str()+"\n")
    file.close()
            
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:
    print("Choose operation:")
    print("1 - view all,\n2 - add new shoe,\n3 - restock,\n4 - search shoes,\n5 - print value of all products,\n6 - Start selling products in stock,\n10 - end the program")
    action = input()
    read_shoes_data()
    
    if action == "1":
        view_all()
        write_shoes_data()
    elif action == "2":
        capture_shoes()
        write_shoes_data()

    elif action == "3":
        re_stock()
        write_shoes_data()

    elif action == "4":
        seach_shoe()
        write_shoes_data()

    elif action == "5":
        value_per_item()
        write_shoes_data()
    
    elif action == "6":
        highest_qty()
        write_shoes_data()

    elif action == "10":
        print("End the program.")
        write_shoes_data()

        exit()
    else:
        print("Something's wrong. Try again.")
