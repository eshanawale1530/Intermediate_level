# Intermediate_level
Intermediate Python projects featuring a Web Scraper and Hangman game. The Web Scraper extracts useful data from websites using Python web-scraping libraries, while the Hangman project implements an interactive word-guessing game with hints and visual progress.
## 🚀 Task 2 – Intermediate Level

This section contains two intermediate-level Python projects designed to improve practical programming and problem-solving skills.

### 1. 🌐 Web Scraper

A Python-based web scraping project that extracts useful information from websites using web-scraping libraries such as Beautiful Soup or Scrapy.

**Concepts Covered:**
- Web scraping
- Extracting data from websites
- HTML parsing
- Python libraries
- Processing extracted data

### 2. 🎮 Hangman Game

A Python-based word-guessing game where the player attempts to guess a hidden word. The game provides hints and displays visual progress as the player makes guesses.

**Concepts Covered:**
- Strings
- Lists
- Loops
- Conditional statements
- User input
- Functions
- Game logic
- Hints and visual progress

### 🎯 Learning Objective

These projects helped me move from basic Python programming to more practical applications by working with web data and developing an interactive command-line game.

Intermediate-Python/
│
├── README.md
│
├── Web Scraper/
│   └── web_scraper.py
│
└── Hangman/
    └── hangman.py**

// WEB SCRAPPING //
    import requests
from bs4 import BeautifulSoup

url = "https://www.shadowfox.in/domains"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Status Code:", response.status_code)

print("\nPAGE TITLE:")
print(soup.title.get_text(strip=True))

print("\nHEADINGS:")

headings = soup.find_all(["h1", "h2", "h3"])

for heading in headings:
    print(heading.get_text(" ", strip=True))

//  HANGMAN //

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

