import time
import requests
import json
import urllib

def delete_wtuk(x):
    art = x['Артикул']
    if ' 1шт' in art:
        art = art.replace(' 1шт', ' ')
    if ' 2шт' in art:
        art = art.replace(' 2шт', ' ')
    if ' 3шт' in art:
        art = art.replace(' 3шт', ' ')
    if ' 4шт' in art:
        art = art.replace(' 4шт', ' ')
    if ' 5шт' in art:
        art = art.replace(' 5шт', ' ')
    if ' 10шт' in art:
        art = art.replace(' 10шт', ' ')
    if ' 12шт' in art:
        art = art.replace(' 12шт', ' ')
    if ' 18шт' in art:
        art = art.replace(' 18шт', ' ')
    if ' 24шт' in art:
        art = art.replace(' 24шт', ' ')
    if ' 25шт' in art:
        art = art.replace(' 25шт', ' ')
    if ' 30шт' in art:
        art = art.replace(' 30шт', ' ')
    if ' 36шт' in art:
        art = art.replace(' 36шт', ' ')
    if ' 48шт' in art:
        art = art.replace(' 48шт', ' ')
    if ' 01шт' in art:
        art = art.replace(' 01шт', ' ')
    if ' 02шт' in art:
        art = art.replace(' 02шт', ' ')
    if  '03шт' in art:
        art = art.replace(' 03шт', ' ')
    if ' 04шт' in art:
        art = art.replace(' 04шт', ' ')
    if ' 05шт' in art:
        art = art.replace(' 05шт', ' ')
    if ' 06шт' in art:
        art = art.replace(' 06шт', ' ')
    if '-01' in art:
        art = art.replace('-01', '')
    if '-02' in art:
        art = art.replace('-02', '')
    if '-04' in art:
        art = art.replace('-04', '')
    if '-06' in art:
        art = art.replace('-06', '')
    if '-12' in art:
        art = art.replace('-12', '')
    if '-18' in art:
        art = art.replace('-18', '')
    if '-24' in art:
        art = art.replace('-24', '')
    if '-30' in art:
        art = art.replace('-30', '')
    if '-32' in art:
        art = art.replace('-32', '')
    if '-36' in art:
        art = art.replace('-36', '')
    if '-48' in art:
        art = art.replace('-48', '')
    if '-64' in art:
        art = art.replace('-64', '')
    if '-11' in art:
        art = art.replace('-11', '')
    if '-22' in art:
        art = art.replace('-22', '')
    if '-16' in art:
        art = art.replace('-16', '')
    if '-32' in art:
        art = art.replace('-32', '')
    if '-1' in art:
        art = art.replace('-1', '')
    if '-2' in art:
        art = art.replace('-2', '')
    if '-3' in art:
        art = art.replace('-3', '')
    if '-4' in art:
        art = art.replace('-4', '')
    if '-5' in art:
        art = art.replace('-5', '')
    if '-6' in art:
        art = art.replace('-6', '')
    x['Артикул'] = art
    return x


def fill_wtuk(x):
    art = x['Артикул']
    if ' 48шт' in art:
        art = art.replace(' 48шт', ' ')
        x['Шт в арт.'] = 48
    if ' 36шт' in art:
        art = art.replace(' 36шт', ' ')
        x['Шт в арт.'] = 36
    if ' 30шт' in art:
        art = art.replace(' 30шт', ' ')
        x['Шт в арт.'] = 30
    if ' 25шт' in art:
        art = art.replace(' 25шт', ' ')
        x['Шт в арт.'] = 25
    if ' 24шт' in art:
        art = art.replace(' 24шт', ' ')
        x['Шт в арт.'] = 24
    if ' 18шт' in art:
        art = art.replace(' 18шт', ' ')
        x['Шт в арт.'] = 18
    if ' 10шт' in art:
        art = art.replace(' 10шт', ' ')
        x['Шт в арт.'] = 10
    if ' 12шт' in art:
        art = art.replace(' 12шт', ' ')
        x['Шт в арт.'] = 12
    if ' 1шт' in art:
        art = art.replace(' 1шт', ' ')
        x['Шт в арт.'] = 1
    if ' 2шт' in art:
        art = art.replace(' 2шт', ' ')
        x['Шт в арт.'] = 2
    if ' 3шт' in art:
        art = art.replace(' 3шт', ' ')
        x['Шт в арт.'] = 3
    if ' 4шт' in art:
        art = art.replace(' 4шт', ' ')
        x['Шт в арт.'] = 4
    if ' 5шт' in art:
        art = art.replace(' 5шт', ' ')
        x['Шт в арт.'] = 5
    if ' 01шт' in art:
        art = art.replace(' 01шт', ' ')
        x['Шт в арт.'] = 1
    if ' 02шт' in art:
        art = art.replace(' 02шт', ' ')
        x['Шт в арт.'] = 2
    if ' 03шт' in art:
        art = art.replace(' 03шт', ' ')
        x['Шт в арт.'] = 3
    if ' 04шт' in art:
        art = art.replace(' 04шт', ' ')
        x['Шт в арт.'] = 4
    if ' 05шт' in art:
        art = art.replace(' 05шт', ' ')
        x['Шт в арт.'] = 5
    if ' 06шт' in art:
        art = art.replace(' 06шт', ' ')
        x['Шт в арт.'] = 6
    if '-01' in art:
        art = art.replace('-01', '')
        x['Шт в арт.'] = 1
    if '-02' in art:
        art = art.replace('-02', '')
        x['Шт в арт.'] = 2
    if '-04' in art:
        art = art.replace('-04', '')
        x['Шт в арт.'] = 4
    if '-06' in art:
        art = art.replace('-06', '')
        x['Шт в арт.'] = 6
    if '-12' in art:
        art = art.replace('-12', '')
        x['Шт в арт.'] = 12
    if '-18' in art:
        art = art.replace('-18', '')
        x['Шт в арт.'] = 18
    if '-24' in art:
        art = art.replace('-24', '')
        x['Шт в арт.'] = 24
    if '-30' in art:
        art = art.replace('-30', '')
        x['Шт в арт.'] = 30
    if '-32' in art:
        art = art.replace('-32', '')
        x['Шт в арт.'] = 32
    if '-36' in art:
        art = art.replace('-36', '')
        x['Шт в арт.'] = 36
    if '-48' in art:
        art = art.replace('-48', '')
        x['Шт в арт.'] = 48
    if '-64' in art:
        art = art.replace('-64', '')
        x['Шт в арт.'] = 64
    if '-11' in art:
        art = art.replace('-11', '')
        x['Шт в арт.'] = 11
    if '-22' in art:
        art = art.replace('-22', '')
        x['Шт в арт.'] = 22
    if '-16' in art:
        art = art.replace('-16', '')
        x['Шт в арт.'] = 16
    if '-32' in art:
        art = art.replace('-32', '')
        x['Шт в арт.'] = 32
    if '-1' in art:
        art = art.replace('-1', '')
        x['Шт в арт.'] = 1
    if '-2' in art:
        art = art.replace('-2', '')
        x['Шт в арт.'] = 2
    if '-3' in art:
        art = art.replace('-3', '')
        x['Шт в арт.'] = 3
    if '-4' in art:
        art = art.replace('-4', '')
        x['Шт в арт.'] = 4
    if '-5' in art:
        art = art.replace('-5', '')
        x['Шт в арт.'] = 5
    if '-6' in art:
        art = art.replace('-6', '')
        x['Шт в арт.'] = 6
    x['Артикул'] = art
    return x


def try_download_seller_products_from_ozon():
    url_otchet = "https://api-seller.ozon.ru/v1/report/products/create"
    data_otchet = {
        "language": "DEFAULT",
        "offer_id": [],
        "search": "",
        "sku": [],
        "visibility": "ALL"
    }
    headers = {'Client-Id': '1642603', 'Api-Key': 'acae0dbe-e77e-4a21-ae64-6d55ac3476d8'}
    response_otchet = requests.post(url_otchet, data=json.dumps(data_otchet), headers=headers).json()
    answer = response_otchet.get("result")

    if answer is None:
        print('ВНИМАНИЕ!!! Произошла ошибка при ГЕНЕРАЦИИ товары.цсв, зовите программиста или выкачайте файл руками')
        print(response_otchet['message'])
    else:
        url_download = 'https://api-seller.ozon.ru/v1/report/info'
        data_download = {'code': answer['code']}
        tries = 0
        while 1:
            response_download = requests.post(url_download, data=json.dumps(data_download), headers=headers).json()
            answer_download = response_download.get('result')
            if answer_download is None:
                print(
                    'ВНИМАНИЕ!!! Произошла ошибка при ПОЛУЧЕНИИ ССЫЛКИ на товары.цсв, зовите программиста или '
                    'выкачайте файл руками')
                print(response_download['message'])
            elif answer_download['status'] == 'success':
                tovari_csv_url = answer_download['file']
                try:
                    urllib.request.urlretrieve(tovari_csv_url, "seller_products.csv")
                    print('Товары.цсв скачан успешно!')
                except urllib.error.HTTPError as e:
                    print(
                        'ВНИМАНИЕ!!! Произошла ошибка при СКАЧИВАНИИ товары.цсв, зовите программиста или выкачайте '
                        'файл руками')
                    print(e)
                break
            elif answer_download['status'] == 'waiting' or answer_download['status'] == 'processing':
                if tries == 10:
                    print('ВНИМАНИЕ!!! СОЗДАНИЕ товары.цсв внутри озона не получилось за 10 сек'
                          ', зовите программиста или выкачайте файл руками')
                    break
                time.sleep(2)
                tries += 1
                print('Попытка скачать товары.цсв, ждем ответ озона №' + str(tries) + '.' * tries)
            else:
                print(
                    "Непредусмотренная ошибка при получении товары.цсв от озон. Пробуйте перезапустить программу или "
                    "зовите программиста")






def df_column_switch(df, column1, column2):
    i = list(df.columns)
    a, b = i.index(column1), i.index(column2)
    i[b], i[a] = i[a], i[b]
    df = df[i]
    return df



def strip_spaces(x):
    x['Наименование'] = x['Наименование'].strip()
    x['Сжато'] = x['Сжато'].strip()
    x['Отправление'] = x['Отправление'].strip()
    x['Шт в арт.'] = x['Шт в арт.'].strip()
    x['Штрихкод'] = x['Штрихкод'].strip()
    return x