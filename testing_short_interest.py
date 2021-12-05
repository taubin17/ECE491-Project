import requests
from datetime import datetime


def get_short_float(symbol):

    header = {'Host': 'finra-markets.morningstar.com',
              'Connection': 'keep-alive',
              'Accept': "*/*",
              'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
              'X-Requested-With': 'XMLHttpRequest',
              'Referer': "http://finra-markets.morningstar.com/MarketData/EquityOptions/detail.jsp?query=126:0P000002CH"
              }

    cookie = {'cookie': '__cfruid=8aa07b66d1f4bf684a119d126ce8262922895acf-1636654544; qs_wsid=B79C33AA82B02C1674F93B217F560473; SessionID=B79C33AA82B02C1674F93B217F560473; UsrID=41151; UsrName=FINRA.QSAPIDEF@morningstar.com; Instid=FINRA; __utmc=93401610; __utmc=153686052; srtqs=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.JmRMkvOP3zIPp6O6ADWNTvSTYr4ygWZkXHWNhynkTfzVg1A2zhFNm9idSC43oI51y00NbAmrwVRzhHgAi76xaabs4DOg8ZdViLCCElqB_dypVIo0ThrhnzyOcu2Eml5ejW12i4MOuTk64FTDNEa3Xyc44o-SKEQGuntB-lOTooo.5-xa9T7JALdWroDg.Vt3ulb3hZFl_PQ9488IxoI2L7rHhtYcWH1BqJzDn707EUeVjK0plQReDMGAqd0SAIUSo7foee4pUoa5Jv5hNuXt6dPr59Wx0QFx63jKLqtGHwzJWRQJ29cUAcORvoo2nms0-qkttzQhEzLwGUUYL1L-lSM5yllQ7DOpErVZUDULxCEx9_sbv9C_YEmWFK0Pr5S0sVSQkMSgTl1YgdF7dEiraXA.Xbm3BjN0Wi4_-peQbi2LAA; srtqsv2=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.xIDQnBpGyAdiO_mAzBAZmsAUGBz_hgYookD8B38apzTrFai-jMCRCJ9WoOby0V7Bx6TUm-Ra5lkK2pkUltvqgjgklb8wbbbYJCZafzv01t97tNtAP81JW-c1GO-ZLJq1hR47GEX_R1aHlCiSIak2soLX4hBbA4VLTvh_Vj3503Q.wLPZmK0eWyJU3j3f.kYnFsziZJfotn1UeJ2frZVWtP5BxEZgO9vDKBvt3fAKnadfCGU339RGpD649lWUDihCRq4MlghIkTrKoADrYNJobuSXxjA4EAPhOVxhK39wmQErkmLa9CHO5Rlz9SPieo9t_lSj_GJF3374orWA4MPiCOc8LBG8Vh2LabEZ7KwIjWODSyuf8SkIobbEz0O60FZ943yxUcj1LGpGw5qtrs__1315-c8mKXJgpnkpZWmmn.Ph7tkP0oKgyxovclASRWKA; __utma=93401610.914503283.1636654544.1636658438.1636666271.3; __utmz=93401610.1636666271.3.3.utmcsr=finra-markets.morningstar.com|utmccn=(referral)|utmcmd=referral|utmcct=/MarketData/EquityOptions/detail.jsp; __utmt=1; __utmb=93401610.1.10.1636666271; __utma=153686052.1841134538.1636654748.1636658438.1636666271.3; __utmz=153686052.1636666271.3.3.utmcsr=finra-markets.morningstar.com|utmccn=(referral)|utmcmd=referral|utmcct=/MarketData/EquityOptions/detail.jsp; __utmt_MM=1; __utmb=153686052.1.10.1636666271'}

    gamestop_symbol = '0P000002CH'
    amc_symbol = '0P00011H0G'


    gme_url = 'http://finra-markets.morningstar.com/ra/snChartData?instid=FINRA&sdkver=2.61.2&accessToken=undefined&productType=sdk&cdt=3&country=USA&ed=20211111&f=d&fields=STA0C&hasPreviousClose=true&ipoDates=20020213&pids=0P000002CH&sd=20110101&tickers=0P000002CH&_=1636666270769'
    amc_url = f'http://finra-markets.morningstar.com/ra/snChartData?instid=FINRA&sdkver=2.61.2&accessToken=undefined&productType=sdk&cdt=3&country=USA&ed=20211111&f=d&fields=STA0C&hasPreviousClose=true&ipoDates=20020213&pids={amc_symbol}&sd=20110101&tickers={amc_symbol}&_=1636666270769'

    content = requests.get(gme_url, headers=header, cookies=cookie).json()

    # print(type(content))

    # print(content['Data'])

    # print(content['Data'][0]['DailyData']['STA0C'])
    dates = []
    percent_short_float = []

    for entry in content['Data'][0]['DailyData']['STA0C']:
        date_converted = datetime.strptime(entry['Date'], '%Y%m%d')
        print(date_converted, entry['Date'], entry['Last'])
        dates.append(date_converted)
        percent_short_float.append(entry['Last'])

    return dates, percent_short_float



if __name__ == '__main__':


    # print(r.request.headers)

    # driver.get(url)
    # sleep(5)

    # stuff = driver.page_source

    # sleep(5)
