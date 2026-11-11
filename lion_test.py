import docx

doc = docx.Document('lion.docx')


text = []
for paragraph in doc.paragraphs:
    text.append(paragraph.text)
print(text)