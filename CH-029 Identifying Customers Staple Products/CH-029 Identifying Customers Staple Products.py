import pandas as pd

file_path = r'CH-029 Identifying Customers Staple Products/CH-029 Identifying Customers Staple Products.xlsx'

df = pd.read_excel(file_path,header=0,usecols='c:e')
df.columns = ['Customer ID','Product','Quantity']


filtro = df.groupby('Customer ID').apply(
    lambda x: x.groupby('Product')['Quantity'].sum().max()
).reset_index(name='max')

filtro['chave'] = filtro['Customer ID'].astype(str) + filtro['max'].astype(str)

#group_df = df.groupby('Customer ID').apply(pd.DataFrame).reset_index

group_df = df.groupby(['Customer ID','Product'])['Quantity'].sum().reset_index()
group_df['chave'] = group_df['Customer ID'].astype(str) + group_df['Quantity'].astype(str)

filter_gp = group_df.merge(filtro, left_on='chave',right_on='chave',how='inner')
#filter_gp.columns = ['chave','max']

def concatenate_values(group):
    return ','.join(group)

res = filter_gp.groupby('chave')['Product'].apply(concatenate_values)
               

print(res)
