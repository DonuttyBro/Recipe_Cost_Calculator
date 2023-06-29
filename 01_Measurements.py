# Measurements by category
def measurement_checker (question, error):

    grams_list = ["kg", "g"]
    litre_list = ["l", "ml"]

    valid = False
    while not valid:

        response = input(question).lower()

        if response in grams_list:
            print("You are measuring in kilograms and grams.")
            return response
        elif response in litre_list:
            print("You are measuring in litres and millilitres.")
            return response
        else:
            print(error)


# Measurements in general
def units(question, error):

    measurement_list = ["g", "kg", "ml", "l"]

    valid = False
    while not valid:
        
        response = input(question).lower()

        
        if response in measurement_list:
          return response
        else:
            print(error)


measurement_used = measurement_checker("What units are you measuring in? ", "Please enter kg, g, l or ml ...\n")
alt_measurement_used = units("What units are you measuring in? ", "Please enter kg, g, l or ml ...\n")

print(measurement_used)
print(alt_measurement_used)


