def main():
    print("Hello! Welcome!")

    input_number_list = list()


    user_input_N = input("Please enter a positive integer for input N: \n")
    user_input_N = int(user_input_N)
    count = 0 

    print("You will provide " + str(user_input_N) + " numbers one by one, program displays the n-th number you are currently entering")

    while count < user_input_N:
        user_input = input("Enter the " + str(count+1) + " number: (only enter one number, press Enter after the number to enter next one)\n")
        input_number_list.append(int(user_input))
        count += 1

    print("You have finished entering " + str(user_input_N) + " numbers. ")

    user_input_check = input("Please enter a number X to check if it exists in previous numbers you entered and generate index: \n")


    if int(user_input_check) in input_number_list:
        indexes = [i for i, x in enumerate(input_number_list) if str(x) == user_input_check]
        print(' '.join(map(str, indexes)))
    else:
    	print("-1")

if __name__ == "__main__":
    main()