#functions go here

# check input is a number more than zero
def num_check (question):
    valid = False
    while not valid:

        error = "please enter a valid number"

        try:
            
            #ask user to enter a number
            response = float(input(question))
            
            # check number is more than zero
            if response > 0:
                return response
            
            #outputs error if input is invalid
            else:
                print("please enter a number that is more than zero")
                print() 

        except ValueError:
            print(error)

#main routine goes here

# introduction?heading prin statements
print()
print("**** area perimeter calculator****")
print()

# start of the calculator loop
keep_going = ""
while keep_going == "":

    width = num_check ("width: ")
    height = num_check("height: ")
    
    # calculate area (width x height)
    area = width * height
    perimeter = 2 * (width + height)

    #output area and perimeter to 2dp
    print("perimeter: {} units".format(perimeter))
    print("area: {} sqaure units".format(area))

    keep_going = input("press <enter> to keep going or any key to quit")

print()
print("thanks fo using the area/perimeter calculator")


    
