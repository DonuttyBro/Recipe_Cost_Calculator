# Import Libraries
import pandas


# functions go here

# shows instructions
def show_instructions():
    print('''\n
    ***** Instructions *****

    Enter the recipe name

    Enter the amount of serves

    For each ingredient, enter ...
    - The ingredient name
    - What it's measured in
    - The amount needed
    - The amount bought
    - The price
    
    When you have entered all the ingredients, type 'no' to quit.
    
    The program will then display the recipe details
    including the ingredient amounts and costs.
    
    This information will also be automatically written to
    a text file. The recipe name will be the text file name.

    ************************''')


# Checks that input is either a float or an integer greater than 0.
# Takes in custom error message.
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Checks that user has entered yes / no to a question
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no ...\n")


# Checks that string response is not blank
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Get what unit they're measuring in
def units(question, error):

    measurement_list = ["g", "kg", "ml", "l"]

    valid = False
    while not valid:
        
        response = input(question).lower()

        
        if response in measurement_list:
          return response
        else:
            print(error)


# Main Routine Starts Here...
# ask user if they want to see instructions
want_instructions = yes_no("Do you want to read the instructions (y/n)? ")

if want_instructions == "yes":
    show_instructions()

# Get recipe name
recipe_name = not_blank("\nRecipe Name: ", "\nThe recipe name cannot be blank")

# How many serves
serve_amount = num_check("\nHow many serves are you making: ", "\nMust be a number greater than 0.", float)

more_ingredients = "yes"

ingredient_names = []
ingredient_amounts_needed = []
ingredient_amounts_bought = []
bought_prices = []
fixed_bought_prices = []
ingredient_serve_prices = []
fixed_ingredient_serve_prices = []
overall_prices = []
fixed_overall_prices = []

while more_ingredients == "yes":
    
    # Get ingredient name
    ingredient_name = not_blank("\nIngredient Name: ", "\nThe ingredient name cannot be blank")

    # Asks if the ingredient has measurements
    any_measurement = yes_no("\nDoes this ingredient need measurements? ")

    if any_measurement == "yes":

        # Get measurement type
        needed_measurement_type = units("\nWhat are you measuring the needed amount in (kg, g, l, ml): ", "\nMust be kg, g, l, or ml.")

        # Get amount needed
        amount_needed = num_check("\nHow much will you need: ", "\nMust be a number greater than 0.", float)
        
        # converts kg and l so they can be in equations with g and ml
        if needed_measurement_type == "kg" or needed_measurement_type == "l":
            needed_how_much = amount_needed * 1000
        else:
            needed_how_much = amount_needed 

        # Bought measurement type
        bought_measurement_type = units("\nWhat are you measuring the bought amount in (kg, g, l, ml): ", "\nMust be kg, g, l, or ml.")

        # Get amount bought
        amount_bought = num_check("\nHow much are you buying: ", "\nMust be a number greater than 0.", float)

        # converts kg and l so they can be in equations with g and ml
        if bought_measurement_type == "kg" or bought_measurement_type == "l":
            bought_how_much = amount_bought * 1000
        else:
            bought_how_much = amount_bought

        # Gets the price of the amount bought
        price = num_check("\nHow much does it cost: ", "\nMust be a number greater than 0", float)
        fixed_price = currency(price)

    elif any_measurement == "no":
        
        # Sets measurement type to none
        needed_measurement_type = ""
        bought_measurement_type = ""

        # Get amount needed
        amount_needed = num_check("\nHow many will you need: ", "\nMust be a number greater than 0.", float)
        needed_how_much = amount_needed
        # Get amount bought
        amount_bought = num_check("\nHow many are you buying: ", "\nMust be a whole  number greater than 0.", int)
        bought_how_much = amount_bought

        # Gets the price of the amount bought
        price = num_check("\nHow much does it cost: ", "\nMust be a number greater than 0", float)
        fixed_price = currency(price)

    # add measurement to amount
    needed_measurement = "{}{}".format(amount_needed, needed_measurement_type)
    bought_measurement = "{}{}".format(amount_bought, bought_measurement_type)

    # Calculates overall costs
    overall_needed_bought = bought_how_much / needed_how_much
    price_overall = price / overall_needed_bought
    fixed_price_overall = currency(price_overall)
    fixed_serve = needed_how_much / serve_amount
    needed_bought = bought_how_much / fixed_serve
    price_serve = price / needed_bought
    fixed_price_serve = currency(price_serve)

    # Adds items to lists
    ingredient_names.append(ingredient_name)
    ingredient_amounts_needed.append(needed_measurement)
    ingredient_amounts_bought.append(bought_measurement)
    bought_prices.append(price)
    fixed_bought_prices.append(fixed_price)
    ingredient_serve_prices.append(price_serve)
    fixed_ingredient_serve_prices.append(fixed_price_serve)
    overall_prices.append(price_overall)
    fixed_overall_prices.append(fixed_price_overall)

    print("\nIngredient Price per serve = {}".format(fixed_price_serve))

    more_ingredients = yes_no("\nAre there any more ingredients: ")

# adds together numbers in lists for totals
bought_overall = sum(bought_prices)
fixed_bought_overall = currency(bought_overall)
overall_serve = sum(ingredient_serve_prices)
fixed_overall_serve = currency(overall_serve)
overall_all = sum(overall_prices)
fixed_overall_all = currency(overall_all)

# puts items in dictionaries
ingredient_dict = {
    "Ingredient Name": ingredient_names,
    "Amount": ingredient_amounts_needed
}
bought_dict = {
    "Ingredient Name": ingredient_names,
    "Amount": ingredient_amounts_bought,
    "Price": fixed_bought_prices
}
price_dict = {
    "Ingredient Name": ingredient_names,
    "Ingredient Serve Price": fixed_ingredient_serve_prices,
    "Ingredient Overall Price": fixed_overall_prices
}

# converts the dictionaries to data frames
ingredient_frame = pandas.DataFrame(ingredient_dict)
bought_frame = pandas.DataFrame(bought_dict)
price_frame = pandas.DataFrame(price_dict)

ingredient_txt = pandas.DataFrame.to_string(ingredient_frame)
bought_txt = pandas.DataFrame.to_string(bought_frame)
price_txt = pandas.DataFrame.to_string(price_frame)

# Sets up the titles in nicer formatting
display_recipe_name = "**** {} ****".format(recipe_name)
display_serve_amount = "Serves: {}".format(serve_amount)
display_ingredient_list = "**** Ingredient Amounts ****"
display_bought_list = "**** Bought Amounts ****"
display_price_list = "**** Ingredient Price Per Serve ****"
display_bought_price_overall = "Overall Bought Price: {}".format(fixed_bought_overall)
display_overall_serve_price = "Overall Serve Price: {}".format(fixed_overall_serve)
display_overall_price = "Overall Price: {}".format(fixed_overall_all)

# Puts all the items in a list
to_write = [display_recipe_name, display_serve_amount,display_ingredient_list ,ingredient_txt,display_bought_list , bought_txt, display_bought_price_overall,
            display_price_list ,price_txt, display_overall_serve_price, display_overall_price]

# Asks if you want to write to file
want_file = yes_no("\nDo you want to print this information to a file? ")

if want_file == "yes":
    # Write to file...
    # create file to hold data (add .txt extension)
    file_name = "{}.txt".format(recipe_name)
    text_file = open(file_name, "w+")

    # heading
    for item in to_write:
        text_file.write(item)
        text_file.write("\n\n")

    # close file
    text_file.close()

# prints the same items that are in the file
print()
for item in to_write:
    print(item)
    print()
