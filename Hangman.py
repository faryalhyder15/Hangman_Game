
#==========================TASK 1 HANGMAN GAME==================================
import random

HANGMAN_STAGES = [
    # 0 wrong guesses
    """
       ┌────┐
       │    │
            │
            │
            │
            │
    ════════╧════
    """,
    # 1 wrong guess
    """
       ┌────┐
       │    │
       O    │
            │
            │
            │
    ════════╧════
    """,
    # 2 wrong guesses
    """
       ┌────┐
       │    │
       O    │
       │    │
            │
            │
    ════════╧════
    """,
    # 3 wrong guesses
    """
       ┌────┐
       │    │
       O    │
      /│    │
            │
            │
    ════════╧════
    """,
    # 4 wrong guesses
    """
       ┌────┐
       │    │
       O    │
      /│\\   │
            │
            │
    ════════╧════
    """,
    # 5 wrong guesses
    """
       ┌────┐
       │    │
       O    │
      /│\\   │
      /     │
            │
    ════════╧════
    """,
    # 6 wrong guesses — GAME OVER
    """
       ┌────┐
       │    │
       O    │
      /│\\   │
      / \\   │
            │
    ════════╧════
    """,
]

# ==================WORD BANK==================================
WORD_LIST = ["python", "hangman", "laptop", "coding", "script"]

MAX_WRONG = 6


def display_word(secret_word: str, guessed: set) -> str:
    """Return the word with blanks for un-guessed letters."""
    return "  ".join(
        letter if letter in guessed else "_" for letter in secret_word
    )


def play_hangman():
    secret_word = random.choice(WORD_LIST)
    guessed_letters: set = set()
    wrong_guesses: list = []

    print("\n" + "═" * 50)
    print("         WELCOME TO HANGMAN  ")
    print("═" * 50)
    print(f"  The word has  {len(secret_word)}  letters. Good luck!\n")

    while True:
        wrong_count = len(wrong_guesses)

        # Draw gallows
        print(HANGMAN_STAGES[wrong_count])

        # Show progress
        print(f"  Word : {display_word(secret_word, guessed_letters)}")
        print(f"  Wrong guesses ({wrong_count}/{MAX_WRONG}) : "
              f"{', '.join(sorted(wrong_guesses)) or 'none yet'}")
        print()

        # Win check
        if all(ch in guessed_letters for ch in secret_word):
            print("    YOU WIN!  The word was:", secret_word.upper())
            break

        # Lose check
        if wrong_count >= MAX_WRONG:
            print("    GAME OVER!  The word was:", secret_word.upper())
            break

        # Get input
        guess = input("  Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("   Please enter a single letter.\n")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("    You already guessed that letter!\n")
            continue

        if guess in secret_word:
            guessed_letters.add(guess)
            print(f"    '{guess}' is in the word!\n")
        else:
            wrong_guesses.append(guess)
            remaining = MAX_WRONG - len(wrong_guesses)
            print(f"    '{guess}' is NOT in the word. "
                  f"{remaining} guess(es) remaining.\n")

    # Play again
    again = input("\n  Play again? (y/n): ").strip().lower()
    if again == "y":
        play_hangman()
    else:
        print("\n  Thanks for playing! Goodbye \n")


if __name__ == "__main__":
    play_hangman()
