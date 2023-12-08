import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'''
Загрузить данные о продажах (Excel, CSV).

Посчитать основные статистики по продажам в разрезе регионов и продуктов:
    Сумма продаж
    Среднее значение продаж
    Минимальные и максимальные продажи
    Медиана
    Стандартное отклонение

Построить графики продаж по месяцам и категориям.
'''


data = pd.read_csv("test/sales.csv")

# Сумма продаж по регионам
region_sum = data.groupby(['Region']).sum()['Total Profit']

# Сумма продаж по товарам
product_sum = data.groupby(['Item Type']).sum()['Total Profit']


# Среднее значение столбца Total Prifit по регионам
region_mean = data.groupby(['Region'])['Total Profit'].mean()

# Среднее значение столбца Total Prifit по регионам
pruduct_mean = data.groupby(['Item Type'])['Total Profit'].mean()


# Минимальные продажи по региону
region_min = data.groupby(['Region'])['Total Profit'].min()

# Минимальные продажи по продукту
product_min = data.groupby(['Item Type'])['Total Profit'].min()


# Максимальные продажи региону
region_max = data.groupby(['Region'])['Total Profit'].max()

# Максимальные продажи продукту
product_max = data.groupby(['Item Type'])['Total Profit'].max()


# Медиана продаж по региону
region_median = data.groupby(['Region'])['Total Profit'].median()

# Медиана продаж по продуктуы
product_median = data.groupby(['Item Type'])['Total Profit'].median()


# Стандартное отклонение по региону
region_std = data.groupby(['Region'])['Total Profit'].std()

# Стандартное отклонение по продукту
product_std = data.groupby(['Item Type'])['Total Profit'].std()


# Форматировать дату
data['Order Date'] = pd.to_datetime(data['Order Date'])


# Графики по агрегации продаж по месяцам
plt.subplot (2, 1, 1)
grafic_month_mean = data.groupby(data['Order Date'].dt.month)['Total Profit'].mean().plot( marker='o', xlim=[1, 12], xticks=np.arange(1, 13, 1), grid=True)


# Получить количество Item Type
item_types_count = data['Item Type'].unique().size

# Графики по агрегации продаж по товарам
plt.subplot (2, 1, 2)
grafic_product_mean = data.groupby(['Item Type'])['Total Profit'].mean().plot( xlim=[1, item_types_count], xticks=np.arange(1, item_types_count, 1), marker='o', grid=True)

plt.show()