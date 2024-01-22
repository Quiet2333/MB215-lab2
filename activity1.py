name = input("what is your name?")# Ask for the user's name 
age = input("what is your age?")# Ask for the user's age
age = int(age)
import datetime
current_year= datetime.datetime.now().year# Get the current year
birth_year=current_year - age# Calculate the birth year
print(f"Hello {name}, you were born in the year {birth_year}.")# Print the greeting and birth year