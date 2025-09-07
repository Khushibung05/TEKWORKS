def preLetterCase(s, letter):
    # Make search case-insensitive
    index = s.lower().find(letter.lower())

    if index == -1:  # Letter not found
        return s.lower()
    elif index == 0:  # Letter is the first character
        return s.upper()
    else:
        # Before index -> lowercase, from index onwards -> uppercase
        return s[:index].lower() + s[index:].upper()


# Examples
print(preLetterCase("CAtCHa", "a"))      # "cATCHA"
print(preLetterCase("Preteen", "e"))     # "prETEEN"
print(preLetterCase("You've got this", "m"))  # "you've got this"
print(preLetterCase("Keep trying", "k"))      # "KEEP TRYING"
