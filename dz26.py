def first_word(text):
    """
    Знаходження першого слова у рядку.

    :param text: Введений текст.
    :return: Перше слово у тексті.
    """
    # Заміна символів пунктуації на пробіли та розділення рядку на слова
    words = text.replace('.', ' ').replace(',', ' ').split()

    # Знайдення першого слова
    for word in words:
        cleaned_word = ''.join(filter(lambda char: char.isalpha() or char == "'", word))
        if cleaned_word:
            return cleaned_word

# Тести
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
