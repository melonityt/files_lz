import docx
import re                                                    #нужно для того чтобы разбить текст на слова и символы
import pandas as pd

doc = docx.Document('lion.docx')
text = []

for paragraph in doc.paragraphs:
    text.append(paragraph.text)
text = '\n'.join(text).lower()                                #.lower() делает все заглавные буквы обычными там где \n там добовляется этот знак после параграфа при склейке

# Создаём массив слов
words_all = re.findall(r'\w+|[^\w\s]', text)                      #Вместо words = text.split() теперь использую re чтобы отделить знаки (r'\w+|[^\w\s]' шаблон для отделения
words_only = re.findall(r'[^\W\d_]+', text)

words_series = pd.Series(words_only)                               #создаём табличку pandas с нашими совами и знаками
words_count = words_series.value_counts()                     #считаем повторения

words_df = words_count.reset_index()                            #с помощью .reset_index()      series преобразуются в DataFrame
words_df.columns = ['Слово', 'Частота встречи, раз']
words_df['Частота встречи в %'] = ((words_df['Частота встречи, раз'])/(words_df['Частота встречи, раз'].sum()))*100             #добавляем новый столбец

print(words_df)
# print(words_df.to_string(index=False))                        #выведет таблицу без индексов




