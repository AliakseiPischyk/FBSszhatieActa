import os
import pandas as pd
from functions import *


nakladnaya = pd.read_excel('nakladnaya.xlsx', engine='openpyxl')
nakladnaya = nakladnaya.drop(range(0,44),axis=0)
nakladnaya = nakladnaya.dropna(axis=1, how='all')
nakladnaya = nakladnaya.fillna(axis=0, value='0')
nakladnaya.columns = list(nakladnaya.iloc[1])
nakladnaya['Единица измерения'] = nakladnaya['Единица измерения'].astype(str)
nakladnaya = nakladnaya[nakladnaya['Единица измерения'].str.contains("шт.")]
nakladnaya['Масса груза'] = nakladnaya['Масса груза'].astype(str)
nakladnaya['Масса груза'] = nakladnaya['Масса груза'].str.replace(',','.')
nakladnaya['Масса груза'] = nakladnaya['Масса груза'].astype(float)
nakladnaya.loc[nakladnaya['Масса груза'] > 25.0, 'Масса груза'] = 999999
nakladnaya['Примечание'] = nakladnaya['Примечание'].apply(lambda x: x.split('/')[0].strip())


def replicate_rows_n_times(row):
    n = row['Колич ество']
    a = [row] * n
    c = pd.DataFrame(a)
    idx = c.index.values.astype(int)[0]

    c['Колич ество'] = 1
    c['Стоимость, руб. коп'] = c['Цена, руб. коп.']
    c['Стоимость с НДС, руб. коп.'] = c['Стоимость, руб. коп']
    c['Масса груза'] = c['Масса груза']/n
    for i in range(0,n):
        nakladnaya.loc[idx + 0.000001*i] =c.iloc[i]


nakladnaya[nakladnaya['Колич ество']>1].apply(lambda row: replicate_rows_n_times(row), axis=1)
nakladnaya.sort_index(inplace=True)
nakladnaya.reset_index(inplace=True, drop=True)
nakladnaya = nakladnaya[['Наименование товара', 'Колич ество','Цена, руб. коп.','Масса груза','Примечание']]
nakladnaya.rename(columns={'Наименование товара':'Наименование приложение','Колич ество':'Количество','Примечание':'Номер отправления'},inplace=True)

prefixed_postings = [filename for filename in os.listdir('.') if filename.startswith("postings")]
postings = pd.read_csv(prefixed_postings[0], sep=';')
postings = postings[['Номер отправления','Наименование товара','Артикул']]
postings.rename(columns = {'Наименование товара':'Наименование полное'})

def rename_postings_if_it_has_different_goods(row):
    nomer = row['Номер отправления']
    if postings['Номер отправления'].value_counts()[nomer] > 1:
        condition = (postings['Номер отправления'] == nomer) #& (postings['Наименование товара'] == row['Наименование товара'])
        print(postings[condition]['Наименование товара'].value_counts())
        print(nomer)
        if len(postings[condition]['Наименование товара'].value_counts()) > 1:
            postings.loc[condition, 'Наименование товара'] = 'ДУБЛЬ ОТПРАВЛЕНИЯ'


postings.apply(lambda row: rename_postings_if_it_has_different_goods(row), axis=1)

nakladnaya_full = nakladnaya.merge(postings,on='Номер отправления',how='left')
nakladnaya_full.fillna('ошибка',inplace=True)

try_download_seller_products_from_ozon()
prefixed = [filename for filename in os.listdir('.') if filename.startswith("seller_products")]
all_goods = pd.read_csv(prefixed[0], sep=';')
all_goods.rename(columns={'Barcode': 'Штрихкод'}, inplace=True)
all_goods = all_goods.sort_values(by='Артикул')
all_goods['Артикул'] = all_goods['Артикул'].apply(lambda x: (x[1:]))

all_goods = all_goods[['Артикул', 'Штрихкод', 'Наименование товара']]
all_goods.rename(columns={'Наименование товара': 'Наименование'}, inplace=True)

act=pd.DataFrame()
act['Наименование'] = nakladnaya_full['Наименование товара']
act['Сжато'] = nakladnaya_full['Количество']
act['Отправление'] = nakladnaya_full['Номер отправления']
act['Стоимость, руб.'] = nakladnaya_full['Цена, руб. коп.'].str.replace(',','.').astype(float)
act['Вес, кг'] = nakladnaya_full['Масса груза']
#act = pd.read_excel('Act.xlsx', engine='openpyxl')
#act.rename(columns={'Тип': 'Сжато'}, inplace=True)
#act['Сжато'] = 1
act['Комментарий'] = ''

act['Отправление'] = act['Отправление'].transform(lambda x: x + ' \n')
act = act.groupby(['Наименование']).agg(
    {'Сжато': 'sum', 'Отправление': 'sum', 'Стоимость, руб.': 'sum', 'Вес, кг': 'sum'}).reset_index()
act = act.merge(all_goods, on='Наименование', how='left')
act = df_column_switch(act, 'Штрихкод', 'Артикул')

act.insert(2, 'Шт в арт.', 0)
act.insert(3, 'Итого', act['Сжато'] * act['Шт в арт.'])
act['Артикул'] = act['Артикул'].fillna('ошибка')
act = act.apply(lambda x: fill_wtuk(x), axis=1)
act['Итого'] = act['Сжато'] * act['Шт в арт.']

act['Наименование'] = act['Наименование'].transform(lambda x: x + ' \n')
act['Сжато'] = act['Сжато'].transform(lambda x: str(x) + ' \n')
act['Шт в арт.'] = act['Шт в арт.'].transform(lambda x: str(x) + ' \n')
act['Штрихкод'] = act['Штрихкод'].transform(lambda x: str(x) + ' \n')
act = act.groupby('Артикул').agg({'Наименование': 'sum', 'Сжато': 'sum', 'Шт в арт.': 'sum', 'Итого': 'sum',
                                  'Отправление': 'sum', 'Стоимость, руб.': 'sum', 'Вес, кг': 'sum',
                                  'Штрихкод': 'sum'}).reset_index()


act = act.apply(lambda x: strip_spaces(x), axis=1)
act = act.sort_values(by='Наименование')

nomenklatura = pd.ExcelFile('Номенклатура - ТОВАРЫ.XLSX', engine='openpyxl')
nomenklatura_alpk = pd.read_excel(nomenklatura, 'АЛЬПАКА')
nomenklatura_vvp = pd.read_excel(nomenklatura, 'ВВП')
nomenklatura_unk = pd.read_excel(nomenklatura, 'УНК')
nomenklatura_trbt = pd.read_excel(nomenklatura, 'ТРБТ')
nomenklatura_tetkom = pd.read_excel(nomenklatura, 'ТЕТКОМ')
nomenklatura_zoom = pd.read_excel(nomenklatura, 'ЗООМ')
nomenklatura_hntr = pd.read_excel(nomenklatura, 'ХНТР')
nomenklatura_tian = pd.read_excel(nomenklatura, 'ТИАН')
nomenklatura_all = pd.concat(
    [nomenklatura_alpk, nomenklatura_vvp, nomenklatura_unk, nomenklatura_trbt, nomenklatura_tetkom, nomenklatura_zoom,
     nomenklatura_hntr, nomenklatura_tian])
nomenklatura_all.drop(columns=['Штрихкод', 'Наименование товара', 'Комментарий'], axis=1, inplace=True)
#nomenklatura_all['Артикул'] = nomenklatura_all['Артикул'].fillna('ошибка')
nomenklatura_all['Артикул'] = nomenklatura_all['Артикул'].fillna('пустая строка')


nomenklatura_all = nomenklatura_all.apply(lambda x: delete_wtuk(x), axis=1)
act = nomenklatura_all.merge(act, on='Артикул', how='right')
act = act.sort_values(by='Наименование')

with pd.ExcelWriter('final.xlsx', engine='xlsxwriter') as writer:
    act.to_excel(writer, sheet_name='Sheet1', index=False)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    cell_format = workbook.add_format({'text_wrap': True})
    worksheet.set_column('A:Z', cell_format=cell_format)
