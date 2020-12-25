import words
# words = {"носорог":"rhino", "орёл":"eagel","ящерица":"lizard","гепард":"cheetah","олень":"deer","лось":"elk","ёлка":"fir-tree","сосна":"pine-tree","представлять":"to imagine"}
rus_words=dict([[v,k] for k,v in words.items()])
def eng():
    eng_words=dict([[v, k] for k,v in words.items()])
    find_word = input("Enter word")
    count = 0
    for i in eng_words:
        if i == find_word:
            print(eng_words.get(find_word) or 'No such key')
        else:
            count += 1
    if count == 9:
        rus()
def rus():
    find_word = input("Enter word")
    for i in rus_words:
        if i == find_word:
            print(rus_words.get(find_word) or 'No such key')
eng()
