import pandas as pd
import csv


# Чтение из файла .parquet
titanic_loaded = pd.read_parquet('titanic.parquet', engine='auto')

titanic_csv = open('titanic.csv', 'w')
writer = csv.writer(titanic_csv, delimiter=';')
writer.writerow(titanic_loaded.columns)  # Записываем названия столбцов
writer.writerows(titanic_loaded.values)   # Записываем данные
titanic_csv.close()

print(titanic_loaded)