from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

def Starbucks_store(result):
    Starbucks_URL = "https://www.starbucks.co.kr/store/store_map.do"
    a=[4043,4104,4244,3990,3968,4079,4032,3980,4024,9629,9752,9531,9521,9545,9692,9517,9598,9594,9663,9678,9309,3170]

    for i in range(len(a)):
        driver.get(Starbucks_URL)
        time.sleep(1)
        try:
            driver.execute_script("getStoreDetail(%d)" %a[i])
            time.sleep(1)
            html = driver.page_source
            bs = BeautifulSoup(html, 'html.parser')
            store_name_h6 = bs.select("header.titl > h6")[0].string.strip()
            print(store_name_h6)
            info = bs.select("dl.shopArea_info > dd")
            store_add = info[0]
            store_ph = info[1].string
            store_pk = info[4].string
            result.append([store_name_h6] + [store_add] + [store_ph] + [store_pk])
        except:
            continue
    return

def main():
    result = []
    print("원하는 스타벅스 매장 찾기")
    Starbucks_store(result)

    df = pd.DataFrame(result, columns = ('Store', 'add', 'phone', 'paking'))
    df.to_csv('./mtest_003.csv', encoding='cp949', index=True)

if __name__ == '__main__':
    main()
   


