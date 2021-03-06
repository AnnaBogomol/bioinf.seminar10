import pandas as pd
import numpy as np
from scipy.stats import t, norm
import seaborn as sns
import matplotlib.pyplot as plt

rv1 = t(3) # Распределение Стьюдента с 3мя степенями свободы
rv2 = norm(0, 1) # Нормальное распределение

# Создали датафреймы для независимых величин 5ти размеров:
df1 = pd.DataFrame({'Sample': rv1.rvs(size=2), 'Distr': 't(3)'})
df2 = pd.DataFrame({'Sample': rv1.rvs(size=5), 'Distr': 't(3)'})
df3 = pd.DataFrame({'Sample': rv1.rvs(size=14), 'Distr': 't(3)'})
df4 = pd.DataFrame({'Sample': rv1.rvs(size=100), 'Distr': 't(3)'})
df5 = pd.DataFrame({'Sample': rv1.rvs(size=1000), 'Distr': 't(3)'})

# Нарисовали гистограмму + график плотности для каждого датафрейма:
sns.histplot(data=df1, x='Sample', stat='density') # сама гистограмма
df_1 = pd.DataFrame({'x': np.linspace(-5, 5, 1000)}) # границы графика плотности и количество точек на графике
df_1['PDF'] = rv2.pdf(df_1['x']) # посчитали функцию плотности распределения в каждой точке df_1
sns.lineplot(data=df_1, x='x', y='PDF') # сам график плотности
plt.tight_layout()
plt.savefig('test11.pdf')

sns.histplot(data=df2, x='Sample', stat='density')
df_2 = pd.DataFrame({'x': np.linspace(-5, 5, 1000)})
df_2['PDF'] = rv2.pdf(df_2['x'])
sns.lineplot(data=df_2, x='x', y='PDF')
plt.tight_layout()
plt.savefig('test12.pdf')

sns.histplot(data=df3, x='Sample', stat='density')
df_3 = pd.DataFrame({'x': np.linspace(-5, 5, 1000)})
df_3['PDF'] = rv2.pdf(df_3['x'])
sns.lineplot(data=df_3, x='x', y='PDF')
plt.xlim(-5, 5) # дополнительно ограничили ось Х
plt.tight_layout()
plt.savefig('test13.pdf')

sns.histplot(data=df4, x='Sample', stat='density')
df_4 = pd.DataFrame({'x': np.linspace(-5, 5, 1000)})
df_4['PDF'] = rv2.pdf(df_4['x'])
sns.lineplot(data=df_4, x='x', y='PDF')
plt.xlim(-5, 5)
plt.tight_layout()
plt.savefig('test14.pdf')

sns.histplot(data=df5, x='Sample', stat='density')
df_5 = pd.DataFrame({'x': np.linspace(-5, 5, 1000)})
df_5['PDF'] = rv2.pdf(df_5['x'])
sns.lineplot(data=df_5, x='x', y='PDF')
plt.xlim(-5, 5)
plt.tight_layout()
plt.savefig('test15.pdf')
