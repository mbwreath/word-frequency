strip_char = [",",".","!","-","?",":",";","/",]
letter_list = []
my_Dict = {}
with open("sample.txt") as a_file:
    count = 0
    while a_file.readline():
        text = a_file.readline()
        for char in strip_char:
            text=text.replace(char, "").lower()
            list_of_words = text.split()
        for word in list_of_words:
            if word in my_Dict:
                my_Dict[word] += 1
            else:
                my_Dict[word] = 1

new_Dict = sorted(my_Dict.items(), key = lambda word: word[1], reverse = True)

for word in new_Dict[0:20]:
    print(word)


    
