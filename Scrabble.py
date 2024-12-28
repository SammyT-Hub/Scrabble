# List of letters and their corresponding points in Scrabble
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", \
"V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Dictionary with the letters and their corresponding points
letter_to_points = {key:value for key, value in zip(letters, points)}

# Add a key-value pair to the dictionary for blank tiles
letter_to_points[" "] = 0


# Function to calculate the points of a word
def score_word(word):
    word = word.upper()
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

# Testing score_word function
brownie_points = score_word("BROWNIE")
# print(brownie_points)


# Dictionary with the players and their words
player_to_words = {}

# Dictionary with the players and their points
player_to_points = {}

# Calculating the points of each player and storing them in player_to_points
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    return player_to_points

# Function to add a word to a player's list of words and update their points
def play_word(player, word):
    player_to_words[player].append(word)
    return update_point_totals()

# Testing play_word function
# print(play_word("player1", "code"))


# Adding players to the game
# Adding the first player
player = str(input("Player 1, please enter your player name: "))
player_to_words[player] = []

# Adding more players
more_players = "Y"
n = 2
while str(more_players).upper() == "Y":
    player = str(input("Player {}, please enter your player name: ".format(n)))
    while player in player_to_words.keys():
        player = str(input("This player name is already taken. Please enter a different name. "))
    player_to_words[player] = []
    more_players = input("Do you want to add more players? (Y/N) ")
    while str(more_players).upper() not in ["Y", "N"]:
        more_players = input("Invalid input. Please enter 'Y' or 'N'. ")
    n += 1

# Welcome message
print("Welcome to the Scrabble game! The players are: ")
for player in player_to_words.keys():
    print(player)


# Gameplay
game_on = True
while game_on:
    for player in player_to_words.keys():
        print("\nIt's {}'s turn.".format(player))
        word = input("Please enter the word you want to play: ")
        play_word(player, word)
        print("The word {} has been added to your list of words.".format(word))
        print("Your total points are: {}".format(player_to_points[player]))
    game_on = input("Do you want to continue playing? (Y/N) ")
    while str(game_on).upper() not in ["Y", "N"]:
        game_on = input("Invalid input. Please enter 'Y' or 'N'. ")
    if str(game_on).upper() == "N":
        print("\nThank you for playing! The final points are: ")
        for player, points in player_to_points.items():
            print("{}: {}".format(player, points))
        winner = max(player_to_points, key=player_to_points.get)
        print("\nCongratulations {}! You are the winner!".format(winner))
        break
    else:
        continue

