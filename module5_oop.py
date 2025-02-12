class NumberIndexSearch:
    def __init__(self):
        self.numbers = []

    def append_number(self, number):
        self.numbers.append(number)

    def search_for_index(self, x):
        if x in self.numbers: 
            return self.numbers.index(x)+1
        else:
            return -1

def main():
    nis_ex = NumberIndexSearch()
    
    user_input_N = int(input("Enter a positive number N for number of inputs: \n"))
    
    for _ in range(user_input_N):
        user_input_number = int(input("Enter one number at a time (press Enter to enter next number): \n"))
        nis_ex.append_number(user_input_number)
        
    user_input_X = int(input("Please enter a number X to check if it exists in previous numbers you entered and generate index:  \n"))
    index_output = nis_ex.search_for_index(user_input_X)
    
    print(index_output)

if __name__ == "__main__":
    main()