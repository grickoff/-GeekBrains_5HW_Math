% matplotlib
inline
import numpy as np
import math
import matplotlib.pyplot as plt

n = 100
r = 0.7
x = np.random.rand(n)
y = r * x + (1 - r) * np.random.rand(n)

plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x) * np.sum(y) - n * np.sum(x * y)) / (np.sum(x) * np.sum(x) - n * np.sum(x * y))
b = (np.sum(y) - a * np.sum(x)) / n

print(a, b)
plt.plot([0, 1], [b, a + b])

plt.show()

# далее я пытался вычислить R по формуле (как сказано в видеоуроке)Б но почему то постоянно на первых множителях выходит ноль.
# я уже всю формулу по действию разобрал в поиске ошибки. но все равно не могу понять - что не так

x_s = np.sum(x) / 100
y_s = np.sum(y) / 100

first_up = []
second_up = []

for i in x:
    first_up.append(int(i - x_s))
first_up = np.sum(first_up)

for i in y:
    second_up.append(int(i - x_s))

    second_up = np.sum(second_up)

up = first_up * second_up
down = sqrt((first_up ** 2) * (second_up ** 2))

R = up / down
print(R)
