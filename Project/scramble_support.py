from File_operations import *
from Number_operations import *
from random import choice
import re

max_letters=10
many_letters = False

class Trie:

    def __init__(self,letter_value = None):
        self.letter = letter_value
        self.data = []
        self.branches = []
        
    def add_data(self,path,word):
        #print("path = ",path,"word = ",word)
        found = False
        if path == []:
            self.data.append(word)
            #print("Added word",word)
            return        
        for node in self.branches:
            if node.letter == path[0]:
                found = True
                break
        if found:
            #print("Previous branch found for ",path[0])
            node.add_data(path[1:],word)
        else:
            #print("New branch created for ",path[0])
            new_node=Trie(path[0])
            self.branches.append(new_node)
            new_node.add_data(path[1:],word)
        return

    def print_trie(self):
        print("letter value = ",self.letter)
        print("data = ",self.data)
        print("Branches = ",len(self.branches))
        for node in self.branches:
            print("Branch ",self.letter,"->",node.letter)
            node.print_trie()
    
    def check_data(self,path):
        if path == []:
            if self.data == []:
                return None
            else:
                return self.data 
        found = False
        for node in self.branches:
            if node.letter == path[0]:
                found = True
                break
        if found:
            return node.check_data(path[1:])
        else:
             return None       

root = Trie()    

def vowels_present(letters):
    try:
        check_letters = ''.join(letters)
    except:
        check_letters = letters
    vowels = re.findall(r'[aeiouy]',check_letters)
    if vowels == []:
        return False
    else:
        return True
    
def get_word_score(raw_word):
    try:
        word = list(''.join(raw_word[0]))
    except:
        word = raw_word
    score = 0
    for letter in word:
        score += int(points_for[letter])
    return score

def sort_letters(data): 
    n = len(data)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if int(points_for[data[j]]) < int(points_for[data[j+1]]):
                data[j],data[j+1]= data[j+1],data[j]
            elif int(points_for[data[j]]) == int(points_for[data[j+1]]):
                if data[j]>data[j+1]:
                    data[j],data[j+1] = data[j+1],data[j]
    return

def sort_words(data):
    n = len(data)
    if n == 1:
        return data
    elif n == 2:
        if get_word_score(data[0]) < get_word_score(data[1]):
            data[0],data[1] = data[1],data[0]
        return data
    else:
        data_1 = sort_words(data[:int(n/2)])
        data_2 = sort_words(data[int(n/2):])
        n_1 = len(data_1)
        n_2 = len(data_2)
        counter_1=0
        counter_2=0
        counter_merge=0
        while(counter_1 < n_1 or counter_2 < n_2):
            if counter_1 < n_1 and counter_2 < n_2:
                if get_word_score(data_1[counter_1]) > get_word_score(data_2[counter_2]):
                    data[counter_merge] = data_1[counter_1]
                    counter_1 += 1
                else:
                    data[counter_merge] = data_2[counter_2]
                    counter_2 += 1
            elif counter_1 < n_1:
                data[counter_merge] = data_1[counter_1]
                counter_1 += 1
            else:
                data[counter_merge] = data_2[counter_2]
                counter_2 += 1
            counter_merge += 1
        return data

def list_checker(needle,haystack):
    for hay in haystack:
        if needle == hay:
            return True
    return False

def word_adder(word):
    path=list(word)
    sort_letters(path)
    root.add_data(path,word)

def word_finder(letters):
    path=list(letters)
    sort_letters(path)
    return root.check_data(path)
                        
def random_letters(letters,n):
    for i in range(n):    
        letters.append(choice('abcdefghijklmnopqrstuvwxyz'))
    return 

def word_search(words,letters):
    #print("letters to be searched",letters)
    groups=[]
    for i in range(len(letters),0,-1):
        groups=group_generator(letters,i)
        for element in groups:
            if vowels_present(element):
                temp=root.check_data(element)
                if temp != None:
                    if not list_checker(temp,words):
                        words.append(temp)
                if (many_letters) & (len(words)>0):
                    return words
                #print("path = ",element)
    return words

def create_trie(file_name):
    with open(file_name) as fptr:
        word = fptr.readline().rstrip()
        while word:
           if word.isalpha():
               word_adder(word)
           #print("word = ",word)
           word = fptr.readline().rstrip()    

create_trie("wordlist.txt")
      
if __name__ == "__main__":
    data=[]
    random_letters(data,26)
    print(data)
