def correct_sentence(text):
    # Робимо перевірку на крапку в кінці
    if not text.endswith('.'):
        text += '.'
    #Робимо перевірку на заглявну літеру
    text = text[0].upper() + text[1:]
    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
