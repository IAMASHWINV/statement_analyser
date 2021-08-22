import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb 


sb.set(rc={'figure.figsize':(11.7,8.27)})
tx = pd.read_csv('temp.csv')
ms = tx.loc[(tx.Withdraw>0) & (tx.Category =='HRR')]
ms = ms.groupby('SubCategory',as_index=False).sum()
g = sb.barplot(x='SubCategory', y="Withdraw", data=ms , ci=None)

for bar in g.patches:
    g.annotate(format(bar.get_height(), '.0f'), 
                   (bar.get_x() + bar.get_width() / 2, 
                    bar.get_height()), ha='center', va='center',
                   size=10, xytext=(0, 8),
                   textcoords='offset points')
plt.tight_layout()
plt.show()
