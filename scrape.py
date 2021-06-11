import pandas as pd
import requests
from bs4 import BeautifulSoup

def about_coconala(to_csv=True,read_csv=None):
    init = pd.read_csv(read_csv)

    df = pd.DataFrame(columns={'案件名',""})
    links = ["https://coconala.com/requests/categories/11?categoryId=11&recruiting=true&page=",
            "https://coconala.com/requests/categories/22?categoryId=22&recruiting=true&page="]
    old_size = 0
    for link in links:
        repetition = 1
        while True:
            urlName = link+str(repetition)
            headers = {
                  "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
            }
            soup = BeautifulSoup(requests.get(urlName, headers = headers).content, 'html.parser')

            content = soup.select('.c-searchItem')
            if len(content) == 0:
                old_size=len(df)
                break
            for i in range(len(content)):
                title_content = content[i].select('.c-itemInfo_title')[0].a.string
                title_link = content[i].select('.c-itemInfo_title')[0].a.get("href")
                title_content = title_content.replace('\n','');title_content = title_content.replace('　','')
                title_elems = title_content.split()
                title = ""
                for k in range(len(title_elems)):
                    title += title_elems[k]
                title = title.replace('\u216f', '-')

                min_price = content[i].select('.c-itemTileContent')[0].div.span.string
                min_price = min_price.replace('\n','');min_price=min_price.replace('　','')
                min_price = min_price.replace('\u216f', '-')
                try:
                    max_price = content[i].select('.c-itemTileContent')[0].div.select('.c-itemTileLine_budget')[1].span.string
                    max_price = max_price.replace('\n','');max_price=max_price.replace('　','')
                    max_price = max_price.replace('\u216f', '-')
                    price = min_price+'~'+max_price
                    price_elems = price.split()
                    price = price_elems[0]+price_elems[1]+price_elems[2]
                except IndexError:
                    price = min_price

                df.loc[i+old_size,'案件名'] = title
                df.loc[i+old_size,'価格'] = price
                df.loc[i+old_size,'Link'] = title_link


                #dx=dx.append(df)
            repetition += 1

    df = df.dropna(how='all').dropna(how='all', axis=1)

    if to_csv:
        df.to_csv("init.csv",index=False)

    k = 0
    new_source = pd.DataFrame()
    for j in range(len(df)):
        judge=True
        for i in range(len(init)):
            if df.loc[j,'案件名'] == init.loc[i,'案件名']:
                judge = False
        if judge == True:
            new_source.loc[k,'案件名'] = df.loc[j,'案件名']
            new_source.loc[k,'価格'] = df.loc[j,'価格']
            new_source.loc[k,'Link'] = df.loc[j,'Link']
            k += 1

    return new_source
