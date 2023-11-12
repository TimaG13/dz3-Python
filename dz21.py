def is_palindrome(text):
    # Видаляємо з рядка всі знаки пунктуації та розмірність букв
    clean_text = ''.join(c.lower() for c in text if c.isalnum())

    # Порівнюємо чистий рядок з його реверсом
    return clean_text == clean_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")