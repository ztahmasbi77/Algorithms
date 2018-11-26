from scramble_support import *

if __name__ == "__main__":
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
            sort_letters(letters)
            word_search(letters)
        else:
                if len(letters)+1 > max_letters:
                    print("Too many letters. Maximum letters limit =",max_letters)
                    continue
                for wild in points_for:
                    wild_letters = letters.copy()
                    wild_letters.append(wild)
                    sort_letters(wild_letters)
                    word_search(wild_letters)
        
