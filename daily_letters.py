from main import word_list
from random import randint

def daily_letters():
    random_word_list = [n for n in word_list if len(set(n)) == 7]
    better_word_list = [n for n in random_word_list if not n[0].isupper()]
    random_word = better_word_list[randint(0, len(random_word_list)-1)]
    daily_letters = [n for n in set(random_word)]
    
    return daily_letters