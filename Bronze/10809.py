alpha = list(range(97,123))
word = input()
for x in alpha:
    print(word.find(chr(x)), end=' ')
print()