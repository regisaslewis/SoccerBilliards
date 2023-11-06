from nltk.corpus import words

word_list = words.words()
successful_words_used = []

def spelling_bee(letters, guess):
    letter_list = [n for n in letters]
    guess_list = [n for n in guess]
    invalid_letters = []

    for n in guess_list:
        if n not in letter_list:
            invalid_letters.append(n)

    if guess in successful_words_used:
        return "Already used."

    if set(guess_list) == set(letter_list):
        successful_words_used.append(guess)
        return "!! PANGRAM !!"
    
    if invalid_letters:
        return f"Invalid letter{'s' if len(invalid_letters) > 1 else ''}: {sorted(set(invalid_letters))}" 
    
    if len(guess) < 4:
        return "Word must have more than three letters."
    
    if guess not in word_list:
        return "Not in the word list."
    
    if letter_list[0] not in guess:
        return "Center letter isn't used."

    successful_words_used.append(guess)
    return "Success!"