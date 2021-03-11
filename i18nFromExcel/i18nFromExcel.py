import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
print('enter the full path + name + extention of the excel file with translation: /n')
excel_path = input('> ')
print('enter good excel tab name (space and case sensitive): /n')
tab_name = input('> ')
print('enter the column in which are the keys: /n')
key_column = input('> ')
print('enter the column in which are the transltated text: /n')
translated_column = input('> ')
print('enter the full path + name + extention of the original imported i18n.properties file: /n')
origin_prop_path = input('> ')
print('enter the full path + name + extention of the i18n file you want /n')
new_prop_path = input('> ')
excel_cols = '{0},{1}'.format(key_column, translated_column)
df_excel = pd.read_excel(excel_path, sheet_name= tab_name, index_col=None, na_values=['NA'], usecols = excel_cols, names=['key','translated'])
df_properties=pd.read_csv(origin_prop_path, sep="=", header=None, names=['key', 'original'])
df_result = pd.merge(df_properties,df_excel, on='key')
del df_result['original']
df_result.drop_duplicates(subset=['key'])
df_result.to_csv(path_or_buf=new_prop_path, sep='=', header=False, index=False)