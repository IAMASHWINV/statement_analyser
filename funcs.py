import pandas as pd
from easygui import multchoicebox,enterbox,textbox,buttonbox,choicebox
from tabulate import tabulate
import matplotlib.pyplot as plt 
import seaborn as sb 
plt.rcParams['figure.figsize'] = 11.7,8.27
def fill_cat(df,Acn):
    coln = buttonbox("Assign",'Statement Analyser' , ['Category','SubCategory','Comments'])
    msg ="Select Recepient"
    title = "Assign" + coln
    choices = sorted(df.To.unique())
    rep = multchoicebox(msg, title, choices)
    cat = enterbox('Enter ' + coln)
    df.loc[df.To.isin(rep),coln] = cat
    df.to_csv(Acn, index=False)
    redo = buttonbox("Continue Assigning",'Statement Analyser' , ['yes','no'])
    if redo == 'yes':
        fill_cat(df,Acn)
    else:
        return df
    #textbox(tabulate(df, headers='keys', tablefmt='psql'))

def TxpDay(df):
    tx = df
    ax = sb.countplot(data=tx, x='Tx_date')
    ax.set_xticklabels(ax.get_xticklabels(),rotation=45, fontweight='light',  fontsize='5')
    plt.tight_layout()
    plt.show()

def Subc(df):
    tmp = df.groupby('Category',as_index=False).sum()
    tmp = tmp.loc[tmp.Withdraw>0]
    choices = sorted(tmp.Category.unique())
    rep = choicebox('Select category',"Statement Analyser", choices)
    ms = df.loc[df.Category == rep].groupby('SubCategory')['Withdraw'].sum()
    ms = ms.loc[ms > 0]
    lab = list(ms.index)
    labels = []
    for i in lab:
        labels.append(i+ ' - ' +str(ms.loc[i]))
    sizes = list((ms/sum(ms))*100)
    patches, texts = plt.pie(sizes, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def ancat(df):
    ms = df.groupby("Category")['Withdraw'].sum()
    ms = ms.loc[ms > 0]
    labels = ms.keys()
    plt.pie(ms, labels=labels,
        autopct=lambda p: '{:.0f}'.format(p * sum(ms) / 100),
        shadow=True)
    plt.title("Expense vs category", fontsize=14)
    plt.show()


def Barp(tx):
    sb.set(rc={'figure.figsize':(11.7,8.27)})
    ms = tx.loc[tx.Withdraw>0]
    choices = sorted(ms.Category.unique())
    rep = choicebox('Select category',"Statement Analyser", choices)
    ms = ms.loc[tx.Category ==rep]
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

#Subc(pd.read_csv('temp.csv'))