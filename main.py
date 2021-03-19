from replit import clear
from random import randint
from game_data import data
from art import logo, vs


def get_random_entry(data, label):
    max = len(data) - 1
    index = randint(0, max)

    entry = data[index]
    follower_count = entry["follower_count"]
    return f"{label}: {entry['name']}, a {entry['description']}, from {entry['country']}.", index, follower_count


entry_a, index_a, follower_count_a = get_random_entry(data, "A")
entry_b, index_b, follower_count_b = get_random_entry(data, "B")


is_unique = False
while not is_unique:
    if index_b != index_a:
        is_unique = True
    else:
        entry_b, index_b, follower_count_b = get_random_entry(data, "B")

score = 0
next_round = True
while next_round:
    clear()
    print(logo)
    if score > 0:
        print(f"You are right! Current score: {score}\n")

    print(f"Compare {entry_a} {follower_count_a}")
    print(vs)
    print(f"Against {entry_b} {follower_count_b}")


    answer = input("\nWho has more followers? Type a or b: ").lower()

    is_valid_answer = False
    while not is_valid_answer:
        if answer in 'ab':
            is_valid_answer = True
        else:
            print("\nI can only accept 'a' or 'b' as an answer, sorry! :P")
            answer = input("Your answer: ").lower()

    answer_dict = {
        "a": {
            "entry": entry_a,
            "followers": follower_count_a,
            "index": index_a,
        },
        "b": {
            "entry": entry_b,
            "followers": follower_count_b,
            "index": index_b,
        },
    }

    if answer == "a":
        comparison = "b"
    else:
        comparison = "a"



    player_guess = answer_dict[answer]["followers"]
    other_option = answer_dict[comparison]["followers"]

    if player_guess > other_option:
        print("Correct! Score +1")
        score += 1

        entry_a = answer_dict[answer]["entry"]
        index_a = answer_dict[answer]["index"]
        follower_count_a = answer_dict[answer]["followers"]
        
        entry_b, index_b, follower_count_b = get_random_entry(data, "B")

    else:
        next_round = False
        print(f"Wrong! Final score was: {score}")










