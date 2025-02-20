# importing TWL module that contains a list of words that are valid in Scrabble
import twl

# List of letters and their corresponding points in Scrabble
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", \
"v", "w", "x", "y", "z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Dictionary with the letters and their corresponding points
letter_to_points = {key:value for key, value in zip(letters, points)}

# Add a key-value pair to the dictionary for blank tiles
letter_to_points[" "] = 0


# Function to calculate the points of a word
def score_word(word_details):
    point_total = 0
    for letter in word_details[0]:
        if letter in word_details[1]:
            point_total += 2 * letter_to_points.get(letter, 0)
        elif letter in word_details[2]:
            point_total += 3 * letter_to_points.get(letter, 0)
        else:
            point_total += letter_to_points.get(letter, 0)
    if word_details[3] == "Y":
        return point_total * 2
    elif word_details[4] == "Y":
        return point_total * 3
    else:
        return point_total

# Testing score_word function
# word_details = ["BROWNIE", ["N"], [], "N", "Y"]
# brownie_points = score_word(word_details)
# print(brownie_points)


# Dictionary with the players and their words
player_to_words = {}

# Dictionary with the players and their points
player_to_points = {}

# Calculating the points of each player and storing them in player_to_points
def update_point_totals():
    for player, word_detail in player_to_words.items():
        player_points = 0
        for word in word_detail:
            player_points += score_word(word)
        player_to_points[player] = player_points
    return player_to_points

# Function to add a word to a player's list of words and update their points
def play_word(player, word_details):
    player_to_words[player].append(word_details)
    return update_point_totals()

# Testing play_word function
# print(play_word("player1", "code"))


# Adding players to the game
# Adding the first player
player = input("Player 1, please enter your player name: ")
player_to_words[player] = []

# Adding more players
more_players = "Y"
n = 2
while more_players == "Y":
    player = input(f"Player {n}, please enter your player name: ")
    while player in player_to_words.keys():
        player = input("This player name is already taken. Please enter a different name. ")
    player_to_words[player] = []
    more_players = input("Do you want to add more players? (Y/N) ").upper()
    while more_players not in ["Y", "N"]:
        more_players = input("Invalid input. Please enter 'Y' or 'N'. ").upper()
    n += 1

# Welcome message
print("Welcome to the Scrabble game! The players are: ")
for player in player_to_words.keys():
    print(player)


# Gameplay
game_on = True
while game_on:
    for player in player_to_words.keys():
        print(f"\nIt's {player}'s turn.")

        # Initialising list containing word_details to be used in play_word function
        word_details = []

        # Getting word played
        word = (input("\nPlease enter the word you played: ").lower())
        # Checking if word is valid
        while twl.check(word) == False:
            word = (input("\nInvalid word. Please enter a valid word: ").lower())
        word_details.append(word)

        # Getting letters that receive double letter points
        word_details.append(list(input("\nPlease enter the letters you received a double letter score for.\nIf you received a double letter \
score for multiple letters, there is no need to separate them. Eg. 'AB'.\nIf you didn't receive a double letter score press enter. \n").lower()))
        # Checking if letters are in word
        while any(letter not in word for letter in word_details[1]):
            word_details[1] = (list(input("\nInvalid input. Please enter the letters from the word you played that recieved a double letter score. \
\nIf you received a double letter score for multiple letters, there is no need to separate them. Eg. 'AB'.\nIf you didn't receive a double letter \
score press enter. \n").lower()))

        # Getting letters that receive triple letter points
        word_details.append(list(input("\nPlease enter the letters you received a triple letter score for.\nIf you received a triple letter \
score for multiple letters, there is no need to separate them. Eg. 'AB'.\nIf you didn't receive a triple letter score press enter. \n").lower())) 
        # Checking if letters are in word and not in double letter score
        while any(letter not in word for letter in word_details[2]) or any(letter in word_details[1] for letter in word_details[2]):
            word_details[2] = (list(input("\nInvalid input. Please enter the letters from the word you played that recieved a triple letter score. \
\nIf you received a triple letter score for multiple letters, there is no need to separate them. Eg. 'AB'.\nIf you didn't receive a triple letter \
score press enter. \n").lower()))

        # Checking for double word score
        double_word = input("\nDid you receive a double word score? (Y/N) ").upper()
        while double_word not in ["Y", "N"]:
            double_word = input("\nInvalid input. Please enter 'Y' or 'N'. ").upper()
        word_details.append(double_word)

        # Checking for triple word score
        triple_word = input("\nDid you receive a triple word score? (Y/N) ").upper()
        while triple_word not in ["Y", "N"]:
            triple_word = input("\nInvalid input. Please enter 'Y' or 'N'. ").upper()
        word_details.append(triple_word)

        # print(word_details)

        # Adding word detail to player's list of words and update their points
        play_word(player, word_details)
        print(f"\nThe word {word_details[0]} has been added to your list of words.")
        print(f"You received {score_word(word_details)} points for {word_details[0]}")
        print(f"Your total points are: {player_to_points[player]}")

    # Asking if players want to continue after they have each had their turn
    keep_playing = input("\nDo you want to continue playing? (Y/N) ").upper()
    while keep_playing not in ["Y", "N"]:
        keep_playing = input("\nInvalid input. Please enter 'Y' or 'N'. ").upper()
    
    # End of Game
    if keep_playing == "N":
        # Final scores
        print("\nThank you for playing! The final points are: ")
        for player, points in player_to_points.items():
            print(f"{player}: {points}")

        # Determining the winner
        points = list(player_to_points.values())
        if points.count(max(points)) > 1: 
            winners = []
            for player in player_to_points.keys():
                if player_to_points[player] == max(points):
                    winners.append(player)   
            print("\nThe game has finished in a tie between the following people: ")
            while winners != []:
                print(f"{winners.pop()}")
        else:
            winner = max(player_to_points, key=player_to_points.get) 
            print(f"\nCongratulations {winner}! You are the winner!")
            
        game_on = False

