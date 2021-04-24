%matplotlib inline
import numpy as np
import math

k, n = 0, 50
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)

x = a + b + c + d

for i in range(0, n):
    if x[i] == 2:
        k = k + 1

answer = (1/2**n) * (math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

print(f'Количество выпадения двух 1 подрят = {k}, выборка составила из {n} попыток в 4 испытаниях, процентное соотношение выпадения подряд двух 1 к общему числу выборки составила {k/n}')
print(f'Вероятность выпадения двух 1 подрят составила: {answer}')




%matplotlib inline
import numpy as np
import itertools

for p in itertools.permutations("012345", 3):
    print(''.join(str(x) for x in p))

for p in itertools.permutations("012345", 6):
    print(''.join(p))

for p in itertools.product("0123", repeat=4):
    print(''.join(p))




