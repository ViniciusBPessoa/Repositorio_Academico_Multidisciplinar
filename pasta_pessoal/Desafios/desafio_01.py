letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def selectLetters(letter : int) -> list:
    letter -= 1
    letter = letters[letter]
    for l in letters:
        if l == letter:
            index = letters.index(l)
            arrey_letter = letters[:index + 1]
    return arrey_letter
        
print(selectLetters(2))