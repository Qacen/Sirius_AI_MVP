import json
import random
import time
from bs4 import BeautifulSoup
import requests

def parser():
    data = []
    districts =['Тверской', 'Кунцево', 'Якиманка', 'Хорошевский', 'Даниловский', 'Басманный', 'Нагатинский затон', 'Южное Тушино', 'Хорошево-Мневники', 'Марьина роща', 'Московский', 'Пресненский', 'Щукино', 'Савеловский', 'Хамовники', 'Мещанский', '', 'Дорогомилово', 'Аэропорт', 'Филевский парк', 'Коптево', 'Арбат', 'Лефортово', 'Раменки', 'Очаково-Матвеевское', 'Марьино', 'Замоскворечье', 'Обручевский', 'Нагатино-Садовники', 'Таганский', 'Преображенское', 'Войковский', 'Покровское-Стрешнево', 'Ховрино', 'Беговой', 'Вешняки', 'Западное Дегунино', 'Марфино', 'Черемушки', 'Южное Бутово', 'Ростокино', 'Солнцево', 'Москворечье-Сабурово', 'Дмитровский', 'Ивановское', 'Чертаново Южное', 'Северное Тушино', 'Бибирево', 'Головинский', 'Орехово-Борисово Южное', 'Левобережный', 'Печатники', 'Рязанский', 'Перово', 'Южнопортовый', 'Чертаново Центральное', 'Некрасовка', 'Красносельский', 'Братеево', 'пос. Коммунарка', 'Нижегородский', 'Гагаринский', 'Свиблово', 'Останкинский', 'Отрадное', 'Алтуфьевский', 'Богородское', 'Ясенево', 'Соколиная гора', 'Фили-Давыдково', 'Алексеевский', 'Косино-Ухтомский', 'Гольяново', 'Сокол', 'Люблино', 'Донской', 'Восточное Дегунино', 'Выхино-Жулебино', 'Проспект Вернадского', 'Тропарево-Никулино', 'Коньково', 'Академический', 'Ярославский', 'Северное Бутово', 'Метрогородок', 'Зюзино', 'Сосенское поселение', 'Кузьминки', 'Капотня', 'Молжаниновский', 'Измайлово', 'Десеновское поселение', 'Кокошкино дп', 'Орехово-Борисово Северное', 'Бирюлево Восточное', 'Ново-Переделкино', 'Внуковское поселение', 'Южное Медведково', 'Бирюлево Западное', 'Митино', 'мкр. Град Московский', 'Можайский', 'Строгино', 'Лосиноостровский', 'Текстильщики', 'Северное Измайлово', 'Ломоносовский', 'Нагорный', 'Сокольники', 'Крылатское', 'Новофедоровское поселение', 'Новая Москва', 'Троицк', 'Восточное Измайлово', 'Тимирязевский', 'Крюково', 'Старое Крюково', 'Северный', 'Северное Медведково', 'Царицыно', 'Андерсен ЖК', 'Котловка', 'Семейный вариант в е Аэропорт4-комн. квартира', 'Клубный дом в е Чистых прудов4-комн. квартира', 'Новогиреево', 'Теплый Стан', 'Бутырский', 'Куркино', 'Видовая кв-ра в е Золотой мили3-комн. квартира', 'Уютная кв-ра в е Цветного б-ра3-комн. квартира', 'Фасадный дом в е Замоскворечья3-комн. квартира', 'Внуково', 'Зябликово', 'Чертаново Северное', 'Новокосино', 'Бабушкинский', 'Бескудниковский']
    with open('dataset2.csv' ,'r' ,encoding='utf-8') as f:
        strs = f.readlines()
    for i in range(700, len(strs)):
        data.append(strs[i].split(';'))
    for i in data:
        offerId = i[2].split('/')[-2]
        print(offerId)
        response = send_request(offerId)
        print(response.status_code)
        if response.status_code != 200:
            time.sleep(random.randint(7,8))
            response = send_request(offerId)
            if (response.status_code != 200): continue
        soup = BeautifulSoup(response.text, 'lxml')
        jsn = json.loads(soup.text)
        try:
            dist_num = len(districts)+1
            for j in range(0,len(districts)):
                if districts[j] == i[11]:
                    dist_num = j+1;
            if (dist_num == len(districts)+1):
                districts.append(i[11])
            str1 = (str(i[6]) +',' +str(i[7]) +',' +str(i[8]) +',' +str(i[9]) +',' +str(dist_num) +',' + str(jsn['graphs'][0]["priceEstimations"][1]['price'] ) +"\n")
            with open('datasetcorrect2.csv', 'a' ,encoding='utf-8') as f:
                f.write(str1)
                print('complite: ' + str1)
        except Exception as ex:
               print("err:  "+ str(offerId))
        time.sleep(random.randint(6 ,8))
def send_request(offerId):
    cookies = {
        '_CIAN_GK': 'd6b3a172-34e0-4268-8157-920007396e57',
        '_gcl_au': '1.1.1211339742.1709361553',
        'tmr_lvid': 'bf4c0333259ff6c53b3e9888bbc4809d',
        'tmr_lvidTS': '1709361553312',
        'uxfb_usertype': 'searcher',
        '_ym_uid': '1709361556506395436',
        '_ym_d': '1709361556',
        'uxs_uid': '96bf5b80-d85f-11ee-9b75-173edf39ed3d',
        'adrcid': 'AMflC_R4Mzy8BlAmM-jTJUQ',
        'AF_SYNC': '1709361557488',
        'afUserId': '6cac59bb-4283-4120-be91-bf6ef75a5543-p',
        '_gid': 'GA1.2.2127652753.1709602893',
        'sopr_utm': '%7B%22utm_source%22%3A+%22colab.research.google.com%22%2C+%22utm_medium%22%3A+%22referral%22%7D',
        '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"1000252B"}',
        'transport-accessibility_onboarding_counter': '1',
        '_ga_L109H0KCP9': 'GS1.1.1709623191.3.0.1709623191.0.0.0',
        'login_mro_popup': '1',
        'sopr_session': '8285ca3afea24fbd',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
        '__cf_bm': '0v2KsVBuSy7wek_8jXoWuN02yByxLX3WEJR9bP1dKzo-1709781849-1.0.1.1-aaMvTSsCCmT_mEqRS7rixut0P0PdzJ.A4uJtpuSNvK9YMnBMe1mfNlpk0sCF.pnnyZNUlYaNeSxnNJgE7vT3dg',
        '_ga': 'GA1.2.44260033.1709361555',
        '_ga_3369S417EL': 'GS1.1.1709780590.11.1.1709782403.60.0.0',
    }
    headers = {
        'authority': 'api.cian.ru',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9',
        # 'cookie': '_CIAN_GK=d6b3a172-34e0-4268-8157-920007396e57; _gcl_au=1.1.1211339742.1709361553; tmr_lvid=bf4c0333259ff6c53b3e9888bbc4809d; tmr_lvidTS=1709361553312; uxfb_usertype=searcher; _ym_uid=1709361556506395436; _ym_d=1709361556; uxs_uid=96bf5b80-d85f-11ee-9b75-173edf39ed3d; adrcid=AMflC_R4Mzy8BlAmM-jTJUQ; AF_SYNC=1709361557488; afUserId=6cac59bb-4283-4120-be91-bf6ef75a5543-p; _gid=GA1.2.2127652753.1709602893; sopr_utm=%7B%22utm_source%22%3A+%22colab.research.google.com%22%2C+%22utm_medium%22%3A+%22referral%22%7D; _gpVisits={"isFirstVisitDomain":true,"idContainer":"1000252B"}; transport-accessibility_onboarding_counter=1; _ga_L109H0KCP9=GS1.1.1709623191.3.0.1709623191.0.0.0; login_mro_popup=1; sopr_session=8285ca3afea24fbd; _ym_isad=2; _ym_visorc=b; __cf_bm=0v2KsVBuSy7wek_8jXoWuN02yByxLX3WEJR9bP1dKzo-1709781849-1.0.1.1-aaMvTSsCCmT_mEqRS7rixut0P0PdzJ.A4uJtpuSNvK9YMnBMe1mfNlpk0sCF.pnnyZNUlYaNeSxnNJgE7vT3dg; _ga=GA1.2.44260033.1709361555; _ga_3369S417EL=GS1.1.1709780590.11.1.1709782403.60.0.0',
        'if-none-match': 'W/"4346540251afa43b4ac8823a5d9e3a2d1698d893"',
        'origin': 'https://www.cian.ru',
        'referer': 'https://www.cian.ru/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
    }
    params = {
        'cianOfferId': offerId,
    }
    response = requests.get(
        'https://api.cian.ru/price-estimator/v1/get-estimation-and-trend-web/',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response
parser()

