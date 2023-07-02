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

for item in range(0,6):
    how_much = num_check("How much does it cost? ", "Must be a number greater than 0 ...\n", float)
    print("You said '{}'\n".format(how_much))