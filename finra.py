from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from time import sleep
import requests
from datetime import datetime


# Function returns the hashed Finra symbol label for a given ticker
def get_hidden_from_symbol(symbol):
    chromedriver_autoinstaller.install()

    options = Options()
    # options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.get('https://finra-markets.morningstar.com/MarketData/EquityOptions/detail.jsp?query=126:0P00011H0')

    sleep(2)

    search_bar = driver.find_element(By.ID, 'ms-finra-autocomplete-box')
    submit = driver.find_element(By.XPATH, '//*[@id="ms-finra-quick-search"]/input[3]')

    search_bar.send_keys(symbol)
    submit.click()

    sleep(3)

    url = driver.current_url
    firna_symbol_equivalent = url[-10::]

    return firna_symbol_equivalent


def get_short_float(symbol, debug=False):
    header = {'Host': 'finra-markets.morningstar.com',
              'Connection': 'keep-alive',
              'Accept': "*/*",
              'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/95.0.4638.69 Safari/537.36",
              'X-Requested-With': 'XMLHttpRequest',
              'Referer': "http://finra-markets.morningstar.com/MarketData/EquityOptions/detail.jsp?query=126:0P000002CH"
              }

    cookie = {
        'cookie': '__cfruid=8aa07b66d1f4bf684a119d126ce8262922895acf-1636654544; '
                  'qs_wsid=B79C33AA82B02C1674F93B217F560473; SessionID=B79C33AA82B02C1674F93B217F560473; UsrID=41151; '
                  'UsrName=FINRA.QSAPIDEF@morningstar.com; Instid=FINRA; __utmc=93401610; __utmc=153686052; '
                  'srtqs=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ'
                  '.JmRMkvOP3zIPp6O6ADWNTvSTYr4ygWZkXHWNhynkTfzVg1A2zhFNm9idSC43oI51y00NbAmrwVRzhHgAi76xaabs4DOg8ZdViLC'
                  'CElqB_dypVIo0ThrhnzyOcu2Eml5ejW12i4MOuTk64FTDNEa3Xyc44o-SKEQGuntB-lOTooo.5-xa9T7JALdWroDg.Vt3ulb3hZF'
                  'l_PQ9488IxoI2L7rHhtYcWH1BqJzDn707EUeVjK0plQReDMGAqd0SAIUSo7foee4pUoa5Jv5hNuXt6dPr59Wx0QFx63jKLqtGHwz'
                  'JWRQJ29cUAcORvoo2nms0-qkttzQhEzLwGUUYL1L-lSM5yllQ7DOpErVZUDULxCEx9_sbv9C_YEmWFK0Pr5S0sVSQkMSgTl1YgdF'
                  '7dEiraXA.Xbm3BjN0Wi4_-peQbi2LAA; srtqsv2=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.xIDQnBpGyAdi'
                  'O_mAzBAZmsAUGBz_hgYookD8B38apzTrFai-jMCRCJ9WoOby0V7Bx6TUm-Ra5lkK2pkUltvqgjgklb8wbbbYJCZafzv01t97tNtA'
                  'P81JW-c1GO-ZLJq1hR47GEX_R1aHlCiSIak2soLX4hBbA4VLTvh_Vj3503Q.wLPZmK0eWyJU3j3f.kYnFsziZJfotn1UeJ2frZVW'
                  'tP5BxEZgO9vDKBvt3fAKnadfCGU339RGpD649lWUDihCRq4MlghIkTrKoADrYNJobuSXxjA4EAPhOVxhK39wmQErkmLa9CHO5Rlz'
                  '9SPieo9t_lSj_GJF3374orWA4MPiCOc8LBG8Vh2LabEZ7KwIjWODSyuf8SkIobbEz0O60FZ943yxUcj1LGpGw5qtrs__1315-c8m'
                  'KXJgpnkpZWmmn.Ph7tkP0oKgyxovclASRWKA; __utma=93401610.914503283.1636654544.1636658438.1636666271.3; '
                  '__utmz=93401610.1636666271.3.3.utmcsr=finra-markets.morningstar.com|utmccn=(referral)|utmcmd=referra'
                  'l|utmcct=/MarketData/EquityOptions/detail.jsp; __utmt=1; __utmb=93401610.1.10.1636666271; __utma=153'
                  '686052.1841134538.1636654748.1636658438.1636666271.3; __utmz=153686052.1636666271.3.3.utmcsr=finra-m'
                  'arkets.morningstar.com|utmccn=(referral)|utmcmd=referral|utmcct=/MarketData/EquityOptions/detail.jsp'
                  '; __utmt_MM=1; __utmb=153686052.1.10.1636666271'}

    new_cookie = {
        'cookie': "__cfruid=54396992864d4570c1ddde33ac48f4a1eede5221-1638725002; "
                  "qs_wsid=974C5473B3C60E93F7D7D2A88FEA601B; SessionID=974C5473B3C60E93F7D7D2A88FEA601B; UsrID=41151; "
                  "UsrName=FINRA.QSAPIDEF@morningstar.com; Instid=FINRA; "
                  "__utma=93401610.1627271649.1638725003.1638725003.1638725003.1; __utmc=93401610; "
                  "__utmz=93401610.1638725003.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; "
                  "__utmt_MM=1; srtqs=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.18jTiEYHVmGYNwBFwfnZ2hX1vDa"
                  "-WA0f88aj-f65JbtzJFak3b8qSvZlhu9"
                  "-hk9lOeuAQl5GUut9E3vbVjARBzZgSyg_R5Mu0eZbKehyDSlBKYzMBQVDxcQ3rZVE1pIjp85psupDZjsziihox5MnQoUOrdOdqzKbAxSAbEkyTh4.t0keFPoQNmXI1kCw.lX_Joy3-PWqprblXpSfEf0kJ-FN8oBXbrIZLs4Ga8v1q8nfEd0c9GN05qgaHjbcnnTs2x89r56f33It6PU3PZs-TPPTpenffxnUhEt3wDk3gIRUE0ZNqsvZaXl8O6ng74IaGzA_Mw5gB8SG89oXh1I3yX4RYXeIs3-j9qxOdnbN80JXDaUcNY-fCcYvosvEGwOv1Xpbwh7ytmPgdiK0GMQM_rg.L8POrQaYyw8CsC0DwtGqfQ; srtqsv2=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.mlu1fMKLAnnqGRqcs3kMJQjUsC7IZW8vANsRc80s_-zLRDOxBJrVkY3NdsHyn4BFqWld76RKyIlokratJUyuCUnTjQlSvrmU0QfHZv7IaHXBBhx9A0LWABQOxTUAUSO8MGR3Mlj7lvDwfd6XDTsweVEHj1Ip3WptaFEIU46YD1s.jM6TZlFfqILucxU9.ajR1UQsAfM_qqKc2MI0qa7o2E4I3k52CXEZ8H3QONuXmaTnkTeTVB5aDkPs9rKBOf-ov-swBA39wIeNJLIUrmSKazy9jPfOyCo5huqINpnOLKj6LpgSQ94tk7XvLOe42Kwt6XyR6WcqK0WXfsIMvkYLWBPyeltaA6beQmgaxKYYpx7zjKA4LC1eXJ_LOAYsXqh1_q-fP0zzC8KsBNL6a7j_1Cv1J4X9gPsyiqh_LuGwx.lJ3CaMVN841rtkUzg6L9sw; __utmb=93401610.4.10.1638725003"}

    base_short_interest_url = f'http://finra-markets.morningstar.com/ra/snChartData?instid=FINRA&sdkver=2.61.2' \
                              f'&accessToken=undefined' \
                              f'&productType=sdk&cdt=3&country=USA&ed=20211111&f=d&fields=STA0C&hasPreviousClose=true' \
                              f'&ipoDates' \
                              f'=20020213&pids={symbol}&sd=20110101&tickers={symbol}&_=1636666270769 '

    base_pe_url = f'https://finra-markets.morningstar.com/ra/snChartData?instid=FINRA&sdkver=2.62.0&accessToken' \
                  f'=undefined&productType=sdk&cdt=2&country=USA&ed=20211203&f=d&fields=HS0A2&hasPreviousClose=true' \
                  f'&ipoDates=20131218&pids=0P00011H0G&sd=20110101&tickers=0P00011H0G&_=1638576168670 '

    print(base_short_interest_url)
    print(base_pe_url)

    pe_content = requests.get(base_pe_url, headers=header, cookies=new_cookie).json()
    short_interest_content = requests.get(base_short_interest_url, headers=header, cookies=new_cookie).json()

    if debug:
        print(pe_content)

    pe_dates = []
    short_interest_dates = []

    short_interest = []
    pe = []

    for entry in short_interest_content['Data'][0]['DailyData']['STA0C']:
        date_converted = datetime.strptime(entry['Date'], '%Y%m%d')
        # print(date_converted, entry['Date'], entry['Last'])
        short_interest_dates.append(date_converted)
        short_interest.append(entry['Last'])

    for entry in pe_content['Data'][0]['DailyData']['HS0A2']:
        date_converted = datetime.strptime(entry['Date'], '%Y%m%d')
        pe_dates.append(date_converted)
        pe.append(entry['Last'])

    return short_interest_dates, short_interest, pe_dates, pe


if __name__ == '__main__':
    symbol = get_hidden_from_symbol('AMC')
    get_short_float(symbol)
