# create an f string template using game_data
# {
#     'name': 'Cristiano Ronaldo',
#     'follower_count': 215,
#     'description': 'Footballer',
#     'country': 'Portugal'
# }
# f"Compare A: {name}, a {description}, from {country}."

from game_data import data
from random import randint
from art import logo, vs


# create a function that returns an f string with a random entry
def get_random_entry(data):
    max = len(data) - 1
    index = randint(0, max)

    entry = data[index]
    return f"Compare A: {entry['name']}, a {entry['description']}, from {entry['country']}.", index


# print two random entries to compare
# make sure they are unique

entry_a, currentIndex = get_random_entry(data)
entry_b, newIndex = get_random_entry(data)

is_unique = False
while not is_unique:
    if newIndex != currentIndex:
        is_unique = True
    else:
        entry_b, newIndex = get_random_entry(data)

# Starting state
# print the first screen: LOGO, entry_a VS entry_b

print(logo)

print(entry_a)
print(vs)
print(entry_b)

# Print the question prompt and save the answer
# validate input

answer = input("Who has more followers? Type a or b: ").lower()

is_valid_answer = False
while not is_valid_answer:
    if answer in 'ab':
        is_valid_answer = True
    else:
        print("I can only accept 'a' or 'b' as an answer, sorry! :P\n")
        answer = input("Your answer: ").lower()
