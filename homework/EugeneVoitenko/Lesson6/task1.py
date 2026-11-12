text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)
words = text.split()
fin_text = []
for word in words:
    if word[-1] == ',':
        word = word.replace(',', '')
        word = word + "ing" + ","
        fin_text.append(word)
    elif word[-1] == '.':
        word = word.replace('.', '')
        word = word + "ing" + "."
        fin_text.append(word)
    else:
        word = word + "ing"
        fin_text.append(word)
print(' '.join(fin_text))
