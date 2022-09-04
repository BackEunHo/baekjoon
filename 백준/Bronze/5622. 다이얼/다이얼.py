alphabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0
word = input()
for alphabet in alphabet_list: # alphabet = 'ABC', 'DEF' ...
    for arr in alphabet: # arr = ['A','B','C'], ['D','E','F'] ...
        for word_list in word:
            if arr == word_list:
                time += alphabet_list.index(alphabet) + 3
print(time)
