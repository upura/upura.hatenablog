import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

data1 = np.random.randn(50)
data2 = 3 + np.random.randn(50)

# data1のプロット
sns.distplot(data1, axlabel="x")
sns.rugplot(data1)

# data2のプロット
sns.distplot(data2, color="y")
sns.rugplot(data2, color="y")

plt.ylabel('p(x)')
plt.show()