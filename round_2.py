import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Взять набор данных с Kaggle о пассажирах Титаника. 
Проанализировать выживаемость по полу, классу каюты. 
Выявить корреляции между признаками пассажиров.
'''


data = pd.read_csv("titanic/train.csv")

# Выживаемость по полу
surv_to_sex = data.groupby('Sex')['Survived'].mean()

# Выживаемость по классу каюты
surv_to_pclass = data.groupby('Pclass')['Survived'].mean()



#Выявить корреляции между признаками пассажиров и вывести на тепловую карту

correlation = data[['Age', 'SibSp', 'Fare', 'Pclass', 'Survived']].corr(method='pearson')
print(correlation)
fig, ax = plt.subplots(figsize=(8,8))
im = ax.imshow(correlation, interpolation='nearest')
fig.colorbar(im, orientation='vertical', fraction = 0.05)

# Установить заголовки
ax.set_xticks(np.arange(len(correlation.columns)), labels=correlation.columns)
ax.set_yticks(np.arange(len(correlation.columns)), labels=correlation.columns)


# Заполнить ячейки
for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        text = ax.text(j, i, round(correlation.to_numpy()[i, j], 2),
                       ha="center", va="center", color="black")
        
plt.show()