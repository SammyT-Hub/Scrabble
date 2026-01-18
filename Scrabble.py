"""
Scrabble Calculator Project

The goal of this project is to build a calculator that will accompany a game of Scrabble. This calculator can be used to keep track of scores
and words that each player has played throughout the game. Finally, the calculator will be able to determine who has won the game at its conclusion.
"""

# importing TWL module that contains a list of words that are valid in Scrabble
import twl

# Functions
def score_word(word_details: dict) -> int:
    """
    Calculates the score for a word played.

    Parameters:
    - word_details: dictionary containing the following details about the word played:
        word: str - the word played
        blank tiles: list - letters that were played using blank tiles
        double letters: list - letters that receive double letter points
        triple letters: list - letters that receive triple letter points
        double word score: str - "Y" if the word receives double word points, "N" otherwise
        triple word score: str - "Y" if the word receives triple word points, "N

    Outputs:
    - returns the score of the word played.
    """
    point_total = 0
    for letter in word_details["word"]:
        if letter in word_details["blank tiles"]:
            point_total += 0
        if letter in word_details["double letters"]:
            point_total += 2 * letter_to_points.get(letter, 0)
        elif letter in word_details["triple letters"]:
            point_total += 3 * letter_to_points.get(letter, 0)
        else:
            point_total += letter_to_points.get(letter, 0)
    if word_details["double word score"] == "Y":
        return point_total * 2
    elif word_details["triple word score"] == "Y":
        return point_total * 3
    else:
        return point_total

def play_word(player: str, word_details: dict) -> None:
    """
    Add a word to the player's list of words in `player_to_words` and updates player's score in `player_to_points`.

    Parameters:
    - player: name of player.
    - word_details: dictionary containing the following details about the word played:
        word: str - the word played
        blank tiles: list - letters that were played using blank tiles
        double letters: list - letters that receive double letter points
        triple letters: list - letters that receive triple letter points
        double word score: str - "Y" if the word receives double word points, "N" otherwise
        triple word score: str - "Y" if the word receives triple word points, "N

    Outputs:
    - None
    """

    # Adding word to player in `player_to_words`.
    player_to_words[player].append(word_details)

    # Updating player's score.
    update_point_totals(player, word_details)

    return

def update_point_totals(player: str, word_details: dict) -> None:
    """
    Scores player's word using `score_word()` and adds this to player's points in `player_to_points`.

    Parameters:
    - player: name of player.
    - word_details: dictionary containing the following details about the word played:
        word: str - the word played
        blank tiles: list - letters that were played using blank tiles
        double letters: list - letters that receive double letter points
        triple letters: list - letters that receive triple letter points
        double word score: str - "Y" if the word receives double word points, "N" otherwise
        triple word score: str - "Y" if the word receives triple word points, "N

    Outputs:
    - prints a message stating the word that was played along with a score update.
    """

    # Adding score to player.
    player_to_points[player] += score_word(word_details)

    # Sorting players based on score.
    player_to_points_sorted = sorted(player_to_points, key = player_to_points.get, reverse = True)
  
    # Generating message and updated leaderboard
    print(f"\n{player} has played {word_details["word"]} and scored {score_word(word_details)}pts. The updated scores are:")
    for player in player_to_points_sorted:
        print(f"\t{player} {player_to_points[player]}pts")




# Setting up dictionaries for scrabble game

# List of letters and their corresponding points in Scrabble
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", \
"v", "w", "x", "y", "z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Dictionary with the letters and their corresponding points
letter_to_points = {key:value for key, value in zip(letters, points)}

# Dictionary with the players and their words
player_to_words = {}

# Dictionary with the players and their points
player_to_points = {}



# Adding players to the game

# Adding the first player
player = input("Player 1, please enter your player name: ")
player_to_words[player] = []
player_to_points[player] = 0

# Adding more players
more_players = "Y"
n = 2  # counter for player number
while more_players == "Y":
    player = input(f"Player {n}, please enter your player name: ")
    while player in player_to_words.keys():
        player = input("This player name is already taken. Please enter a different name. ")
    player_to_words[player] = []
    player_to_points[player] = 0
    more_players = input("Do you want to add more players? (Y/N) ").upper()
    while more_players not in ["Y", "N"]:
        more_players = input("Invalid input. Please enter 'Y' or 'N'. ").upper()
    n += 1



# Welcome message
print("\nWelcome to the Scrabble game! The players are: ")
for player in player_to_words.keys():
    print(player)



# Gameplay
game_on = True
while game_on:
    for player in player_to_words.keys():
        next_move = input(f"\nIt's {player}'s turn. Do you wish to:\n\t1. play \n\t2. swap tiles \n\t3. pass\
\n\nPlease enter the number corresponding to your choice: ")
        while next_move not in ["1", "2", "3"]:
            next_move = input("\nInvalid input. Please enter '1', '2', or '3': ")
        if next_move == "2" or next_move == "3":
            print(f"\n{player} has chosen to {'swap tiles' if next_move == '2' else 'pass'}. Next player's turn.")
        else:

            # Initialising dictionary containing word_details to be used in play_word function
            word_details = {}

            # Getting number of words played
            num_of_words = int(input("\nHow many words did you play this turn? "))
            while num_of_words < 1:
                num_of_words = int(input("\nInvalid input. Please enter a positive integer for the number of words you are playing this turn: "))

            # Checking if player got a bingo
            bingo = input("\nDid you use all 7 of your tiles in one turn? (Y/N) ").upper()
            while bingo not in ["Y", "N"]:
                bingo = input("\nInvalid input. Please enter 'Y' or 'N'. ").upper()
            if bingo == "Y":   
                player_to_points[player] += 50
                print(f"\nCongratulations {player}! You have received a 50 point bonus for getting a bingo!")

            # Getting words played
            for i in range(num_of_words):

                order = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

                word = (input(f"\nPlease enter the {order[i]} word you played: ").lower())

                # Checking if word is valid
                while twl.check(word) == False:
                    word = (input("\nInvalid word. Please enter a valid word: ").lower())
                word_details["word"] = word

                # Converting word to list for easier checking of letters
                word = list(word)

        
                # Getting letters that players used a blank tile for
                word_details["blank tiles"] = (list(input("\nPlease enter the letters you used a blank tile for.\nIf you used multiple blank tiles, \
there is no need to separate them. Eg. 'AB'.\nIf you didn't use a blank tile press enter. \n").lower()))
        
                # Checking if letters are in word
                while any(letter not in word for letter in word_details["blank tiles"]):
                    word_details["blank tiles"] = (list(input("\nInvalid input. Please enter the letters from the word you played that blank tiles were used for. \
\nIf you used multiple blank tiles, there is no need to separate them. Eg. 'AB'.\nIf you didn't use a blank tile press enter. \n").lower()))
        
                # Removing blank tile letters from word list to avoid issues when checking for double/triple letter scores
                for letter in word_details["blank tiles"]:
                    word.remove(letter)

        
                # Getting letters that receive double letter points
                word_details["double letters"] = (list(input("\nPlease enter the letters you received a double letter score for.\nIf you received a double letter \
score for multiple letters, there is no need to separate them. Eg. 'AB'.\nIf you didn't receive a double letter score press enter. \n").lower()))
        
                # Checking if letters are in word
                while any(letter not in word for letter in word_details["double letters"]):
                    word_details["double letters"] = (list(input("\nInvalid input. Please enter the letters from the word you played that recieved a double letter score. \
\nIf you received a double letter score for multiple letters, there is no need to separate them. Eg. 'AB'.\nIf you didn't receive a double letter \
score press enter. \n").lower()))
            
                # Removing double letters from word list to avoid issues when checking for triple letter scores
                for letter in word_details["double letters"]:
                    word.remove(letter)


                # Getting letters that receive triple letter points
                word_details["triple letters"] = (list(input("\nPlease enter the letters you received a triple letter score for.\nIf you received a triple letter \
score for multiple letters, there is no need to separate them. Eg. 'AB'.\nIf you didn't receive a triple letter score press enter. \n").lower())) 
        
                # Checking if letters are in word
                while any(letter not in word for letter in word_details["triple letters"]):
                    word_details["triple letters"] = (list(input("\nInvalid input. Please enter the letters from the word you played that recieved a triple letter score. \
\nIf you received a triple letter score for multiple letters, there is no need to separate them. Eg. 'AB'.\nIf you didn't receive a triple letter \
score press enter. \n").lower()))
                

                # Checking for double word score
                double_word = input("\nDid you receive a double word score? (Y/N) ").upper()
                while double_word not in ["Y", "N"]:
                    double_word = input("\nInvalid input. Please enter 'Y' or 'N'. ").upper()
                word_details["double word score"] = double_word


                # Checking for triple word score
                triple_word = input("\nDid you receive a triple word score? (Y/N) ").upper()
                while triple_word not in ["Y", "N"]:
                    triple_word = input("\nInvalid input. Please enter 'Y' or 'N'. ").upper()
                word_details["triple word score"] = triple_word

                # print(word_details)

                # Adding `word_details` to player's list of words, update their points and showing updated leaderboard
                play_word(player, word_details)


    # Asking if players want to continue after they have each had their turn
    keep_playing = input("\nDo you want to continue playing? (Y/N) ").upper()
    while keep_playing not in ["Y", "N"]:
        keep_playing = input("\nInvalid input. Please enter 'Y' or 'N'. ").upper()
    


    # End of Game
    if keep_playing == "N":

        # Determining winner(s).
        winners = [player for player in player_to_points.keys() if player_to_points[player] == max(player_to_points.values())]

        # Announcing winners and wrapping up.
        if len(winners) == 0:
            raise "Error! There must be at least one winner."
        elif len(winners) == 1:
            print(f"\nThe winner is ...\n\t{winners[0]}\n\nCongratulations! Thank you all for playing:)")
        else:
            print(f"The winners are ...")
            for player in winners:
                print(f"\t{player}")
            print(f"\nCongratulations! Thank you all for playing:)")
            
        game_on = False

