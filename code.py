import random

# Sample dictionary of valid words
valid_words = ["cat", "dog", "bird", "apple", "banana", "tree", "bat", "ball"]

# Scrabble letter point values
scrabble_tiles = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# Function to calculate the score of a word
def calculate_score(word):
    score = 0
    for letter in word.upper():
        if letter in scrabble_tiles:
            score += scrabble_tiles[letter]
    return score

# Function to check if a word is valid
def is_valid_word(word):
    return word.lower() in valid_words

# Function to generate a random tile set (like drawing from a bag)
def generate_tiles():
    letters = list(scrabble_tiles.keys())
    return random.choices(letters, k=7)  # 7 tiles for a player's rack

# Main game function
def play_game():
    print("Welcome to the Scrabble Game!")
    player_tiles = generate_tiles()
    print(f"Your tiles: {', '.join(player_tiles)}")

    while True:
        word = input("Form a word (or type 'exit' to quit): ").strip().lower()
        
        if word == "exit":
            print("Thanks for playing!")
            break
        
        if is_valid_word(word) and all(word.count(letter) <= player_tiles.count(letter) for letter in word):
            score = calculate_score(word)
            print(f"'{word}' is a valid word and scores {score} points!")
            player_tiles = [tile for tile in player_tiles if tile not in word]  # Remove used tiles
            player_tiles.extend(generate_tiles())  # Draw new tiles
            print(f"Your new tiles: {', '.join(player_tiles)}")
        else:
            print("Invalid word or insufficient tiles.")
        print()

# Start the game
if __name__ == "__main__":
    play_game()
