import time
import pytz
from decimal import *
import datetime
from csv import writer
import os
import pandas as pd
import urllib
from urllib.request import Request, urlopen
import bs4 as bs
import sys
ncount = 0
ma = range(0,5)
premkt = 'PreMarket'
csv = '.csv'
ndx = 'NDX'

totalprinted = 1

def iprint_goldmainpage():
    global totalprinted
    whiletruecount = 1
    ncount = 1
    programfilename1 = sys.argv[0]
    programfilename2 = programfilename1.split('/')
    programfilename = programfilename2[-1]
    unableprint = 0

    while True:
        def section1_cr8_main_premktfolder_path(input1):
            output1 = "C:/Users/malco/Desktop/Automation/{}".format(input1)
            mypath_input1 = output1
            print(mypath_input1)
            return mypath_input1

        def section2_cr8main_premktfolder(input2):
            if not os.path.exists(input2):
                os.makedirs(input2)

        def section3_create_fname_date(input3):
            fname8 = input3 + "/" + "{}".format(premktcsvus)
            return fname8

        def section4_create_fnamedate(fname):
            if not os.path.exists(fname):
                os.makedirs(fname)
                df = pd.DataFrame(columns=['date', 'price'])

        def section5_create_csvfname(input5):
            csvfname = input5 + str(today_dateus) + csv
            return csvfname

        def section6_create_csvdirname(input6, input7):
            csvdirname = input6 + '/' + '{}'.format(input7)
            return csvdirname

        def section10_create_csv_goodbadbuy(csvdirname, tick):
            if not os.path.exists(csvdirname):
                with open(csvdirname, 'a+', newline='') as csv:
                    csvwriter = writer(csv)
                    csvwriter.writerow(['Time', 'Price', 'Clock', 'ValChng', 'Percchng', 'Color of Chng',
                                        'Prev.Close', 'Open', 'DayRngWhole', 'DayRngStart', 'DayRngEnd',

                                        'TechSummary1', '5min1', '15min1', 'Hrly1', 'Daily1', 'Mthly1',
                                        'TechSummary2', '5min2', '15min2', 'Hrly2', 'Daily2', 'Mthly2',
                                        'TechSummary3', '5min3', '15min3', 'Hrly3', 'Daily3', 'Mthly3',

                                        'Pattern1', 'Timeframe1', 'Reliability1', 'Candles Ago1',
                                        'Pattern2', 'Timeframe2', 'Reliability2', 'Candles Ago2',
                                        'Pattern3', 'Timeframe3', 'Reliability3', 'Candles Ago3',
                                        'Pattern4', 'Timeframe4', 'Reliability4', 'Candles Ago4'])
            else:
                print('file exists:', csvdirname)
        today_dateus = str(datetime.datetime.now(tz=pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")).split()[0]
        premktcsvus = today_dateus

        gold = '2. Gold MainPage '
        goldmainpage0 = '2. Gold MainPage (Investingxcom)'
        goldmainpage1 = section1_cr8_main_premktfolder_path(goldmainpage0)
        section2_cr8main_premktfolder(goldmainpage1)    #Call function as : section2_cr8main_premktfolder(input2)
        fname1 = section3_create_fname_date(goldmainpage1)
        section4_create_fnamedate(fname1)
        csvfname1 = section5_create_csvfname(gold)
        csvdirname1 = section6_create_csvdirname(fname1, csvfname1)
        section10_create_csv_goodbadbuy(csvdirname1, gold)

        def section1_cr8_main_premktfolder_path(input1):
            output1 = "C:/Users/malco/Desktop/Automation/{}".format(input1)
            mypath_input1 = output1
            print(mypath_input1)
            return mypath_input1

        def section2_cr8main_premktfolder(input2):
            if not os.path.exists(input2):
                os.makedirs(input2)

        def section3_create_fname_date(input3):  # input 3 is mypath
            fname8 = input3 + "/" + "{}".format(premktcsvus)  # txt file
            return fname8

        def section4_create_fnamedate(fname):
            if not os.path.exists(fname):
                os.makedirs(fname)
                df = pd.DataFrame(columns=['date', 'price'])

        def section5_create_csvfname(input5):  # input 4 is ndx
            csvfname = input5 + str(today_dateus) + csv
            return csvfname

        def section6_create_csvdirname(input6, input7):  # input6 is fname
            csvdirname = input6 + '/' + '{}'.format(input7)
            return csvdirname


        def section10_create_csv_goodbadbuy(csvdirname, tick):
            if not os.path.exists(csvdirname):
                with open(csvdirname, 'a+', newline='') as csv:
                    csvwriter = writer(csv)
                    csvwriter.writerow(['Time', 'Price', 'Clock', 'ValChng', 'Percchng', 'Color of Chng',

                                        'Prev.Close', 'Open', 'DayRngWhole', 'DayRngStart', 'DayRngEnd',

                                        'TechSummary1', '5min1', '15min1', 'Hrly1', 'Daily1', 'Mthly1',
                                        'TechSummary2', '5min2', '15min2', 'Hrly2', 'Daily2', 'Mthly2',
                                        'TechSummary3', '5min3', '15min3', 'Hrly3', 'Daily3', 'Mthly3',

                                        'Pattern1', 'Timeframe1', 'Reliability1', 'Candles Ago1',
                                        'Pattern2', 'Timeframe2', 'Reliability2', 'Candles Ago2',
                                        'Pattern3', 'Timeframe3', 'Reliability3', 'Candles Ago3',
                                        'Pattern4', 'Timeframe4', 'Reliability4', 'Candles Ago4'])
            else:
                print('file exists:', csvdirname)
        today_dateus = str(datetime.datetime.now(tz=pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")).split()[0]
        premktcsvus = today_dateus

        gold = '2. Gold MainPage '
        goldmainpage0 = '2. Gold MainPage(Investingxcom)'
        goldmainpage1 = section1_cr8_main_premktfolder_path(goldmainpage0)
        section2_cr8main_premktfolder(goldmainpage1)    #Call function as : section2_cr8main_premktfolder(input2)
        fname1 = section3_create_fname_date(goldmainpage1)
        section4_create_fnamedate(fname1)
        csvfname1 = section5_create_csvfname(gold)
        csvdirname1 = section6_create_csvdirname(fname1, csvfname1)
        section10_create_csv_goodbadbuy(csvdirname1, gold)

        timeshort = str(datetime.datetime.now(tz=pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")).split()[1]
        timelongus = str(datetime.datetime.now(tz=pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")).split()
        timelongsg = str(datetime.datetime.now(tz = pytz.timezone('Asia/Singapore')).strftime("%Y-%m-%d %H:%M:%S")).split()

        print('                 ___________________________________RUNNING TIMELING________________________')
        print('                 Total Times Printed Since commencement of program:', totalprinted)
        totalprinted += 1
        print('                 whiletrue count', whiletruecount)
        print('                 US Time is:', timelongus)
        print('                 SG Time is:', timelongsg)
        print('                 Latest FileName is:', programfilename)
        print('                 Times unable to print:', unableprint)

        url = "https://www.investing.com/commodities/gold"
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            web_byte = urlopen(req).read()
            html_doc = web_byte.decode('utf-8')
            soup = bs.BeautifulSoup(html_doc, 'html.parser')
        except:
            unableprint +=1
            break
        whiletruecount += 1
        if whiletruecount % 10 != 0:
            with open(csvdirname1, 'a+', newline='') as csv1:
                csvwriter1 = writer(csv1)


                for all in soup.find_all('span'):
                    price = soup.find('span', class_="arial_26 inlineblock pid-8830-last").text
                    col1 = price.replace(',', '')
                #col2
                def col2():
                    for i in soup.find_all('div', class_="bottom lighterGrayFont arial_11"):
                        clock_scrap = i.find_all('span')[0]
                        clock_got = clock_scrap.get('class')[1]
                        clock = clock_got.split('Clock')[0]
                        return clock
                col2 = col2()
                #col3, 4
                for head in soup.find_all('div', class_="top bold inlineblock"):
                    ## Difference
                    col3 = head.find_all('span')[1].text
                    ## percenage change
                    col4 = head.find_all('span')[3].text

                #col5
                for head in soup.find_all('div', class_="top bold inlineblock"):
                    span = head.find_all('span')[1]
                    color = span.get('class')[1]
                    col5 = color.split('Font')[0]

                #col 6 to 10
                categorybox = soup.find_all('span', class_='float_lang_base_2 bold')
                col6 = categorybox[0].text.replace(',', '')
                col7 = categorybox[3].text.replace(',', '')

                ## col8,9,10: daysrange, daysrangeopen, daysrangeclose
                col8 = categorybox[6].text.replace(',', '') #days range
                col9 = col8.split()[0].replace(',', '') #daysrangeopen
                col10 = col8.split()[2].replace(',', '') #daysrangeclose

                #col11 to 28
                table = soup.find_all('table', class_='genTbl closedTbl technicalSummaryTbl')
                for table in soup.find_all('table', class_='genTbl closedTbl technicalSummaryTbl'):
                    col11 = table.find_all('td')[0].text  # Moving Average
                    col12 = table.find_all('td')[1].text  # col 11
                    col13 = table.find_all('td')[2].text
                    col14 = table.find_all('td')[3].text
                    col15 = table.find_all('td')[4].text
                    col16 = table.find_all('td')[5].text

                    col17 = table.find_all('td')[6].text  # Technical Indicator
                    col18 = table.find_all('td')[7].text
                    col19 = table.find_all('td')[8].text
                    col20 = table.find_all('td')[9].text
                    col21 = table.find_all('td')[10].text
                    col22 = table.find_all('td')[11].text

                    col23 = table.find_all('td')[12].text  # summary
                    col24 = table.find_all('td')[13].text
                    col25 = table.find_all('td')[14].text
                    col26 = table.find_all('td')[15].text
                    col27 = table.find_all('td')[16].text
                    col28 = table.find_all('td')[17].text  # col 28

                    #col 29
                for candlebox1 in soup.find_all('tr', id='row0'):  # candlestick pattern
                    pattern1 = candlebox1.find_all('td')[1].text
                    timeframe1 = candlebox1.find_all('td')[2].text
                    trc1 = candlebox1.find_all('td')[3]
                    reliability1 = trc1.get('title')
                    candlesago1 = candlebox1.find_all('td')[4].text

                for candlebox2 in soup.find_all('tr', id='row1'):  # candlestick pattern
                    pattern2 = candlebox2.find_all('td')[1].text
                    timeframe2 = candlebox2.find_all('td')[2].text
                    trc2 = candlebox2.find_all('td')[3]
                    reliability2 = trc2.get('title')
                    candlesago2 = candlebox2.find_all('td')[4].text

                for candlebox3 in soup.find_all('tr', id='row2'):  # candlestick pattern
                    pattern3 = candlebox3.find_all('td')[1].text
                    timeframe3 = candlebox3.find_all('td')[2].text
                    trc3 = candlebox3.find_all('td')[3]
                    reliability3 = trc3.get('title')
                    candlesago3 = candlebox3.find_all('td')[4].text

                for candlebox4 in soup.find_all('tr', id='row3'):  # candlestick pattern
                    pattern4 = candlebox4.find_all('td')[1].text
                    timeframe4 = candlebox4.find_all('td')[2].text
                    trc4 = candlebox4.find_all('td')[3]
                    reliability4 = trc4.get('title')
                    candlesago4 = candlebox4.find_all('td')[4].text

                csvwriter1.writerow([timeshort, col1, col2, col3,col4, col5,

                                     col6, col7, col8, col9, col10,

                                     col11, col12, col13, col14, col15, col16,
                                     col17,col18, col19, col20, col21, col22,
                                     col23,col24, col25, col26, col27, col28,

                                     pattern1, timeframe1, reliability1, candlesago1,
                                     pattern2, timeframe2, reliability2, candlesago2,
                                     pattern3, timeframe3, reliability3, candlesago3,
                                     pattern4, timeframe4, reliability4, candlesago4])
                print('__________________________________PRINTING DATA___________________________________')
                all_col = [timeshort, col1, col2, col3,col4, col5,
                                     col6, col7, col8, col9, col10,col11,
                                     col12, col13, col14, col15, col16, col17,
                                     col18, col19, col20, col21, col22, col23,
                                     col24, col25, col26, col27, col28,
                                     pattern1, timeframe1, reliability1, candlesago1,
                                     pattern2, timeframe2, reliability2, candlesago2,
                                     pattern3, timeframe3, reliability3, candlesago3,
                                     pattern4, timeframe4, reliability4, candlesago4]

                #                                     pattern5, timeframe5, reliability5, candlesago5
                all_col_names= ['Time', 'Price', 'Clock', 'ValChng', 'Percchng', 'Color of Chng',
                     'Prev.Close', 'Open', 'DayRngStart', 'DayRngEnd', 'DayRngWhole',
                     'TechSummary1', '5min1', '15min1', 'Hrly1', 'Daily1', 'Mthly1',
                     'TechSummary2', '5min2', '15min2', 'Hrly2', 'Daily2', 'Mthly2',
                     'TechSummary3', '5min3', '15min3', 'Hrly3', 'Daily3', 'Mthly3',
                     'Pattern1', 'Timeframe1', 'Reliability1', 'Candles Ago1',
                     'Pattern2', 'Timeframe2', 'Reliability2', 'Candles Ago2',
                     'Pattern3', 'Timeframe3', 'Reliability3', 'Candles Ago3',
                     'Pattern4', 'Timeframe4', 'Reliability4', 'Candles Ago4']

                all_col_count = 0
                for i in range(44):
                    print('col{} is: {}'.format(all_col_names[i], all_col[i]))

                time.sleep(1.5)
        else:
            csv1.close()
            print('closed file')
            break

while True:
    iprint_goldmainpage()