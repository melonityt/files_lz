import docx
import re                                                    #нужно для того чтобы разбить текст на слова и символы
import pandas as pd
import matplotlib.pyplot as plt

doc = docx.Document('lion.docx')
text = []

for paragraph in doc.paragraphs:
    text.append(paragraph.text)
text = '\n'.join(text).lower()                                #.lower() делает все заглавные буквы обычными там где \n там добовляется этот знак после параграфа при склейке

# Создаём массив слов
words_all = re.findall(r'\w+|[^\w\s]', text)                      #Вместо words = text.split() теперь использую re чтобы отделить знаки (r'\w+|[^\w\s]' шаблон для отделения
words_only = re.findall(r'[^\W\d_]+', text)
letters_and_simbols = re.findall(r'\w|[^\w\s]', text)

words_series = pd.Series(words_only)                               #создаём табличку pandas с нашими совами и знаками
words_count = words_series.value_counts()                     #считаем повторения

words_df = words_count.reset_index()                            #с помощью .reset_index()      series преобразуются в DataFrame
words_df.columns = ['Слово', 'Частота встречи, раз']
words_df['Частота встречи в %'] = ((words_df['Частота встречи, раз'])/(words_df['Частота встречи, раз'].sum()))*100             #добавляем новый столбец

#считаем буквы и символы
letters_ser = pd.Series(letters_and_simbols)
letters_count = letters_ser.value_counts()


print(words_df)

words_df.to_csv('lion.csv', sep=';', index=False)

# print(words_df.to_string(index=False))                        #выведет таблицу без индексов
# print(letters_count)


letters_count.head(len(letters_count)).plot.bar(color='#00FF00', edgecolor='black')         #это выведет гистограмму из всех букв и символов
plt.title('Частота символов в тексте')
plt.xlabel('Символ')
plt.ylabel('Количество')
plt.xticks(rotation=0)                                          #переворачивает буквы чтобы они были нормальными
plt.show()
