"""
CP1404/CP5632 - Practical
Broken program to determine score status
Define main function:
    Generate a random score between 0 and 100
    Call determine_score function with the generated score and store the result
    Display the result with a message: "Your result is <result>"

Define function determine_score(score):
    If score is less than 0 or greater than 100:
        Set result to "Invalid score"
    Else if score is greater than 90:
        Set result to "Excellent"
    Else if score is greater than 50:
        Set result to "Passable"
    Else:
        Set result to "Bad"
    Return the result

Call the main function

"""
import random


def main():
    """main function"""
    score = random.randint(0, 100)
    result = determine_score(score)
    print(f"Your result is {result}")


def determine_score(score):
    """determine what level the inputted score is"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
