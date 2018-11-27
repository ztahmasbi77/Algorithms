from scramble_support import *

if __name__ == "__main__":
    words=[]
    while(1):
        raw_input = input("Enter next word ")
        numbers = re.findall(r'\d',raw_input)
        wildcard = re.findall(r'\?',raw_input)
        letters = re.sub(r'[\d\?]+', '', raw_input)
        junk = re.findall(r'[\W]',letters)
        if junk != []:
            print("Invalid Input")
            continue
        letters = letters.lower()
        letters = list(letters)
        for i in numbers:
            random_letters(letters,int(i))
        if wildcard == []:
            if len(letters) > max_letters:
                print("Too many letters. Maximum letters limit =",max_letters)
                continue
            if vowels_present(letters):
                sort_letters(letters)
                words=word_search(letters)
            else:
                print("No vowels present in the letters = ",letters)
                continue
        else:
                if len(letters)+1 > max_letters:
                    print("Too many letters. Maximum letters limit =",max_letters)
                    continue
                for wild in points_for:
                    wild_letters = letters.copy()
                    wild_letters.append(wild)
                    if vowels_present(wild_letters):
                        sort_letters(wild_letters)
                        words=word_search(wild_letters)
                        if words != []:
                            print("words found = ",words)
                            break
        if words != []:
            print("Word with maximum score is ", words," with a score of ",get_word_score(words));
        else:
            print("No word can be made with the letters ",letters)
