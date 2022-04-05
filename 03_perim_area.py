def num_check (question):
    valid = False
    while not valid:

        error = ("please enter a number that is more than zero")

        try:

            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)
                print() 

        except ValueError:
            print(error)
    


width = num_check ("width: ")
height = num_check("height")
area = width * height
perimeter = 2 * (width + height)
print("perimeter: {} units".format(perimeter))
print("area: {} sqaure units".format(area))
