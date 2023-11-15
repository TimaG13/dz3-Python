def popular_words(text, words):
    # Розділити текст на слова та перетворити їх у нижній регістр
    word_list = text.lower().split()

    # Ініціалізувати словник для зберігання кількості зустрічей кожного слова
    word_count = {word: 0 for word in words}

    # Підрахунок кількості зустрічей кожного слова в тексті
    for word in word_list:
        if word in word_count:
            word_count[word] += 1

    return word_count

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

