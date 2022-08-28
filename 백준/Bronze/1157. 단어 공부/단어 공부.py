from itertools import count

max = 0
word = input().upper() #Mississipi
set_word = set(word)
set_word = list(set_word) #['m', 'i', 'p', 's']

for i in range(len(set_word)):
    if max < word.count(set_word[i]):
        max = word.count(set_word[i])
        result = set_word[i]
    elif max == word.count(set_word[i]):
        result = '?'
print(result)

