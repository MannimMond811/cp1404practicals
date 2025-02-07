"""
Define the MENU options:
    (G) Get a valid score
    (P) Print result
    (S) Show stars
    (Q) Quit

Display the MENU

Define main function:
    Initialize valid_score as an empty string
    Prompt the user to choose an option and convert to uppercase

    While the choice is not "Q":
        If the choice is "G":
            Call validate_score function to get a valid score and store it in valid_score
        Else if the choice is "P":
            If valid_score is empty:
                Print "No score to determine"
            Else:
                Call print_result with valid_score and print the result
        Else if the choice is "S":
            If valid_score is empty:
                Print "No score to determine"
            Else:
                Print "*" repeated valid_score number of times
        Else:
            Print MENU and "Error choice"

        Prompt the user to choose again and convert to uppercase

    Print "Bye"

Define function validate_score:
    Prompt the user to input a score
    While the score is less than 0 or greater than 100:
        Prompt the user to input a new score
    Return the valid score

Define function print_result:
    If the score is less than 0 or greater than 100:
        Set result to "Invalid score"
    Else if the score is 90 or more:
        Set result to "Excellent"
    Else if the score is 50 or more:
        Set result to "Passable"
    Else:
        Set result to "Bad"
    Return the result

Call the main function

"""
MENU = "(G)et a valid score\n (P)rint result\n (S)how stars\n (Q)uit"
print(MENU)


def main():
    """main function"""
    valid_score = ""
    choice = input("Choose:").upper()
    while choice != "Q":
        if choice == "G":
            valid_score = validate_score()
        elif choice == "P":
            if valid_score == "":
                print("No score to determine")
            else:
                result = print_result(valid_score)
                print(result)
        elif choice == "S":
            if valid_score == "":
                print("No score to determine")
            else:
                print("*"*int(valid_score))
        else:
            print(MENU)
            print("Error choice")
        choice = input("Choose：").upper()
    print("Bye")


def validate_score():
    """validate user input"""
    score = float(input("Enter your score:"))
    while score < 0 or score > 100:
        score = float(input("Enter your score:"))
    return score

def print_result(score):
    """determine user inputted score and print result"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()