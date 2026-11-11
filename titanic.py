import pandas as pd
import csv



# # Запись в файл .parquet (по умолчанию используется сжатие snappy)
# df.to_parquet('data.parquet', engine='pyarrow', index=False)

# Чтение из файла .parquet
titanic_loaded = pd.read_parquet('titanic.parquet', engine='auto')
# print(titanic_loaded)

outfile = open('titanic.csv', 'w')



writer = csv.writer(outfile, delimiter=';', quotechar='"')
writer.writerows(titanic_loaded)


print(outfile)


outfile.close()