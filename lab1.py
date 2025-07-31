#Write your code here in python 

def calc_grade():
    # Prompt user to enter marks or type "EXIT" to quit
    x = input()

    # Check if the user wants to exit the program
    if x.upper() == "EXIT":
        return;  # Exit the function

    # Check if the input is not a number
    if not x.isdigit():
        print("Invalid input")  # Display error message
        return;

    # Convert the input string to an integer
    m = int(x)

    # Check if the number is out of the valid range (0-100)
    if m < 0 or m > 100:
        print("Invalid input")  # Display error message
    elif m >= 90:
        print("A")  # Grade A for marks 90-100
    elif m >= 75:
        print("B")  # Grade B for marks 75-89
    elif m >= 60:
        print("C")  # Grade C for marks 60-74
    elif m >= 40:
        print("D")  # Grade D for marks 40-59
    else:
        print("F")  # Grade F for marks below 40

if __name__ == "__main__":
  calc_grade()
