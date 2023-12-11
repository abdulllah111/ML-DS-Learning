import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#   Numpy


# print("\nДанные из файла:")
data = np.loadtxt('data.csv', delimiter=',', dtype=np.int64)

# print(data)
# print(data.shape)
# print(data.dtype)
# print(data.ndim)

# print("\nДанные из списка:")
# data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# print(data)
# print(data.shape)
# print(data.dtype)
# print(data.ndim)



#Pandas

s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

# print(s)
# print(s[(s > 3) & (s < 8)])

data = {
    'Name': ['Маша', 'Вася', 'Коля'],
    'Age': [25, 26, 27],
    'Job': ['Programmer', 'Business', 'Stomatolog']
}
df = pd.DataFrame(data)
# print(df)

data = {
    'Age': {'Маша':25, 'Вася':26, 'Коля':27},
    'Job': {'Маша':'Programmer', 'Вася':'Business', 'Коля':'Stomatolog'},   
}

df = pd.DataFrame(data)

# print(df)


df = pd.read_csv('ComputerRepairing.csv', sep=',')

# print(df)

df["isNum"] = df["price"].apply(lambda x: x.isnumeric())

# является ли элемент колонки "Цена в рублях" числом
df["price"] = df["price"].apply(lambda x: x.isnumeric() and int(x) or 0)

# print(df[df.isNum == True]['price'])

# print(df)

# df["price"].plot.hist()


#   Matplotlib

plt.style.use('bmh')
print(plt.style.available)
# fig, ax = plt.subplots(figsize=(10, 5))

df = pd.read_csv('titanic/sample_data.csv', sep=',')
# df['Age'].plot.hist()

# ax.pie(df['Age'].value_counts(), labels=df['Age'].value_counts().index, autopct='%1.1f%%')
# print(df)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

X = np.arange(-5, 10, 0.05)
Y = np.arange(-5, 10, 0.05)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')



plt.show()


