import pdfplumber
import pandas as pd

def extract_inf(rem):
    rem = rem.replace("\n",'').split('/')
    info = [rem[0]] 
    try:
        info.append(rem[2])
        info.append(rem[3])
    except IndexError:
        info.append('Na')
        info.append('Na')
    return info  
        
def Read_St(Fname):
    pdf = pdfplumber.open(Fname)
    pg_objs = pdf.pages
    Transactions = []
    for Pg in pg_objs:
        Table = Pg.extract_table()
        try:
            Transaction_Pg = [x for x in Table if x[1]!=None]
        except TypeError:
            break
        Transactions.extend(Transaction_Pg)
    return clean(Transactions)

def clean(Transactions):
    title = Transactions.pop(0)
    df = pd.DataFrame(Transactions, columns =title)
    df.index = df.index+1
    df.drop(['S No.', 'Value Date', 'Cheque Number'],axis = 1,inplace=True)
    df = df.rename({'Withdrawal Amount\n(INR )': 'Withdraw', 'Deposit Amount\n(INR )': 'Deposit', 'Balance (INR )': 'Balance',
    'Transaction Remarks' : 'Remarks','Transaction Date': 'Tx date'}, axis=1)
    df['Tx date']= pd.to_datetime(df['Tx date'], format= "%d,%m,%Y")
    df = df.astype({"Withdraw": float, "Deposit": float,'Balance': float})
    df['Remarks'] = df.Remarks.apply(extract_inf)
    df[['Mode','Comments','To']] =  pd.DataFrame(df.Remarks.tolist(), index= df.index)
    df.drop(['Remarks'],inplace=True,axis=1)
    df['Category'] = df.apply(lambda _: '', axis=1)
    df.to_csv('Ashwin.csv')
    return df

