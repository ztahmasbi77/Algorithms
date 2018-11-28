from scramble_support import sort_letters

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

def word_adder(word):
    path=list(word)
    sort_letters(path)
    root.add_data(path,word)

def word_finder(letters):
    path=list(letters)
    sort_letters(path)
    return root.check_data(path)

def create_trie(file_name):
    with open(file_name) as fptr:
        word = fptr.readline().rstrip()
        while word:
           if word.isalpha():
               word_adder(word)
           #print("word = ",word)
           word = fptr.readline().rstrip()    

create_trie("wordlist")
    
