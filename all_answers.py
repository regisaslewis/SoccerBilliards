from main import word_list

def all_answers(copy):
    answers = [n for n in word_list if len(n) >= 4 and copy[0] in n]
    checklist = []
    for n in answers:
        letters = [x for x in n]
        if set(letters) <= set(copy):
            checklist.append(n)                    
    pangrams = [n for n in word_list if len(n) > 4 and copy[0] in n and set(n) == set(copy)]
    points = 0
    four_letter_words = [n for n in checklist if len(n) == 4]
    more_letter_words_as_points = [len(n) for n in checklist if len(n) > 4 and n not in pangrams]
    pangrams_as_points = [(len(n) + 7) for n in pangrams]
    points += len(four_letter_words)
    points += sum(more_letter_words_as_points)
    points += sum(pangrams_as_points)

    print("All Words: ", checklist)
    print("Pangrams: ", pangrams)
    print("Total Possible Points: ", points)