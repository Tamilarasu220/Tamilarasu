from bs4 import BeautifulSoup
import pandas as pd
import requests
import configparser
Config = configparser.ConfigParser()
Config.read("comman.ini")
# print(Config.sections())
def ConfigSectionMap(section):
    Lst_sec=[]
    options = Config.options(section)
    for option in options:
        dict1=(Config.get(section,option))
        #print(dict1)
        Lst_sec.append(dict1)
    return (Lst_sec)
Bank= ConfigSectionMap("Bank Sector")
for dict1 in Bank:
    banks_url='banks-private-sector/'
    url2=banks_url+str(dict1)
    url1="https://www.moneycontrol.com/india/stockpricequote/"
    print('++++++++'+str(dict1)+'++++++++')
    url=url1+url2
    # headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    #           'Referer': 'https://www.moneycontrol.com/india/stockpricequote/auto-lcvs-hcvs/tatamotors/TM03'}
    page = requests.get(url) #, headers=headers,verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    #BSE AND NSE
    TABLE=(soup.findAll('div',{"class":"bselft"}))
    BSE_DT= TABLE[0].find(class_="display_lastupd").get_text()
    BSE_value= TABLE[0].find(class_="pcnsb div_live_price_wrap").get_text() #class="pcnsb div_live_price_wrap"
    BSE_value1 = BSE_value.replace("\n", " ")
    # try:
    #      value1=BSE_data.find(class_="span_price_wrap stprh rdclr").get_text() #class="span_price_wrap stprh rdclr"
    # except AttributeError:
    #     value1 = BSE_data.find(class_="span_price_wrap stprh grnclr").get_text()
    TABLE0 = (soup.findAll('div', {"class": "nsert"}))
    NSE_DT = TABLE0[0].find(class_="display_lastupd").get_text()
    NSE_value = TABLE0[0].find(class_="pcnsb div_live_price_wrap").get_text()  #class="FL bsepcnm",class="span_price_wrap stprh red_hilight rdclr"
    NSE_value1=NSE_value.replace("\n", " ")
    # if((NSE_DATA.find(class_="span_price_wrap stpr red_hilight rdclr"))==(NSE_DATA.find(class_="span_price_wrap stpr red_hilight rdclr"))):
    #     value2 = NSE_DATA.find(class_="span_price_wrap stpr red_hilight rdclr").get_text()
    # else:
    #    value2 = NSE_DATA.find(class_="span_price_wrap stprh grnclr").get_text() #class="span_price_wrap stprh grnclr""
    TABLE1=(soup.findAll('div',{"class":"clearfix mkt_openclosebx"})) #real data
    BSE_VALUE=TABLE1[0].find(class_ ="clearfix op_list") # class="clearfix op_list"
    BSE_PREV=BSE_VALUE.find(class_="prev_open priceprevclose").get_text()
    BSE_OPEN =BSE_VALUE.find(class_="prev_open priceopen").get_text()
    NSE_VALUE=TABLE1[1].find(class_ ="clearfix op_list")
    NSE_PREV = NSE_VALUE.find(class_="prev_open priceprevclose").get_text()
    NSE_OPEN = NSE_VALUE.find(class_="prev_open priceopen").get_text()
    # print('NSE')
    # print(NSE_VALUE)
    BSE_DATA = {'Sectors':str(dict1),
                'BSE_Date&Time': BSE_DT,
                'BSE_CURRENT_value': BSE_value1}
    BSE = { 'Sectors':str(dict1),
            'BSE_PREV_VALUE':BSE_PREV,
            'BSE_OPEN_VALUE':BSE_OPEN }
    NSE_DATA = {'Sectors':str(dict1),
                'NSE_Date&Time': NSE_DT,
                'NSE_CURRENT_value': NSE_value1}
    NSE = { 'Sectors':str(dict1),
            'NSE_PREV_VALUE':NSE_PREV,
            'NSE_OPEN_VALUE':NSE_OPEN}

    df = pd.DataFrame.from_dict(BSE_DATA,orient='index')
    Bse_Data=(df.transpose())
    print(Bse_Data)
    writer = pd.ExcelWriter("money_control.xlsx", engine='xlsxwriter')
    df = pd.DataFrame.from_dict(BSE,orient='index')
    Bse=df.transpose()
    # print(page1)
    print("++++++++++++++++++++++"*2)
    df = pd.DataFrame.from_dict(NSE_DATA,orient='index')
    Nse_Data=df.transpose()
    print(Nse_Data)
    df = pd.DataFrame.from_dict(NSE,orient='index')
    Nse=df.transpose()
    print(Nse)
    # BSE &NSE code ending
    items=soup.findAll('div',{"class":"tab-pane fade in active"}) #tab-pane fade in active, class="clearfix value_list", class="tab-pane fade in active", class="tab-pane fade in active"
    stand_alone=items[1].findAll(class_ ="value_txtfl") #class="value_txtfl", value_txtfl
    if(stand_alone==0):
        a = items[0].findAll(class_="value_txtfl")
    else:
        a=items[1].findAll(class_ ="value_txtfl")
    new_list=[]
    for i in a:
        new_list.append(i.get_text())
    b=items[1].findAll(class_ ="value_txtfr")
    new_list1 = []
    for i in b:
        new_list1.append(i.get_text())
    value={'stand_alone--'+str(dict1):new_list,
           'stand_alone_values--'+str(dict1):new_list1}
    df = pd.DataFrame.from_dict(value, orient='index')
    Stand_Alone=df.transpose()
    print(Stand_Alone)
    news = soup.findAll('div', {"class": "col_right"}) #class="clearfix marg_top30",class="announe_list"
    # News_feed=[]
    News_= news[0].find(class_="announe_list").get_text() #other_thumbtxt , clearfix, class="vid_list clearfix" , articleImg
    # for i in News_:
    #  News_feed.append(i)
    #News_feed = News_.replace("\n", " ")
    print("News_feed", News_)
    NEWS= {'News_feed':News_}
    df=pd.DataFrame.from_dict(NEWS, orient='index')
    News=df.transpose()
    # with pd.ExcelWriter('money_control.xlsx', engine="openpyxl", mode="a") as writer:
    # df.to_excel(writer, sheet_name="name", startrow=num, startcol=num)
    with pd.ExcelWriter("money_control.xlsx") as writer:
        Bse_Data.to_excel(writer,sheet_name='Bse_Data')
        Bse.to_excel(writer,sheet_name='Bse')
        Nse_Data.to_excel(writer,sheet_name='Nse_Data')
        Nse.to_excel(writer,sheet_name='Nse')
        Stand_Alone.to_excel(writer,sheet_name='Stand_Alone')
        News.to_excel(writer, sheet_name='NEWS')
        writer.save()