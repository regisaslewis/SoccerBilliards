from main import word_list

def all_answers(copy):
    answers = [n for n in word_list if len(n) > 4 and copy[0] in n]
    checklist = []
    for n in answers:
        letters = [x for x in n]
        if set(letters) <= set(copy):
            checklist.append(n)                    
    pangrams = [n for n in word_list if len(n) > 4 and copy[0] in n and set(n) == set(copy)]
    print("All Words: ", checklist)
    print("Pangrams: ", pangrams)