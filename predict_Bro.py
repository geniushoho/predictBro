### Location: Taiwan/Hsinchu
### Owner: Yun-Han
### Date: 20200704
### Version: v2
### Purpose: search data by date

import requests
import time
import datetime
from pandas_datareader import data as dreader
import pandas as pd

name = input('請輸入日期(如：2020-07-03): ')
date_time_str = name + ' 15:15:27.243860'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f').date()
#print(date_time_obj)
#print(type(date_time_obj))

hweektoday = date_time_obj.weekday()

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
#    print(yearb2+monthb2+dayb2)
#    print(year0+month0+day0)

    h = requests.get(url)
    time.sleep(1.5)
#    print(h.text)
#    print(len(h.text))
#    print("test")
    if len(h.text) < 650:
        time.sleep(1.5)
        print(year0+month0+day0+"@holiday")
        #print('holiday')
        return False
    return True
#    print(h.headers)
#    h = requests.head(url, allow_redirects=True)
#    print(h)
#    header = h.headers
#    print("test")
#    print(header)
#    content_type = header.get('content-type')
#    print(content_type.lower())
#    if 'Utf-8' in content_type.lower():
#        return False
#    if 'html' in content_type.lower():
#        return False
#    return True


##HO##if ((not(hweektoday != 5)) and (not(hweektoday != 6)) and (0 <= int("%d" % datetime.datetime.now().hour) < 15)):
##HO##    year0 = "2019"
##HO##    month0 = "03"
##HO##    day0 = "22"
##HO##    yearb2 = "2019"
##HO##    monthb2 = "03"
##HO##    dayb2 = "20"
##HO##elif hweektoday == 6: #如果是星期日的話
##HO##    year0 = (date_time_obj -  datetime.timedelta(days=2)).strftime("%Y")
##HO##    month0 = (date_time_obj -  datetime.timedelta(days=2)).strftime("%m")
##HO##    day0 = (date_time_obj -  datetime.timedelta(days=2)).strftime("%d")
##HO##    yearb2 = (date_time_obj -  datetime.timedelta(days=4)).strftime("%Y")
##HO##    monthb2 = (date_time_obj -  datetime.timedelta(days=4)).strftime("%m")
##HO##    dayb2 = (date_time_obj -  datetime.timedelta(days=4)).strftime("%d")
##HO##    #dtClosed = str(date_time_obj - datetime.timedelta(days = 3 ))#日期就要
##HO##elif hweektoday == 5: #如果是星期六的話
##HO##    year0 = (date_time_obj -  datetime.timedelta(days=1)).strftime("%Y")
##HO##    month0 = (date_time_obj -  datetime.timedelta(days=1)).strftime("%m")
##HO##    day0 = (date_time_obj -  datetime.timedelta(days=1)).strftime("%d")
##HO##    yearb2 = (date_time_obj -  datetime.timedelta(days=3)).strftime("%Y")
##HO##    monthb2 = (date_time_obj -  datetime.timedelta(days=3)).strftime("%m")
##HO##    dayb2 = (date_time_obj -  datetime.timedelta(days=3)).strftime("%d")
##HO###elif (hweektoday == 0) and (int("%d" % datetime.datetime.now().hour) < 15): #如果是星期1的話
##HO###    #print("ohmygod")
##HO###    year0 = (date_time_obj -  datetime.timedelta(days=3)).strftime("%Y")
##HO###    month0 = (date_time_obj -  datetime.timedelta(days=3)).strftime("%m")
##HO###    day0 = (date_time_obj -  datetime.timedelta(days=3)).strftime("%d")
##HO###    yearb2 = (date_time_obj -  datetime.timedelta(days=5)).strftime("%Y")
##HO###    monthb2 = (date_time_obj -  datetime.timedelta(days=5)).strftime("%m")
##HO###    dayb2 = (date_time_obj -  datetime.timedelta(days=5)).strftime("%d")
##HO##elif (hweektoday == 0) and (int("%d" % datetime.datetime.now().hour) >= 15): #如果是星期1的話
##HO##    #print(hweektoday == 0)
##HO##    #print(int("%d" % datetime.datetime.now().hour) >= 15)
##HO##    #print("ohmy")
##HO##    year0 = date_time_obj.strftime("%Y")
##HO##    month0 = date_time_obj.strftime("%m")
##HO##    day0 = date_time_obj.strftime("%d")
##HO##    yearb2 = (date_time_obj -  datetime.timedelta(days=4)).strftime("%Y")
##HO##    monthb2 = (date_time_obj -  datetime.timedelta(days=4)).strftime("%m")
##HO##    dayb2 = (date_time_obj -  datetime.timedelta(days=4)).strftime("%d")
##HO##elif (hweektoday == 1) and (int("%d" % datetime.datetime.now().hour) >= 15): #如果是星期2的話
##HO##    #print("ohmyQQ")
##HO##    year0 = date_time_obj.strftime("%Y")
##HO##    month0 = date_time_obj.strftime("%m")
##HO##    day0 = date_time_obj.strftime("%d")
##HO##    yearb2 = (date_time_obj -  datetime.timedelta(days=4)).strftime("%Y")
##HO##    monthb2 = (date_time_obj -  datetime.timedelta(days=4)).strftime("%m")
##HO##    dayb2 = (date_time_obj -  datetime.timedelta(days=4)).strftime("%d")
##HO##else:
##HO##    #print(hweektoday == 0)
##HO##    #print(int("%d" % datetime.datetime.now().hour) > 15)
##HO##    #print(int("%d" % datetime.datetime.now().hour))
##HO##    #print("ohmyGG")
##HO##    year0 = date_time_obj.strftime("%Y")
##HO##    month0 = date_time_obj.strftime("%m")
##HO##    day0 = date_time_obj.strftime("%d")
##HO##    yearb2 = (date_time_obj -  datetime.timedelta(days=2)).strftime("%Y")
##HO##    monthb2 = (date_time_obj -  datetime.timedelta(days=2)).strftime("%m")
##HO##    dayb2 = (date_time_obj -  datetime.timedelta(days=2)).strftime("%d")
##HO##    #dtClosed = str(date_time_obj - datetime.timedelta(days = 1))

#print(dtClosed)
#print(type(day0))
#print(day0 == "19")

#for i in range(1,100):
#三大法人下載
#res = requests.get('http://www.taifex.com.tw/cht/3/futContractsDateDown?queryStartDate=2019%2F03%2F07&queryEndDate=2019%2F03%2F08&commodityId=TXF') 
#print(res)
#http://www.taifex.com.tw/cht/3/futContractsDateDown : 檢查元素-> network -> 按下載 -> 將滑鼠點到左欄的name "nlTotalTableDateDown"就可以看到該網址
#時間: 檢查元素 -> network -> Header -> Form Data (view parsed)
#url = "http://www.taifex.com.tw/cht/3/futContractsDateDown?queryStartDate=" + yearb2 + "%2F" + monthb2 + "%2F" + dayb2 + "&queryEndDate=" + year0 + "%2F" + month0 + "%2F" + day0 + "&commodityId=TXF"

#print((date_time_obj -  datetime.timedelta(days=j)).strftime("%d"))
print(date_time_obj)
#year0 = date_time_obj.strftime("%Y")
#month0 = date_time_obj.strftime("%m")
#day0 = date_time_obj.strftime("%d")
#year0 = (date_time_obj -  datetime.timedelta(days=0)).strftime("%Y")
#month0 = (date_time_obj -  datetime.timedelta(days=0)).strftime("%m")
#day0 = (date_time_obj -  datetime.timedelta(days=0)).strftime("%d")
#yearb2 = (date_time_obj -  datetime.timedelta(days=2)).strftime("%Y")
#monthb2 = (date_time_obj -  datetime.timedelta(days=2)).strftime("%m")
#dayb2 = (date_time_obj -  datetime.timedelta(days=2)).strftime("%d")

#year0 = "2019"
#month0 = "04"
#day0 = "13"
#yearb2 = "2019"
#monthb2 = "04"
#dayb2 = "11"

x=0
i=0
j=0
z=False

#z = is_downloadable('http://www.taifex.com.tw/cht/3/futContractsDateDown?queryStartDate=2019%2F03%2F07&queryEndDate=2019%2F03%2F08&commodityId=TXF') 
#z = is_downloadable('http://www.taifex.com.tw/cht/3/callsAndPutsDateDown?queryStartDate=2019%2F03%2F07&queryEndDate=2019%2F03%2F08&commodityId=TXO') 
#z = is_downloadable("http://www.taifex.com.tw/cht/3/callsAndPutsDateDown?queryStartDate=" + yearb2 + "%2F" + monthb2 + "%2F" + dayb2 + "&queryEndDate=" + year0 + "%2F" + month0 + "%2F" + day0 + "&commodityId=TXO")
#print(z==0)

while z==0:
    j+=1
    year0 = (date_time_obj -  datetime.timedelta(days=j-1)).strftime("%Y")
    month0 = (date_time_obj -  datetime.timedelta(days=j-1)).strftime("%m")
    day0 = (date_time_obj -  datetime.timedelta(days=j-1)).strftime("%d")
    yearb2 = year0
    monthb2 = month0
    dayb2 = day0
#    yearb2 = (date_time_obj -  datetime.timedelta(days=(2+j))).strftime("%Y")
#    monthb2 = (date_time_obj -  datetime.timedelta(days=(2+j))).strftime("%m")
#    dayb2 = (date_time_obj -  datetime.timedelta(days=(2+j))).strftime("%d")
    print(yearb2+monthb2+dayb2)
    print(year0+month0+day0)
    z = is_downloadable("http://www.taifex.com.tw/cht/3/callsAndPutsDateDown?queryStartDate=" + yearb2 + "%2F" + monthb2 + "%2F" + dayb2 + "&queryEndDate=" + year0 + "%2F" + month0 + "%2F" + day0 + "&commodityId=TXO")
#    time.sleep(1.5)
#    j+=1
#    print(j)
#    print(z)
#print(yearb2+monthb2+dayb2)
#print(year0+month0+day0)
 
##    print(year0)
##    print(month0)
##    print(day0)
##    print("test")
##
##
    while x<=17:
        #x+=6
        #i+=1
#        print(x)
#        print(i)
#        print(j)
        year0 = (date_time_obj -  datetime.timedelta(days=j-1)).strftime("%Y")
        month0 = (date_time_obj -  datetime.timedelta(days=j-1)).strftime("%m")
        day0 = (date_time_obj -  datetime.timedelta(days=j-1)).strftime("%d")
        yearb2 = (date_time_obj -  datetime.timedelta(days=(2+j-1+i))).strftime("%Y")
        monthb2 = (date_time_obj -  datetime.timedelta(days=(2+j-1+i))).strftime("%m")
        dayb2 = (date_time_obj -  datetime.timedelta(days=(2+j-1+i))).strftime("%d")
     
        url = "http://www.taifex.com.tw/cht/3/callsAndPutsDateDown?queryStartDate=" + yearb2 + "%2F" + monthb2 + "%2F" + dayb2 + "&queryEndDate=" + year0 + "%2F" + month0 + "%2F" + day0 + "&commodityId=TXO"
        time.sleep(1.5)
        #print(url)
        #print(is_downloadable('http://www.taifex.com.tw/cht/3/callsAndPutsDateDown?queryStartDate=" + yearb2 + "%2F" + monthb2 + "%2F" + dayb2 + "&queryEndDate=" + year0 + "%2F" + month0 + "%2F" + day0 + "&commodityId=TXO'))
        
        print(yearb2+monthb2+dayb2)
        print(year0+month0+day0)
        res = requests.get(url)
        #print(res.status_code)
        #print(res.headers)
        #print(res.text)
        time.sleep(1.5)
        f = open('export.csv', 'w+', encoding = 'UTF-8-sig')
        f.write(res.text)
        f.close()
        df = pd.read_csv("./export.csv")
        df.columns = ['date','1','2','3','4','5','6','7','8','9','bnum','bmoney','pnum','pmoney','totalnum','totalmoney']
        #print(df)
        x=len(df)
        #print(x)
        i+=1
        print("往抓一天資料")

################Predict Bro########################
#df=df['date']  #选择表格中的'w'、'z'列
#df=df.ix['date']  #选择表格中的'w'、'z'列
A=(df.ix[17,'bmoney']/df.ix[17,'bnum'])-(df.ix[14,'bmoney']/df.ix[14,'bnum'])  #选择表格中的'w'、'z'列
B=(df.ix[17,'pmoney']/df.ix[17,'pnum'])-(df.ix[14,'pmoney']/df.ix[14,'pnum'])  #选择表格中的'w'、'z'列
Ab1=(df.ix[11,'bmoney']/df.ix[11,'bnum'])-(df.ix[8,'bmoney']/df.ix[8,'bnum'])  #选择表格中的'w'、'z'列
Bb1=(df.ix[11,'pmoney']/df.ix[11,'pnum'])-(df.ix[8,'pmoney']/df.ix[8,'pnum'])  #选择表格中的'w'、'z'列
Ab2=(df.ix[5,'bmoney']/df.ix[5,'bnum'])-(df.ix[2,'bmoney']/df.ix[2,'bnum'])  #选择表格中的'w'、'z'列
Bb2=(df.ix[5,'pmoney']/df.ix[5,'pnum'])-(df.ix[2,'pmoney']/df.ix[2,'pnum'])  #选择表格中的'w'、'z'列
#print(A,B,Ab1,Bb1,Ab2,Bb2)
Abig=A-Ab1
Bbig=B-Bb1
Abigb1=Ab1-Ab2
Bbigb1=Bb1-Bb2
#print(Abig,Bbig,Abigb1,Bbigb1)
AAA=Abig-Abigb1
BBB=Bbig-Bbigb1
#print(AAA,BBB)
################ OP Ratio ########################
date2=df.ix[2,'date']
BCmoney2=df.ix[2,'bmoney']
BPmoney2=df.ix[5,'bmoney']
SCmoney2=df.ix[2,'pmoney']
SPmoney2=df.ix[5,'pmoney']
#Ratio_BPmoney2=round((BCmoney2-BPmoney2)/BPmoney2,2) #BC/CP only
Ratio_BPmoney2=round(((BCmoney2+SPmoney2)-(BPmoney2+SCmoney2))/(BCmoney2+SPmoney2),2)
date1=df.ix[8,'date']
BCmoney1=df.ix[8,'bmoney']
BPmoney1=df.ix[11,'bmoney']
SCmoney1=df.ix[8,'pmoney']
SPmoney1=df.ix[11,'pmoney']
#Ratio_BPmoney1=round((BCmoney1-BPmoney1)/BPmoney1,2)
Ratio_BPmoney1=round(((BCmoney1+SPmoney1)-(BPmoney1+SCmoney1))/(BCmoney1+SPmoney1),2)
date0=df.ix[14,'date']
BCmoney0=df.ix[14,'bmoney']
BPmoney0=df.ix[17,'bmoney']
SCmoney0=df.ix[14,'pmoney']
SPmoney0=df.ix[17,'pmoney']
#Ratio_BPmoney0=round((BCmoney0-BPmoney0)/BPmoney0,2)
Ratio_BPmoney0=round(((BCmoney0+SPmoney0)-(BPmoney0+SCmoney0))/(BCmoney0+SPmoney0),2)

#print(BCmoney0)
#print(SPmoney0)
#print(BPmoney0)
#print(SCmoney0)

#print(date2, Ratio_BPmoney2)
#print(date1, Ratio_BPmoney1)
#print(str(Ratio_BPmoney0))
#print(type(yearb2))
#print(type(date2))
#QQQ2 = (date2, Ratio_BPmoney2)
#QQQ1 = (date1, Ratio_BPmoney1)
#QQQ0 = (date0, Ratio_BPmoney0)

#print(type("Ratio_BPmoney0"))

#if (0 <= int("%d" % datetime.datetime.now().hour) < 15):
#print(hweektoday != 5)
#print(not(hweektoday != 5))
#print(not(hweektoday != 6))
#print(hweektoday != 6)
#print(0 <= int("%d" % datetime.datetime.now().hour) < 15)
#print((not(hweektoday != 5)) and (not(hweektoday != 6)) and (0 <= int("%d" % datetime.datetime.now().hour) < 15))

if ((not(hweektoday != 5)) and (not(hweektoday != 6)) and (0 <= int("%d" % datetime.datetime.now().hour) < 15)):
     Haha="預測哥15:00後再來吧！！！", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
elif x > 18:
     Haha="多抓了幾天資料喔！！！", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
elif BBB > AAA:
     #localtime = time.localtime(time.time())
     #Haha="預測哥:多" + str(datetime.datetime.now())
     #Haha="預測哥:多",yearb2+monthb2+dayb2,"To",year0+month0+day0, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
     #Haha="預測哥:多\n"+"資料區間:\n"+yearb2+monthb2+dayb2+"\n"+year0+month0+day0+"\n"+"現在時間:\n"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
     Haha="預測哥:多\n"+"資料區間:\n"+yearb2+monthb2+dayb2+"\n"+year0+month0+day0+"\n"+"OP買賣比:\n"+date2+" "+(str(Ratio_BPmoney2))+"\n"+date1+" "+(str(Ratio_BPmoney1))+"\n"+date0+" "+(str(Ratio_BPmoney0))+"\n"+"現在時間:\n"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

else:
     #print("預測哥:空")
     #Haha="預測哥:空\n"+"資料區間:\n"+yearb2+monthb2+dayb2+"\n"+year0+month0+day0+"\n"+"現在時間:\n"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
     Haha="預測哥:空\n"+"資料區間:\n"+yearb2+monthb2+dayb2+"\n"+year0+month0+day0+"\n"+"OP買賣比:\n"+date2+" "+(str(Ratio_BPmoney2))+"\n"+date1+" "+(str(Ratio_BPmoney1))+"\n"+date0+" "+(str(Ratio_BPmoney0))+"\n"+"現在時間:\n"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
     #Haha="預測哥:空", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) , yearb2+monthb2+dayb2+"~"+year0+month0+day0
 
print(Haha)

message = Haha
stickerID = 101
#picURL = 'https://pic.pimg.tw/hankmstar/1523605728-525076794.jpg'
#picURL = 'https://a.ksd-i.com/a/2018-12-22/112407-689013.jpg'
#picURL = 'https://image.cache.storm.mg/styles/smg-800x533-fp/s3/media/image/2019/10/07/20191007-041333_U17017_M556880_7846.jpg'
#picURL = 'https://assets.juksy.com/files/articles/93669/800x_100_w-5d59499306106.jpeg'
#picURL = 'https://menelect.imgix.net/wp-content/uploads/2019/10/The-Naked-Director-2-Jun-Amaki-Cover-1000-2.jpg'
#picURL = 'https://news.agentm.tw/wp-content/uploads/cover_news046-750x422.jpg'
picURL = 'https://i2.kknews.cc/SIG=398a9vi/1o800006q7o21nr6r25r.jpg'
#Token = "wy1a5c5dcFviz5eIrtGB6A0MNLmS2JcJ9Yqumu2PQtc"
#Token = "nNSnSuJ4PnQ2r91uahCQe9BNpAuW54FxTX7Vifpve2C"
Token = "57BOiBIqNEkCqx8fqmJYrkZ1qazBew9I54asNjluC1x"

def SendMessageToLineNotify(message, picurl):    
    url = "https://notify-api.line.me/api/notify"    
    payload1 = {'message':message}
    payload = {'message':message,
               'imageThumbnail':picurl,
               'imageFullsize':picurl,
#               'stickerPackageId':1,
#               'stickerId':stickerID
              }
    header = {'Content-Type':'application/x-www-form-urlencoded',
              'Authorization':'Bearer ' + Token
             }
    resp=requests.post(url, headers=header, data=payload)
    #print resp.text

def main():
    msg = message
    picurl = picURL
    SendMessageToLineNotify(msg, picurl)

if __name__ == '__main__':
    main()
