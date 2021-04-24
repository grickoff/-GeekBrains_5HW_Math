%matplotlib inline
import numpy as np

x = []

for i in range(10):
    x.append(sum(np.random.rand(10)))

plt.hist(x)

plt.xlabel('Суммы')
plt.ylabel('Частота встречи')
plt.title('Гистограмма распределения суммы псевдорандомных чисел')
print(f'Суммы рандомных чисел: {x}')