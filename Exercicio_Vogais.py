def vogal(char):
    vogais = "aeiouAEIOU"
    if len(char) == 1 and char in vogais:
        return True
    else:
        return False