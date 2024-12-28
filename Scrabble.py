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
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], \
"Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

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


# Function to add a word to a player's list of words
def play_word(player, word):
    player_to_words[player].append(word)
    return update_point_totals()

# Testing play_word function
print(play_word("player1", "code"))

