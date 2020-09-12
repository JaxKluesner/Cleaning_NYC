import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

memento_chance = np.random.binomial(30, 0.06, size=10000)
plt.hist(memento_chance, range=(0,10), bins=10)
plt.xlabel('Memento triggers')
plt.ylabel('Runs')
plt.title('Farming Simulator')
plt.show()
mem_avg = np.mean(memento_chance)
mem_0 = np.count_nonzero(memento_chance == 0)
mem_1 = np.count_nonzero(memento_chance == 1)
mem_greater_1 = np.count_nonzero(memento_chance > 1)
print("Runs with 0 triggers " + str(mem_0))
print("Runs with 1 triggers " + str(mem_1))
print("Runs with >1 triggers " + str(mem_greater_1))
print(mem_0 / 10000)
