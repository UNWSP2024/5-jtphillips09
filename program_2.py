# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

import random

def check_answer(num1, num2, user_answer):
    """Check if the user's answer is correct and display a message."""
    correct_answer = num1 + num2
    if user_answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

if __name__ == '__main__':
    # Generate two random numbers between 100 and 999
    number1 = random.randint(100, 999)
    number2 = random.randint(100, 999)

    # Display the quiz
    print(f"  {number1}")
    print(f"+ {number2}")
    print("------")

    # Get user's answer
    user_input = int(input("Enter your answer: "))

    # Check the answer using the function
    check_answer(number1, number2, user_input)
