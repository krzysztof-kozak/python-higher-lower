from random import randint


def get_random_entry(data):
    max = len(data) - 1
    index = randint(0, max)

    entry = data[index]
    follower_count = entry["follower_count"]
    return f"{entry['name']}, a {entry['description']}, from {entry['country']}.", index, follower_count
