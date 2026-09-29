import random


# -------------------------------------------------
# WORD DATABASE
# -------------------------------------------------

words = {
    "python": "A popular programming language",
    "computer": "An electronic machine used for processing data",
    "keyboard": "A device used to type text",
    "internet": "A worldwide network connecting computers",
    "developer": "A person who creates software",
    "algorithm": "A step-by-step method used to solve a problem",
    "database": "A collection of organized information",
    "programming": "The process of writing instructions for computers",
    "software": "A set of programs used by a computer",
    "hardware": "The physical parts of a computer"
}


# -------------------------------------------------
# HANGMAN VISUAL STAGES
# -------------------------------------------------

hangman_stages = [
    """
       +---+
       |   |
           |
           |
           |
          ===
    """,

    """
       +---+
       |   |
       O   |
           |
           |
          ===
    """,

    """
       +---+
       |   |
       O   |
       |   |
           |
          ===
    """,

    """
       +---+
       |   |
       O   |
      /|   |
           |
          ===
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
           |
          ===
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
          ===
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
          ===
    """
]


# -------------------------------------------------
# DISPLAY WORD
# -------------------------------------------------

def display_word(word, guessed_letters):
    """
    Display guessed letters and underscores
    for letters that have not been guessed.
    """

    result = ""

    for letter in word:

        if letter in guessed_letters:
            result += letter + " "

        else:
            result += "_ "

    return result


# -------------------------------------------------
# PLAY HANGMAN
# -------------------------------------------------

def play_game():

    # Select a random word
    word = random.choice(list(words.keys()))

    # Get the hint for that word
    hint = words[word]

    # Store guessed letters
    guessed_letters = set()

    # Count wrong guesses
    wrong_guesses = 0

    # Maximum wrong guesses
    max_attempts = 6

    # Score
    score = 100

    print("\n" + "=" * 50)
    print("             HANGMAN GAME")
    print("=" * 50)

    print("\n💡 Hint:", hint)

    # -------------------------------------------------
    # MAIN GAME LOOP
    # -------------------------------------------------

    while wrong_guesses < max_attempts:

        # Show Hangman drawing
        print(hangman_stages[wrong_guesses])

        # Show current word
        print("Word:", display_word(word, guessed_letters))

        # Show guessed letters
        if guessed_letters:
            print(
                "Guessed letters:",
                " ".join(sorted(guessed_letters))
            )
        else:
            print("Guessed letters: None")

        print("Score:", score)
        print(
            "Remaining attempts:",
            max_attempts - wrong_guesses
        )

        # -------------------------------------------------
        # CHECK WIN
        # -------------------------------------------------

        if all(letter in guessed_letters for letter in word):

            print("\n🎉 CONGRATULATIONS!")
            print("You guessed the word:", word)
            print("Your final score:", score)

            return

        # -------------------------------------------------
        # USER INPUT
        # -------------------------------------------------

        guess = input(
            "\nEnter a letter or type 'hint': "
        ).lower().strip()

        # -------------------------------------------------
        # HINT
        # -------------------------------------------------

        if guess == "hint":

            print("\n💡 Hint:", hint)

            continue

        # -------------------------------------------------
        # INPUT VALIDATION
        # -------------------------------------------------

        if len(guess) != 1 or not guess.isalpha():

            print(
                "⚠️ Invalid input! "
                "Please enter only one letter."
            )

            continue

        # -------------------------------------------------
        # CHECK REPEATED LETTER
        # -------------------------------------------------

        if guess in guessed_letters:

            print(
                "⚠️ You already guessed that letter."
            )

            continue

        # Add letter to guessed letters
        guessed_letters.add(guess)

        # -------------------------------------------------
        # CHECK CORRECT / WRONG GUESS
        # -------------------------------------------------

        if guess in word:

            print("✅ Correct guess!")

            # Add points
            score += 10

        else:

            print("❌ Wrong guess!")

            # Increase wrong guesses
            wrong_guesses += 1

            # Reduce score
            score -= 10

    # -------------------------------------------------
    # GAME OVER
    # -------------------------------------------------

    print(hangman_stages[wrong_guesses])

    print("\n💀 GAME OVER!")
    print("The correct word was:", word)
    print("Your final score:", score)


# -------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------

print("\n🎮 Welcome to the Hangman Game!")

while True:

    play_game()

    play_again = input(
        "\nDo you want to play again? (yes/no): "
    ).lower().strip()

    if play_again != "yes":

        print("\nThank you for playing Hangman! 👋")

        break