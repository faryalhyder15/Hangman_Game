# 🎮 Hangman Game (Python)

A simple command-line Hangman game built in Python where the player guesses letters to uncover a hidden word before running out of attempts.

---

## 📌 Features

* Random word selection from a predefined list
* Visual Hangman stages (ASCII art)
* Tracks correct and incorrect guesses
* Input validation (only single letters allowed)
* Replay option after game ends

---

## 🛠️ Technologies Used

* Python
* Built-in libraries: `random`

---

## ▶️ How to Run

1. Clone or download the project
2. Open terminal in the project folder
3. Run the script:

```bash
python hangman.py
```

---

## 🎯 Game Rules

* You must guess the hidden word one letter at a time
* Each wrong guess adds a part to the Hangman
* Maximum allowed wrong guesses: **6**
* Win by guessing all letters correctly before the Hangman is complete

---

## 🧠 Example Gameplay

```
Word : _  _  _  _  _  _
Wrong guesses (0/6): none yet

Guess a letter: a
'a' is NOT in the word. 5 guess(es) remaining.
```

---

## 🔁 Replay Option

After the game ends, you can choose to play again:

```
Play again? (y/n):
```

---

## 📂 Word List

```
["python", "hangman", "laptop", "coding", "script"]
```

---

## 🚀 Future Improvements

* Add difficulty levels
* Expand word list
* Add categories (e.g., animals, tech, etc.)
* GUI version using Tkinter or Pygame

---


If you want, I can also make a **GitHub-style professional README with badges + screenshots** or convert this into a **resume project description**.
