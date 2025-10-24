import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt
print(os.getcwd())

x = range(10)
y = [i**2 for i in x]

sns.regplot(x=list(x), y=y)
plt.show()
