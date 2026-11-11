import docx

f = open('test.txt', 'w')

doc = docx.Document('lion.docx')


text = []
for paragraph in doc.paragraphs:
    text.append(paragraph.text)

print('\n'.join(text).lower())          #.lower() делает все заглавные буквы обычными

words = [for w in text.split()]


f.close()


# # количество абзацев в документе
# print(len(doc.paragraphs))

# # текст первого абзаца в документе
# print(doc.paragraphs[0].text)

# # текст второго абзаца в документе
# print(doc.paragraphs[1].text)

# # текст третьего предложения(Run) второго абзаца
# print(doc.paragraphs[1].runs[3].text)