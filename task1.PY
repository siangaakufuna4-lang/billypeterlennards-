from datetime import date
name = input("What is your name?: ")
birth_year = int(input("What year were you born?: "))


current_year = date.today().year
age = current_year - birth_year

print(f" {name}, you are {age} years old.")
