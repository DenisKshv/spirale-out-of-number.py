import time # We want to feel like talking to AI from an old film. So we will need the delays :)

# lets defy a function that we will use later to check if we can address a certain index in the matrix 
def index_in_matrix (a_lengtht_of_one_side, x_index, y_index,):
    if x_index >= a_lengtht_of_one_side:
        return False
    elif y_index >= a_lengtht_of_one_side:
        return False
    else:
        return True

# All of the program is going to loop infinitely, which can allow us to give the user choise to input something else
while True:

    # Firstly let's get the number from user and call it 'number_from_user'
    # But we need to restrict user to only inputing an positive integer, and not zero of course. We will give sme answers to user tht lead him into inputing what we want
    while True:
        try:
            time.sleep(1)
            number_from_user = int(input("Please enter any positive integer:"))
            if number_from_user == 0:
                time.sleep(1)
                print("Zero is too boring.")
                time.sleep(1)
                print("I only accept integers more then zero.")
            elif number_from_user < 0:
                time.sleep(1)
                print ("I said a POSITIVE integer.")
            else:
                break
        except ValueError:
            time.sleep(1)
            print("I asked for an INTEGER.")

    # Then let's get the square of the number_from_user, and call it 'number_from_user_squared' 
    number_from_user_squared = number_from_user ** 2

    # Let's create an array
    Spiral = []

    # Now let's create our 2D matrix by adding empty arrays into 'Spiral'array
    # We will fill it later
    for i in range(number_from_user):
        Spiral.append([])

    # Let's create a counter that will be used to fill the matrix
    matrix_filling_counter = number_from_user_squared

    # Now lets fill in the top layer of the matrix with the begining of spiral
    for i in range(number_from_user):
        Spiral[0].append(matrix_filling_counter)
        matrix_filling_counter -= 1

    # And then fill in the rest of matrix with zero's (we will need that later)
    for x in range(number_from_user - 1):
        for y in range(number_from_user):
            Spiral[x + 1].append(0)

    # This is where filling of the rest of matrix starts ################################################################
    x_position = number_from_user - 1 # 'x_position' & 'y_position' are going to help us accurately address the right indexes    
    y_position = 0 
    n = number_from_user # 'n' will help us count the length of each 'straight line' in the matrix 
    while matrix_filling_counter != 0:
        ################################################################ \/ This section is responcible for filling in the numbers in a 'up to down' direction
        n -= 1
        for i in range(n):
            if not(index_in_matrix(number_from_user, x_position, y_position + 1)):
                break
            elif Spiral[y_position + 1][x_position] != 0:
                break
            else:
                y_position += 1 
                Spiral[y_position][x_position] = matrix_filling_counter
                matrix_filling_counter -= 1
        ################################################################ \/ This one is for 'right to left' direction
        for i in range(n):
            if not(index_in_matrix(number_from_user, x_position - 1, y_position)):
                break
            elif Spiral[y_position][x_position - 1] != 0:
                break
            else:
                x_position -= 1
                Spiral[y_position][x_position] = matrix_filling_counter
                matrix_filling_counter -= 1
        ################################################################ \/ This one is for 'upward' direction
        n -= 1
        for i in range(n):
            if not(index_in_matrix(number_from_user, x_position, y_position - 1)):
                break
            elif Spiral[y_position - 1][x_position] != 0:
                break
            else:
                y_position -= 1 
                Spiral[y_position][x_position] = matrix_filling_counter
                matrix_filling_counter -= 1
        ################################################################ \/ And finnaly 'left to right' direction
        for i in range(n):
            if not(index_in_matrix(number_from_user, x_position + 1, y_position)):
                break
            elif Spiral[y_position][x_position + 1] != 0:
                break
            else:
                x_position += 1
                Spiral[y_position][x_position] = matrix_filling_counter
                matrix_filling_counter -= 1
    # This is where filling of the rest of matrix ends ################################################################

    # Print of the final result
    time.sleep(1)
    for i in range(number_from_user):
        print(Spiral[i])
    # Now let's give the user choise of inputing something else
    # We will use somewhat-same while True loop we used for getting a number from user 
    while True:
        try:
            time.sleep(1)
            print("Do you want to try input something different? Answer 'yes' or 'no'.", end='\n')
            time.sleep(1)
            users_answer = str(input("Your answer:"))
            if users_answer == "no":
                time.sleep(1)
                print("In that case, goodbye!")
                time.sleep(1)
                exit()
            elif users_answer == "yes":
                time.sleep(1)
                print("Ok, we'll start again!")
                break
            else:
                time.sleep(1)
                print("I only accept eather 'yes' or 'no'.")
        except ValueError:
            time.sleep(1)
            print("I only accept eather 'yes' or 'no'.")