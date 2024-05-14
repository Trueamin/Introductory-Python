import random 

Lower_bound = 1
Upper_bound = 999

Target_number = int(input(f"Enter your number between {Lower_bound} and {Upper_bound}: "))

Guess = random.randint(Lower_bound, Upper_bound)

while True:
    print(f"Computer is guess a namber: {Guess}")
    user_input = input('What is your answer(smaller/ larger/ correct): ').lower()

    if user_input == 'correct':
        print('Congratulations! computer is guess your number.')
        break
    elif user_input == 'smaller':
        Upper_bound = Guess - 1
    elif user_input == 'larger':
        Lower_bound = Guess + 1
    else:
        print("Please enter one of the answers 'smaller', 'larger' or 'correct'")
    Guess = random.randint(Lower_bound, Upper_bound)

