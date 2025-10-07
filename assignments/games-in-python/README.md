# 📘 Assignment: Hangman Game

## 🎯 Objetivo

Implement a classic Hangman game in Python to practice string manipulation, loops, conditionals, and user input. You will build a playable command-line game that reinforces core programming concepts.

## 📝 Tarefas

### 🛠️ Game Logic and User Interaction

#### Description

Create a Python script that runs the Hangman game in the terminal. The game should select a word, accept guesses, and display progress to the player.

#### Requirements

Completed program should:

- Randomly select a word from a predefined list.
- Display the word with underscores for unguessed letters (e.g. `_ a n g m a n`).
- Accept single-letter guesses from the user and validate input (must be a new, alphabetical character).
- Show the current progress and letters already guessed after each turn.
- Track and display the number of incorrect guesses remaining.
- End the game with a win message if the word is guessed, or a lose message revealing the word if attempts run out.

Example output:

```
Word: _ a n g m a n
Guesses left: 4
Guessed letters: a, n, g, m
Enter your next guess:
```

### 🛠️ Code Organization

#### Description

Structure your code using functions for key operations (e.g., word selection, input validation, updating game state).

#### Requirements

Completed program should:

- Use at least three functions (e.g., `choose_word()`, `display_progress()`, `process_guess()`).
- Include comments and docstrings for clarity.
- Be easy to read and modify.
