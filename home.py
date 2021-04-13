from Read import Read_St
import pandas as pd
import easygui
Fname = easygui.fileopenbox()
Transactions = Read_St(Fname)

print(Transactions)