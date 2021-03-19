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

# create a function that returns an f string with a random entry
def get_random_entry(data):
    max = len(data) - 1
    random_index = randint(0, max)
    return data[random_index]


entry = get_random_entry(data)
print(f"Compare A: {entry['name']}, a {entry['description']}, from {entry['country']}.")




