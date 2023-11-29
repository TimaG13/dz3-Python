import re
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    # Зчитуємо вміст html-файлу
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Використовуємо регулярний вираз для видалення html-тегів
    cleaned_text = re.sub(r'<.*?>', '', html)

    # Видаляємо порожні рядки
    cleaned_text = '\n'.join(line for line in cleaned_text.splitlines() if line.strip())

    # Записуємо очищений текст у вказаний файл
    with codecs.open(result_file, 'w', 'utf-8') as result:
        result.write(cleaned_text)

# Приклад виклику функції
delete_html_tags('draft.html', 'cleaned.txt')
