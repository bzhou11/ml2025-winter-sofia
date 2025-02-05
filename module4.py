def main():
    print("Hello! Welcome!")

    stop_enter_number = False
    input_number_list = list()

    while stop_enter_number == False:
    	user_input = input("Please enter a number N one by one, press Enter after the number N to enter next one (Enter 'E' to stop entering and proceed with next step)\n")

    	if user_input == "E": 
    		stop_enter_number = True
    	else:
    		input_number_list.append(int(user_input))

    user_input_check = input("Please enter a number X to check if it exists in previous numbers you entered and generate index: \n")

    if int(user_input_check) in input_number_list:
        indexes = [i for i, x in enumerate(input_number_list) if str(x) == user_input_check]
        print(' '.join(map(str, indexes)))
    else:
    	print("-1")

if __name__ == "__main__":
    main()