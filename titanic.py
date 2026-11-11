import pandas as pd
import csv
import matplotlib.pyplot as plt

# Чтение из файла .parquet
titanic_loaded = pd.read_parquet('titanic.parquet', engine='auto')

titanic_csv = open('titanic.csv', 'w')
writer = csv.writer(titanic_csv, delimiter=';')
writer.writerow(titanic_loaded.columns)  # Записываем названия столбцов
writer.writerows(titanic_loaded.values)   # Записываем данные
titanic_csv.close()

print(titanic_loaded)

# titanic_loaded.head(len(titanic_loaded)).plot.bar(color='#00FF00', edgecolor='black')
# plt.title('Выживаемость пассажиров титаника')
# plt.xlabel('Класс')
# plt.ylabel('Проценты')
# plt.xticks(rotation=0)                                          #переворачивает буквы чтобы они были нормальными
# plt.show()

# Считаем процент выживших и невыживших по каждому классу
survival = pd.crosstab(                                             #делаем таблицу для matplotlib с классом и выживаемостью
    titanic_loaded['Pclass'],
    titanic_loaded['Survived'],
    normalize='index'                                               #позволяет узнать долю каждого результата относительно общего количества
) * 100

#делаем гистограмму
classes = ['Первый класс', 'Второй класс', 'Третий класс']

plt.bar(classes, survival[1], color="#00D9FF")

plt.bar(classes, survival[0], bottom=survival[1], color="#FFBB00")          #* bottom указывает с какой высоты начинать строить тех кто не выжил

plt.title('Выживаемость пассажиров Титаника')
plt.xlabel('Класс')
plt.ylabel('Проценты, сначало выжившие')

plt.show()