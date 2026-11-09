#Word guessing game
import random
word_bank = ["Africa", "Asia", "Europe", "North America", "South America", "Australia", "Antarctica"]
word = random.choice(word_bank).casefold()

print("Welcome to the Word Guessing Game!")

print("Topic: Continents")

guessedWord = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    
    guess = input('Guess a letter or the full word: ').strip().casefold()
    
    if guess == word.casefold():
        print(f"\nCongratulations! You guessed the word: {word}")
        break
    elif len(guess) == 1 and guess in word.casefold():
        for i in range(len(word)):
            if word[i].casefold() == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Incorrect guess. You have ' + str(attempts) + ' ' + 'guesses remaining,')
    if '_' not in guessedWord:
        print(f"\nCongratulaions!! You guessed the word correctly: {word}") 
        break

if attempts == 0:
    print('\nSorry, you have run out of attempts. The word was: ' + word)  