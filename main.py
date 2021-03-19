from replit import clear
from game_data import data
from art import logo, vs
from helper_functions import get_random_entry

def game():
    entry_a, index_a, follower_count_a = get_random_entry(data)
    entry_b, index_b, follower_count_b = get_random_entry(data)

    is_entry_unique = False
    while not is_entry_unique:
        if index_b != index_a:
            is_entry_unique = True
        else:
            entry_b, index_b, follower_count_b = get_random_entry(data)

    score = 0
    next_round = True
    while next_round:
        is_entry_unique = False
        while not is_entry_unique:
            if index_b != index_a:
                is_entry_unique = True
            else:
                entry_b, index_b, follower_count_b = get_random_entry(data, "B")

        clear()
        print(logo)
        if score > 0:
            print(f"You are right! Current score: {score}\n")

        print(f"Compare A: {entry_a}")
        print(vs)
        print(f"Against B: {entry_b}")

        answer = input("\nWho has more followers? Type a or b: ").lower()

        is_valid_answer = False
        while not is_valid_answer:
            if answer in 'ab' and len(answer) == 1:
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

            entry_a = answer_dict["b"]["entry"]
            index_a = answer_dict["b"]["index"]
            follower_count_a = answer_dict["b"]["followers"]

            entry_b, index_b, follower_count_b = get_random_entry(data)

        else:
            next_round = False
            clear()
            print(logo)
            print(f"Wrong! Final score was: {score}")

            play_again = input("\nPlay again? Type y: ").lower()

            if play_again == 'y':
                game()
            else:
                print("Ok, bye!")

game()


