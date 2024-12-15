import random
#ans='y'
def color_game():
    colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"]
    score_board = []

    print("Hey cutie !")
    player_name = input("Can you tell me what is your name ? : ")
    print("-----------------------------Welcome",player_name,"to the color game----------------")
    ans=input("can we use this name in score board or you want to change it ?(y/n):")
    if ans=='n':
        player_name = input("Please enter your name for the score board: ")
    else:
        print("OKAY",player_name,"Let's Begin !")
    while True:
        print("\n1> Start game")
        print("2> Exit")
        choice = input("Enter your choice: ")

        if choice == "2":
            print("Thanks for playing!")
            break

        elif choice == "1":
            print("CHOOSE FROM THE GIVEN COLORS:",colors)
            machine_color = random.choice(colors)
            attempts = 0
            max_attempts = 5
            won = False

            while attempts < max_attempts:
                user_color = input("\nPlease enter the color: ").lower()

                if user_color not in colors:
                    print("Invalid color! Please choose from the following:")
                    print(", ".join(colors))
                    continue

                attempts += 1

                if user_color == machine_color:
                    print(f"\nCongratulations! You won the game in {attempts} attempts.")
                    won = True
                    break
                else:
                    print(f"Your guess was wrong. Please try again.")
                    print(f"Number of attempts left: {max_attempts - attempts}")

            if not won:
                print(f"\nGame over! The correct color was: {machine_color}")

            score_board.append({
                "name": player_name,
                "won": won
            })

            print("\n1> See score board")
            print("2> Play again")
            print("3> Exit")
            post_game_choice = input("Enter your choice: ")

            if post_game_choice == "1":
                games_won = sum(1 for game in score_board if game["won"])
                games_lost = len(score_board) - games_won
                print(f"\nScore Board:")
                print(f"Number of games won: {games_won}")
                print(f"Number of games lost: {games_lost}")
                print(f"Name of the player: {player_name}")

            elif post_game_choice == "2":
                continue

            elif post_game_choice == "3":
                print("Thanks for playing!")
                break

        else:
            print("Invalid choice. Please select 1 or 2.")
if __name__ == "__main__":
    color_game()
