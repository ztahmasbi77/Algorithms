from File_operations import *
from random import choice
import re
digits_regex="[0123456789]"
max_letters=10

def get_word_score(word):
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
                        
def random_letters(letters,n):
    for i in range(n):    
        letters.append(choice('abcdefghijklmnopqrstuvwxyz'))
    return 

def word_search(letters):
    print("letters to be searched",letters)
    words=[]
    return words
        
if __name__ == "__main__":
    data=[]
    random_letters(data,26)
    print(data)
