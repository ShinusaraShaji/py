text=input("Enter a line:")
words=text.spli t()
word_count={word:words.count(word)for word in set(words)}
print(word_count)
