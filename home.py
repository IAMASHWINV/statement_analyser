from Read import Read_St
from funcs import *
import pandas as pd
from easygui import buttonbox,fileopenbox,choicebox,enterbox
import os,sys



ch = buttonbox("Select account type",'Statement Analyser' , ['New account','Existing account'])
if ch == 'New account':
    Fname = fileopenbox()
    Acn = enterbox('Enter Account name' )
    Transactions = Read_St(Fname,Acn)
else:
    files = os.listdir(os.getcwd())    
    files = list(filter(lambda f: f.endswith('.csv'), files))
    Acn = choicebox('Select account name', 'Statement Analyser', files)
    Transactions = pd.read_csv(Acn)
    ex_ch = buttonbox("Select Action",'Statement Analyser' , ['Group Transactions','Analyse'])
    if ex_ch == 'Group Transactions':
        fill_cat(Transactions,Acn)
    else:
        op = {'exit':sys.exit, 'Transactions per day':TxpDay,'Category analyis':ancat,'SubCategory analyis (pie)':Subc,'SubCategory analyis':Barp}
        while(True):
            an_ch = buttonbox("Analysis type",'Statement Analyser' , ['Transactions per day','Category analyis','SubCategory analyis (pie)','SubCategory analyis','exit'])
            op[an_ch](Transactions)
