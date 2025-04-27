# Given 2 list, generate a third one with all the elements that are repeated
L_1 = ["h","o","l","a"," ", "m","u","n","d","o"]
L_2 = ["h","o","l","a", " ", "l","u","n","a"]
L_3 = []

for letter in L_1:
    if letter in L_2 and letter not in L_3:
        L_3.append(letter)

print(L_3)