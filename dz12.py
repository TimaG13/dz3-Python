# 'Python Community' #-> #PythonCommunity
# 'i like python community!' #-> #ILikePythonCommunity
text = 'Should, I. subscribe? Yes!'  # -> #ShouldISubscribeYes    string.punctuation

import string

# Введення рядка від користувача
# text = input("Введіть текст: ")

# Видалення символів пунктуації
text = ''.join(symbol for symbol in text if symbol not in string.punctuation)

# Розділити рядок на слова та перетворити першу літеру кожного слова на велику
words = text.split()

converted_words = [word[0].upper() + word[1:] for word in words]

# Об'єднати перетворені слова у хештег та обмежити його до 140 символів
hashtag = '#' + ''.join(converted_words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
