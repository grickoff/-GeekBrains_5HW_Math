% matplotlib
inline

import numpy as np

red_list = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
number = int(np.random.uniform(0, 36))
if number == 0:
    color = "It's ZERO, MAAAAAAN"
elif number in red_list:
    color = 'red'
else:
    color = 'black'

print(number, color)