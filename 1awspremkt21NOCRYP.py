# output1 = "/home/ubuntu/AWS premkt/{}".format(input1)
import pytz
from decimal import *
from csv import writer
import bs4 as bs
# import requests
import pandas as pd
from decimal import *
import datetime
from urllib.request import Request, urlopen
import numpy as np
# import matplotlib.pyplot as plt
import os
import time
from urllib.request import Request, urlopen
import sys
premkt = 'PreMarket'
csv = '.csv'

num = range(0,2000)

totalprinted = 1
def iprint():
    global totalprinted
    whiletruecount = 1
    ncount = 1
    programfilename1 = sys.argv[0]
    programfilename2 = programfilename1.split('/')
    programfilename = programfilename2[-1]
    unableprint = 0
    while True:















        ######################################  THIS SECTION IS FOR AMAZON WEB SERVICES DEKSTOP#######################################
        ######################################  IF AWS UBHASH THIS SECTION ; SECTION AMAZONWEB SERVICE

        # SECTION: AMAZON WEB SERVICES

        today_dateus = str(datetime.datetime.now(tz=pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")).split()[0]
        premktcsvus = today_dateus
        snp500futures = '1. snp500futures'
        ndxfutures = '2. ndxfutures'
        dow30 = '3. dow30'
        snp500 = '4. snp500'
        ndx = '5. ndx'
        snp500vix = '6. snp500vix'
        usdollarindex = '7. usdollarindex'
        usa = '8. usa'
        headingforex = 'FOREX HEADING NOTHING HERE'
        eurusd = '9. EUR-USD'
        gbpusd = '10. GBP-USD'
        usdjpy = '11. USD-JPY'
        audusd = '12. AUD-USD'
        usdcad = '13. USD-CAD'
        eurjpy = '14. EUR-JPY'
        eurchf = '15. EUR-CHF'

        headingcommodities = 'COMODDITY HEADING NOTHING HERE'
        crudeoilwti = '16. Gold'
        brentoil = '17. Silver'
        natgas = '18. Copper'
        gold = '19. Crude Oil WTI'
        silver = '20. Brent Oil'
        copper = '21. Natural Gas'
        # cryp
        btc = '22. BTC'
        eth = '23. ETH'
        bch = '24. BCH'
        xrp = '25. LTC'
        ltc = '27. XRP'

        def section1_cr8_main_premktfolder_path(input1):
            output1 = "/home/ubuntu/1. AWS premkt/{}".format(input1)
            mypath_input1 = output1
            return mypath_input1

        def section2_cr8main_premktfolder(input2):
            if not os.path.exists(input2):
                os.makedirs(input2)

        def section5_create_csvfname(input5):  # input 4 is ndx
            csvfname = input5 + " " + str(today_dateus) + csv
            return csvfname

        def section6_create_csvdirname(input6, input7):  # input6 is fname
            csvdirname = input6 + '/' + '{}'.format(input7)
            return csvdirname

        def section9_create_csv(csvdirname, tick):
            if not os.path.exists(csvdirname):
                with open(csvdirname, 'a+', newline='') as csv:
                    # dfempty = pd.DataFrame(columns= col)
                    csvwriter = writer(csv)
                    csvwriter.writerow(["Time", "Price", 'Clock', 'ValChng', 'PercChng'])

        def section10_create_csv_goodbadbuy(csvdirname, tick):
            if not os.path.exists(csvdirname):
                with open(csvdirname, 'a+', newline='') as csv:
                    # dfempty = pd.DataFrame(columns= col)
                    csvwriter = writer(csv)
                    csvwriter.writerow(
                        ['Time', 'Price', 'Clock', 'ValChng', 'PercChng', 'GoodBad', 'MABuy', 'MASell', 'InctorBuy',
                         'InctorSell'])

        fname1 = section1_cr8_main_premktfolder_path(today_dateus)
        section2_cr8main_premktfolder(fname1)
        print(fname1)
        csvfname1 = section5_create_csvfname(snp500futures)
        csvfname2 = section5_create_csvfname(ndxfutures)
        csvfname3 = section5_create_csvfname(dow30)
        csvfname4 = section5_create_csvfname(snp500)
        csvfname5 = section5_create_csvfname(ndx)
        csvfname6 = section5_create_csvfname(snp500vix)
        csvfname7 = section5_create_csvfname(usdollarindex)

        csvfname9 = section5_create_csvfname(eurusd)
        csvfname10 = section5_create_csvfname(gbpusd)
        csvfname11 = section5_create_csvfname(usdjpy)
        csvfname12 = section5_create_csvfname(audusd)
        csvfname13 = section5_create_csvfname(usdcad)
        csvfname14 = section5_create_csvfname(eurjpy)
        csvfname15 = section5_create_csvfname(eurchf)

        csvfname16 = section5_create_csvfname(gold)
        csvfname17 = section5_create_csvfname(silver)
        csvfname18 = section5_create_csvfname(copper)
        csvfname19 = section5_create_csvfname(crudeoilwti)

        csvfname20 = section5_create_csvfname(brentoil)
        csvfname21 = section5_create_csvfname(natgas)

        # csvfname22 = section5_create_csvfname(btc)
        # csvfname23 = section5_create_csvfname(eth)
        # csvfname24 = section5_create_csvfname(bch)
        # csvfname25 = section5_create_csvfname(ltc)
        # csvfname27 = section5_create_csvfname(xrp)

        csvdirname1 = section6_create_csvdirname(fname1, csvfname1)
        csvdirname2 = section6_create_csvdirname(fname1, csvfname2)
        csvdirname3 = section6_create_csvdirname(fname1, csvfname3)
        csvdirname4 = section6_create_csvdirname(fname1, csvfname4)
        csvdirname5 = section6_create_csvdirname(fname1, csvfname5)
        csvdirname6 = section6_create_csvdirname(fname1, csvfname6)
        csvdirname7 = section6_create_csvdirname(fname1, csvfname7)
        csvdirname9 = section6_create_csvdirname(fname1, csvfname9)
        csvdirname10 = section6_create_csvdirname(fname1, csvfname10)
        csvdirname11 = section6_create_csvdirname(fname1, csvfname11)
        csvdirname12 = section6_create_csvdirname(fname1, csvfname12)
        csvdirname13 = section6_create_csvdirname(fname1, csvfname13)
        csvdirname14 = section6_create_csvdirname(fname1, csvfname14)
        csvdirname15 = section6_create_csvdirname(fname1, csvfname15)
        csvdirname16 = section6_create_csvdirname(fname1, csvfname16)
        csvdirname17 = section6_create_csvdirname(fname1, csvfname17)
        csvdirname18 = section6_create_csvdirname(fname1, csvfname18)
        csvdirname19 = section6_create_csvdirname(fname1, csvfname19)
        csvdirname20 = section6_create_csvdirname(fname1, csvfname20)
        csvdirname21 = section6_create_csvdirname(fname1, csvfname21)
        # csvdirname22 = section6_create_csvdirname(fname1, csvfname22)
        # csvdirname23 = section6_create_csvdirname(fname1, csvfname23)
        # csvdirname24 = section6_create_csvdirname(fname1, csvfname24)
        # csvdirname25 = section6_create_csvdirname(fname1, csvfname25)
        # csvdirname27 = section6_create_csvdirname(fname1, csvfname27)

        # Create CSV file, dont need to variable allocation
        section9_create_csv(csvdirname1, snp500futures)
        section9_create_csv(csvdirname2, ndxfutures)
        section9_create_csv(csvdirname3, dow30)
        section9_create_csv(csvdirname4, snp500)
        section9_create_csv(csvdirname5, ndx)
        section9_create_csv(csvdirname6, snp500vix)
        section9_create_csv(csvdirname7, usdollarindex)

        section10_create_csv_goodbadbuy(csvdirname9, eurusd)
        section10_create_csv_goodbadbuy(csvdirname10, gbpusd)
        section10_create_csv_goodbadbuy(csvdirname11, usdjpy)
        section10_create_csv_goodbadbuy(csvdirname12, audusd)
        section10_create_csv_goodbadbuy(csvdirname13, usdcad)
        section10_create_csv_goodbadbuy(csvdirname14, eurjpy)
        section10_create_csv_goodbadbuy(csvdirname15, eurchf)

        section9_create_csv(csvdirname16, gold)
        section9_create_csv(csvdirname17, silver)
        section9_create_csv(csvdirname18, copper)
        section9_create_csv(csvdirname19, crudeoilwti)
        section9_create_csv(csvdirname20, brentoil)
        section9_create_csv(csvdirname21, natgas)
        # section9_create_csv(csvdirname22, btc)
        # section9_create_csv(csvdirname23, eth)
        # section9_create_csv(csvdirname24, bch)
        # section9_create_csv(csvdirname25, ltc)
        # section9_create_csv(csvdirname27, xrp)


































        # # ######################################  THIS SECTION IS FOR MALCOLM'S DEKSTOP#######################################
        # # ######################################  IF MALCOLM'S DESKTOP UBHASH THIS SECTION ; SECTION MALCOLM'S DESKTOP
        # #
        # # # SECTION: MALCOLM'S DESKTOP
        # #
        #
        # def section1_cr8_main_premktfolder_path(input1):
        #     output1 = "C:/Users/malco/Desktop/Automation/1. premkt/{}".format(input1)
        #     mypath_input1 = output1
        #     return mypath_input1
        #
        # # note: input 2 is section1_cr8_main_premktfolder(usa)
        # def section2_cr8main_premktfolder(input2):
        #     if not os.path.exists(input2):
        #         os.makedirs(input2)
        #
        # # # SECTION 3: CREATE DATE
        # def section3_create_fname_date(input3):  # input 3 is mypath
        #     fname8 = input3 + "/" + "{}".format(premktcsvus)  # txt file
        #     return fname8
        #
        # def section4_create_fnamedate(fname):
        #     if not os.path.exists(fname):
        #         os.makedirs(fname)
        #
        # def section5_create_csvfname(input5):  # input 4 is ndx
        #     csvfname = input5 + " " +str(today_dateus) + csv
        #     return csvfname
        #
        # def section6_create_csvdirname(input6, input7):  # input6 is fname
        #     csvdirname = input6 + '/' + '{}'.format(input7)
        #     return csvdirname
        #
        # def section9_create_csv(csvdirname, tick):
        #     if not os.path.exists(csvdirname):
        #         with open(csvdirname, 'a+', newline='') as csv:
        #             # dfempty = pd.DataFrame(columns= col)
        #             csvwriter = writer(csv)
        #             csvwriter.writerow(["Time", "Price", 'Clock', 'ValChng', 'PercChng'])
        #
        # def section10_create_csv_goodbadbuy(csvdirname, tick):
        #     if not os.path.exists(csvdirname):
        #         with open(csvdirname, 'a+', newline='') as csv:
        #             # dfempty = pd.DataFrame(columns= col)
        #             csvwriter = writer(csv)
        #             csvwriter.writerow(
        #                 ['Time', 'Price', 'Clock', 'ValChng', 'PercChng', 'GoodBad', 'MABuy', 'MASell', 'InctorBuy',
        #                  'InctorSell'])
        #
        # #Create Files and csv
        # #creating file
        # snp500futures = '1. snp500futures'
        # ndxfutures = '2. ndxfutures'
        # dow30 = '3. dow30'
        # snp500 = '4. snp500'
        # ndx = '5. ndx'
        # snp500vix = '6. snp500vix'
        # usdollarindex = '7. usdollarindex'
        #
        # eurusd = '9. EUR-USD'
        # gbpusd = '10. GBP-USD'
        # usdjpy = '11. USD-JPY'
        # audusd = '12. AUD-USD'
        # usdcad = '13. USD-CAD'
        # eurjpy = '14. EUR-JPY'
        # eurchf = '15. EUR-CHF'
        #
        # headingcommodities = 'COMODDITY HEADING NOTHING HERE'
        # gold = '16. Gold'
        # silver = '17. Silver'
        # copper = '18. Copper'
        # crudeoilwti = '19. Crude Oil WTI'
        # brentoil = '20. Brent Oil'
        # natgas = '21. Natural Gas'
        # # cryp
        # btc = '22. BTC'
        # eth = '23. ETH'
        # bch = '24. BCH'
        # ltc = '25. LTC'
        # xrp = '27. XRP'
        #
        # today_dateus = str(datetime.datetime.now(tz=pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")).split()[0]
        # premktcsvus = today_dateus
        #                                                         #section 1
        # # INDICES
        # mypath_snp500futures = section1_cr8_main_premktfolder_path(snp500futures)
        # mypath_ndxfutures = section1_cr8_main_premktfolder_path(ndxfutures)
        # mypath_dow30 = section1_cr8_main_premktfolder_path(dow30)
        # mypath_snp500 = section1_cr8_main_premktfolder_path(snp500)
        # mypath_ndx = section1_cr8_main_premktfolder_path(ndx)
        # mypath_snp500vix = section1_cr8_main_premktfolder_path(snp500vix)
        # mypath_usdollarindex = section1_cr8_main_premktfolder_path(usdollarindex)
        #
        #
        # # FOREX
        # mypath_eurusd = section1_cr8_main_premktfolder_path(eurusd)
        # mypath_gbpusd = section1_cr8_main_premktfolder_path(gbpusd)
        # mypath_usdjpy = section1_cr8_main_premktfolder_path(usdjpy)
        # mypath_audusd = section1_cr8_main_premktfolder_path(audusd)
        # mypath_usdcad = section1_cr8_main_premktfolder_path(usdcad)
        # mypath_eurjpy = section1_cr8_main_premktfolder_path(eurjpy)
        # mypath_eurchf = section1_cr8_main_premktfolder_path(eurchf)
        #
        # # COMMDITIES
        # mypath_gold = section1_cr8_main_premktfolder_path(gold)
        # mypath_silver = section1_cr8_main_premktfolder_path(silver)
        # mypath_copper = section1_cr8_main_premktfolder_path(copper)
        # mypath_crudeoilwti = section1_cr8_main_premktfolder_path(crudeoilwti)
        # mypath_brentoil = section1_cr8_main_premktfolder_path(brentoil)
        # mypath_natgas = section1_cr8_main_premktfolder_path(natgas)
        # # CRYP
        # mypath_btc = section1_cr8_main_premktfolder_path(btc)
        # mypath_eth = section1_cr8_main_premktfolder_path(eth)
        # mypath_bch = section1_cr8_main_premktfolder_path(bch)
        # mypath_ltc = section1_cr8_main_premktfolder_path(ltc)
        # mypath_xrp = section1_cr8_main_premktfolder_path(xrp)
        #
        #                                                         # section 2
        #
        # # INDICES
        # section2_cr8main_premktfolder(mypath_snp500futures)  # Call function as : section2_cr8main_premktfolder(input2)
        # section2_cr8main_premktfolder(mypath_ndxfutures)
        # section2_cr8main_premktfolder(mypath_dow30)
        # section2_cr8main_premktfolder(mypath_snp500)
        # section2_cr8main_premktfolder(mypath_ndx)
        # section2_cr8main_premktfolder(mypath_snp500vix)
        # section2_cr8main_premktfolder(mypath_usdollarindex)
        #
        # # FOREX
        # section2_cr8main_premktfolder(mypath_eurusd)
        # section2_cr8main_premktfolder(mypath_gbpusd)
        # section2_cr8main_premktfolder(mypath_usdjpy)
        # section2_cr8main_premktfolder(mypath_audusd)
        # section2_cr8main_premktfolder(mypath_usdcad)
        # section2_cr8main_premktfolder(mypath_eurjpy)
        # section2_cr8main_premktfolder(mypath_eurchf)
        #
        # # COMMODITIES
        # section2_cr8main_premktfolder(mypath_gold)
        # section2_cr8main_premktfolder(mypath_silver)
        # section2_cr8main_premktfolder(mypath_copper)
        # section2_cr8main_premktfolder(mypath_crudeoilwti)
        # section2_cr8main_premktfolder(mypath_brentoil)
        # section2_cr8main_premktfolder(mypath_natgas)
        #
        # # cryp
        # section2_cr8main_premktfolder(mypath_btc)
        # section2_cr8main_premktfolder(mypath_eth)
        # section2_cr8main_premktfolder(mypath_bch)
        # section2_cr8main_premktfolder(mypath_ltc)
        # section2_cr8main_premktfolder(mypath_xrp)
        #
        #                                                             #section 3
        # fname1 = section3_create_fname_date(mypath_snp500futures)
        # fname2 = section3_create_fname_date(mypath_ndxfutures)
        # fname3 = section3_create_fname_date(mypath_dow30)
        # fname4 = section3_create_fname_date(mypath_snp500)
        # fname5 = section3_create_fname_date(mypath_ndx)
        # fname6 = section3_create_fname_date(mypath_snp500vix)
        # fname7 = section3_create_fname_date(mypath_usdollarindex)
        # # FOREX
        # fname9 = section3_create_fname_date(mypath_eurusd)
        # fname10 = section3_create_fname_date(mypath_gbpusd)
        # fname11 = section3_create_fname_date(mypath_usdjpy)
        # fname12 = section3_create_fname_date(mypath_audusd)
        # fname13 = section3_create_fname_date(mypath_usdcad)
        # fname14 = section3_create_fname_date(mypath_eurjpy)
        # fname15 = section3_create_fname_date(mypath_eurchf)
        #
        # # Cryp
        # fname16 = section3_create_fname_date(mypath_gold)
        # fname17 = section3_create_fname_date(mypath_silver)
        # fname18 = section3_create_fname_date(mypath_copper)
        # fname19 = section3_create_fname_date(mypath_crudeoilwti)
        # fname20 = section3_create_fname_date(mypath_brentoil)
        # fname21 = section3_create_fname_date(mypath_natgas)
        #
        # # cryp
        # fname22 = section3_create_fname_date(mypath_btc)
        # fname23 = section3_create_fname_date(mypath_eth)
        # fname24 = section3_create_fname_date(mypath_bch)
        # fname25 = section3_create_fname_date(mypath_ltc)
        # fname27 = section3_create_fname_date(mypath_xrp)
        #
        #                                                             # Section4 creates only file
        # section4_create_fnamedate(fname1)
        # section4_create_fnamedate(fname2)
        # section4_create_fnamedate(fname3)
        # section4_create_fnamedate(fname4)
        # section4_create_fnamedate(fname5)
        # section4_create_fnamedate(fname6)
        # section4_create_fnamedate(fname7)
        # section4_create_fnamedate(fname9)
        # section4_create_fnamedate(fname10)
        # section4_create_fnamedate(fname11)
        # section4_create_fnamedate(fname12)
        # section4_create_fnamedate(fname13)
        # section4_create_fnamedate(fname14)
        # section4_create_fnamedate(fname15)
        # section4_create_fnamedate(fname16)
        # section4_create_fnamedate(fname17)
        # section4_create_fnamedate(fname18)
        # section4_create_fnamedate(fname19)
        # section4_create_fnamedate(fname20)
        # section4_create_fnamedate(fname21)
        # section4_create_fnamedate(fname22)
        # section4_create_fnamedate(fname23)
        # section4_create_fnamedate(fname24)
        # section4_create_fnamedate(fname25)
        # section4_create_fnamedate(fname27)
        #                                                             #Section 5
        # csvfname1 = section5_create_csvfname(snp500futures)
        # csvfname2 = section5_create_csvfname(ndxfutures)
        # csvfname3 = section5_create_csvfname(dow30)
        # csvfname4 = section5_create_csvfname(snp500)
        # csvfname5 = section5_create_csvfname(ndx)
        # csvfname6 = section5_create_csvfname(snp500vix)
        # csvfname7 = section5_create_csvfname(usdollarindex)
        #
        # csvfname9 = section5_create_csvfname(eurusd)
        # csvfname10 = section5_create_csvfname(gbpusd)
        # csvfname11 = section5_create_csvfname(usdjpy)
        # csvfname12 = section5_create_csvfname(audusd)
        # csvfname13 = section5_create_csvfname(usdcad)
        # csvfname14 = section5_create_csvfname(eurjpy)
        # csvfname15 = section5_create_csvfname(eurchf)
        # # COMMOD
        # csvfname16 = section5_create_csvfname(gold)
        # csvfname17 = section5_create_csvfname(silver)
        # csvfname18 = section5_create_csvfname(copper)
        # csvfname19 = section5_create_csvfname(crudeoilwti)
        # csvfname20 = section5_create_csvfname(brentoil)
        # csvfname21 = section5_create_csvfname(natgas)
        # # CRYP
        # csvfname22 = section5_create_csvfname(btc)
        # csvfname23 = section5_create_csvfname(eth)
        # csvfname24 = section5_create_csvfname(bch)
        # csvfname25 = section5_create_csvfname(ltc)
        # csvfname27 = section5_create_csvfname(xrp)
        #                                                                           #Section6
        #
        # #
        # csvdirname1 = section6_create_csvdirname(fname1, csvfname1)
        # csvdirname2 = section6_create_csvdirname(fname2, csvfname2)
        # csvdirname3 = section6_create_csvdirname(fname3, csvfname3)
        # csvdirname4 = section6_create_csvdirname(fname4, csvfname4)
        # csvdirname5 = section6_create_csvdirname(fname5, csvfname5)
        # csvdirname6 = section6_create_csvdirname(fname6, csvfname6)
        # csvdirname7 = section6_create_csvdirname(fname7, csvfname7)
        #
        # csvdirname9 = section6_create_csvdirname(fname9, csvfname9)
        # csvdirname10 = section6_create_csvdirname(fname10, csvfname10)
        # csvdirname11 = section6_create_csvdirname(fname11, csvfname11)
        # csvdirname12 = section6_create_csvdirname(fname12, csvfname12)
        # csvdirname13 = section6_create_csvdirname(fname13, csvfname13)
        # csvdirname14 = section6_create_csvdirname(fname14, csvfname14)
        # csvdirname15 = section6_create_csvdirname(fname15, csvfname15)
        #
        # csvdirname16 = section6_create_csvdirname(fname16, csvfname16)
        # csvdirname17 = section6_create_csvdirname(fname17, csvfname17)
        # csvdirname18 = section6_create_csvdirname(fname18, csvfname18)
        # csvdirname19 = section6_create_csvdirname(fname19, csvfname19)
        # csvdirname20 = section6_create_csvdirname(fname20, csvfname20)
        # csvdirname21 = section6_create_csvdirname(fname21, csvfname21)
        #
        # csvdirname22 = section6_create_csvdirname(fname22, csvfname22)
        # csvdirname23 = section6_create_csvdirname(fname23, csvfname23)
        # csvdirname24 = section6_create_csvdirname(fname24, csvfname24)
        # csvdirname25 = section6_create_csvdirname(fname25, csvfname25)
        # csvdirname27 = section6_create_csvdirname(fname27, csvfname27)
        #                                                                     #section 9
        # # Create CSV file, dont need to variable allocation
        # section9_create_csv(csvdirname1, snp500futures)
        # section9_create_csv(csvdirname2, ndxfutures)
        # section9_create_csv(csvdirname3, dow30)
        # section9_create_csv(csvdirname4, snp500)
        # section9_create_csv(csvdirname5, ndx)
        # section9_create_csv(csvdirname6, snp500vix)
        # section9_create_csv(csvdirname7, usdollarindex)
        #
        # section10_create_csv_goodbadbuy(csvdirname9, eurusd)
        # section10_create_csv_goodbadbuy(csvdirname10, gbpusd)
        # section10_create_csv_goodbadbuy(csvdirname11, usdjpy)
        # section10_create_csv_goodbadbuy(csvdirname12, audusd)
        # section10_create_csv_goodbadbuy(csvdirname13, usdcad)
        # section10_create_csv_goodbadbuy(csvdirname14, eurjpy)
        # section10_create_csv_goodbadbuy(csvdirname15, eurchf)
        #
        # section9_create_csv(csvdirname16, gold)
        # section9_create_csv(csvdirname17, silver)
        # section9_create_csv(csvdirname18, copper)
        # section9_create_csv(csvdirname19, crudeoilwti)
        # section9_create_csv(csvdirname20, brentoil)
        # section9_create_csv(csvdirname21, natgas)
        #
        # section9_create_csv(csvdirname22, btc)
        # section9_create_csv(csvdirname23, eth)
        # section9_create_csv(csvdirname24, bch)
        # section9_create_csv(csvdirname25, ltc)
        # section9_create_csv(csvdirname27, xrp)





























                                                        #ALWAYS ON
        timeshort = str(datetime.datetime.now(tz=pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")).split()[1]
        timelongus = str(datetime.datetime.now(tz=pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")).split()
        timelongsg = str(datetime.datetime.now(tz = pytz.timezone('Asia/Singapore')).strftime("%Y-%m-%d %H:%M:%S")).split()
        print('\n\n')
        print('                 ___________________________________RUNNING TIMELING________________________')
        print('                 Total Times Printed Since commencement of program:', totalprinted)
        totalprinted += 1
        print('                 whiletrue count', whiletruecount)
        print('                 US Time is:',timelongus)
        print('                 SG Time is:',timelongsg)
        print('                 Latest FileName is:', programfilename)
        print('                 Times unable to print:', unableprint)


        #from CNBC
        url = "https://www.investing.com/equities/pre-market"
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            web_byte = urlopen(req).read()
            html_doc = web_byte.decode('utf-8')
            soup = bs.BeautifulSoup(html_doc, 'html.parser')
        except:
            unableprint +=1
            break
        whiletruecount += 1
        if whiletruecount % 10!=0:
        #1 snp500futures
            with open(csvdirname1,'a+', newline='') as csv1:
                csvwriter1 = writer(csv1)
                val1 = soup.find('td', class_="lastNum pid-8839-last").text
                val1 = val1.replace(',', '')
                val1 = Decimal(float(val1))  # note it doesnt change to decimal
                val1 = round(val1, 2)
                for i in soup.find_all('tr', pair="8839"):
                    # clock
                    got1 = i.find_all('span', id='sb_clock_8839')[0]
                    clock1 = got1.get('class')[0].split('Clock')[0]

                    ##change
                    change1 = i.find_all('td', id="sb_change_8839")[0].text

                    # percchange
                    perchange1 = i.find_all('td', id="sb_changepc_8839")[0].text

                    csvwriter1.writerow([timeshort, val1, clock1, change1, perchange1])



            # 2 ndxfutures
            with open(csvdirname2,'a+', newline='') as csv2:
                csvwriter2 = writer(csv2)
                val2 = soup.find('td', class_="lastNum pid-8874-last").text
                val2 = val2.replace(',', '')
                val2 = Decimal(float(val2))  # note it doesnt change to decimal
                val2 = round(val2, 2)
                # print('            ', val2)
                for i in soup.find_all('tr', pair="8874"):
                    # clock
                    got2 = i.find_all('span', id='sb_clock_8874')[0]
                    clock2 = got2.get('class')[0].split('Clock')[0]

                    ##change
                    change2 = i.find_all('td', id="sb_change_8874")[0].text

                    # percchange
                    perchange2 = i.find_all('td', id="sb_changepc_8874")[0].text

                    csvwriter2.writerow([timeshort, val2, clock2, change2, perchange2])


            # 3 dow30
            with open(csvdirname3,'a+', newline='') as csv3:
                csvwriter3 = writer(csv3)
                vala = soup.find('td', class_="lastNum pid-169-last").text
                vala = vala.replace(',', '')
                vala = Decimal(float(vala))  # note it doesnt change to decimal
                vala = round(vala, 2)
                # print('                        ', vala)
                for i in soup.find_all('tr', pair="169"):
                    # clock
                    got3 = i.find_all('span', id='sb_clock_169')[0]
                    clock3 = got3.get('class')[0].split('Clock')[0]

                    ##change
                    change3 = i.find_all('td', id="sb_change_169")[0].text

                    # percchange
                    perchange3 = i.find_all('td', id="sb_changepc_169")[0].text

                    csvwriter3.writerow([timeshort, vala, clock3, change3, perchange3])



            # 4 snp50
            with open(csvdirname4,'a+', newline='') as csv4:
                csvwriter4 = writer(csv4)
                val4 = soup.find('td', class_="lastNum pid-166-last").text
                val4 = val4.replace(',', '')
                val4 = Decimal(float(val4))  # note it doesnt change to decimal
                val4 = round(val4, 2)
                # print('                                    ', val4)
                for i in soup.find_all('tr', pair="166"):
                    # clock
                    got4 = i.find_all('span', id='sb_clock_166')[0]
                    clock4 = got4.get('class')[0].split('Clock')[0]

                    ##change
                    change4 = i.find_all('td', id="sb_change_166")[0].text

                    # percchange
                    perchange4 = i.find_all('td', id="sb_changepc_166")[0].text

                    csvwriter4.writerow([timeshort, val4, clock4, change4, perchange4])



            #5 ndx
            with open(csvdirname5,'a+', newline='') as csv5:
                csvwriter5 = writer(csv5)
                val5 = soup.find('td', class_='lastNum pid-14958-last').text
                val5 = val5.replace(',', '')
                val5 = Decimal(float(val5))  # note it doesnt change to decimal
                val5 = round(val5, 2)
                # print('                                            ', val5)
                for i in soup.find_all('tr', pair="14958"):
                    # clock
                    got5 = i.find_all('span', id='sb_clock_14958')[0]
                    clock5 = got5.get('class')[0].split('Clock')[0]

                    ##change
                    change5 = i.find_all('td', id="sb_change_14958")[0].text

                    # percchange
                    perchange5 = i.find_all('td', id="sb_changepc_14958")[0].text

                    csvwriter5.writerow([timeshort, val5, clock5, change5, perchange5])



            # 6 snp500vix
            with open(csvdirname6,'a+', newline='') as csv6:
                csvwriter6 = writer(csv6)
                val6 = soup.find('td', class_="lastNum pid-44336-last").text
                val6 = val6.replace(',', '')
                val6 = Decimal(float(val6))  # note it doesnt change to decimal
                val6 = round(val6, 2)
                # print('                                                    ', val6)
                for i in soup.find_all('tr', pair="44336"):
                    # clock
                    got6 = i.find_all('span', id='sb_clock_44336')[0]
                    clock6 = got6.get('class')[0].split('Clock')[0]

                    ##change
                    change6 = i.find_all('td', id="sb_change_44336")[0].text

                    # percchange
                    perchange6 = i.find_all('td', id="sb_changepc_44336")[0].text

                    csvwriter6.writerow([timeshort, val6, clock6, change6, perchange6])



            # 7 usdollarindex
            with open(csvdirname7,'a+', newline='') as csv7:

                csvwriter7 = writer(csv7)
                val7 = soup.find('td', class_="lastNum pid-8827-last").text
                val7 = val7.replace(',', '')
                val7 = Decimal(float(val7))  # note it doesnt change to decimal
                val7 = round(val7, 4)
                # print('                                                            ', val7)
                for i in soup.find_all('tr', pair="8827"):
                    # clock
                    got7 = i.find_all('span', id='sb_clock_8827')[0]
                    clock7 = got7.get('class')[0].split('Clock')[0]

                    ##change
                    change7 = i.find_all('td', id="sb_change_8827")[0].text

                    # percchange
                    perchange7 = i.find_all('td', id="sb_changepc_8827")[0].text

                    csvwriter7.writerow([timeshort, val7, clock7, change7, perchange7])


                ######################CURRENCIES
        # #9 EURUSD
        #
            tsb = soup.find_all('p', class_='float_lang_base_1 buyText')
            tss = soup.find_all('p', class_='float_lang_base_2 sellText')

            with open(csvdirname9,'a+', newline='') as csv9:
                csvwriter9 = writer(csv9)
                #val, goodbadbuy
                for row in soup.find_all('tr', id='TSB_pair_1'):
                    val9 = row.find_all('td')[3].text
                    goodbadbuy9 = row.find_all('td')[4].text

                #Summary
                mabuy1 = tsb[2].text.split('Buy ')[1]
                tibuy1 = tsb[3].text.split('Buy ')[1]
                masell1 = tss[2].text.split('Sell ')[1]
                tisell1 = tss[3].text.split('Sell ')[1]

                #valchange, perchange
                change9 = soup.find_all('span', id="TSB__summary_change_value_1")[0].text
                perchange9 = soup.find_all('span', id="TSB__summary_change_percent_1")[0].text

                #clock
                for i in soup.find_all('tr', id='TSB_pair_1'):
                    clock9 = i.find('span').get('class')[1].split('Clock')[0]

                csvwriter9.writerow([timeshort, val9, clock9,change9, perchange9, goodbadbuy9, mabuy1, masell1, tibuy1, tisell1])


            # #10 gbpusd
            with open(csvdirname10, 'a+', newline='') as csv10:
                csvwriter10 = writer(csv10)

                for row in soup.find_all('tr', id='TSB_pair_2'):
                    val10 = row.find_all('td')[3].text
                    goodbadbuy10 = row.find_all('td')[4].text

                #valchange, perchange
                change10 = soup.find_all('span', id="TSB__summary_change_value_2")[0].text
                perchange10 = soup.find_all('span', id="TSB__summary_change_percent_2")[0].text

                #Summary
                mabuy2 = tsb[4].text.split('Buy ')[1]
                tibuy2 = tsb[5].text.split('Buy ')[1]
                masell2 = tss[4].text.split('Sell ')[1]
                tisell2 = tss[5].text.split('Sell ')[1]

                for i in soup.find_all('tr', id='TSB_pair_2'):
                    clock10 = i.find('span').get('class')[1].split('Clock')[0]
                csvwriter10.writerow([timeshort, val10, clock10,change10, perchange10,  goodbadbuy10, mabuy2, masell2, tibuy2, tisell2])
      #
            # #11 usdjpy
            with open(csvdirname11, 'a+', newline='') as csv11:
                csvwriter11 = writer(csv11)

                for row in soup.find_all('tr', id='TSB_pair_3'):
                    val11 = row.find_all('td')[3].text
                    goodbadbuy11 = row.find_all('td')[4].text

                #valchange, perchange
                change11 = soup.find_all('span', id="TSB__summary_change_value_3")[0].text
                perchange11 = soup.find_all('span', id="TSB__summary_change_percent_3")[0].text

                #Summary
                mabuy3 = tsb[6].text.split('Buy ')[1]
                tibuy3 = tsb[7].text.split('Buy ')[1]
                masell3 = tss[6].text.split('Sell ')[1]
                tisell3 = tss[7].text.split('Sell ')[1]

                for i in soup.find_all('tr', id='TSB_pair_3'):
                    clock11 = i.find('span').get('class')[1].split('Clock')[0]
                csvwriter11.writerow([timeshort, val11, clock11,change11, perchange11,  goodbadbuy11, mabuy3, masell3, tibuy3, tisell3])
 #
            # #12 audusd
            with open(csvdirname12, 'a+', newline='') as csv12:
                csvwriter12 = writer(csv12)

                for row in soup.find_all('tr', id='TSB_pair_5'):
                    val12 = row.find_all('td')[3].text
                    goodbadbuy12 = row.find_all('td')[4].text

                # valchange, perchange
                change12 = soup.find_all('span', id="TSB__summary_change_value_5")[0].text
                perchange12 = soup.find_all('span', id="TSB__summary_change_percent_5")[0].text

                #Summary
                mabuy4 = tsb[8].text.split('Buy ')[1]
                tibuy4 = tsb[9].text.split('Buy ')[1]
                masell4 = tss[8].text.split('Sell ')[1]
                tisell4 = tss[9].text.split('Sell ')[1]

                for i in soup.find_all('tr', id='TSB_pair_5'):
                    clock12 = i.find('span').get('class')[1].split('Clock')[0]
                csvwriter12.writerow([timeshort, val12,clock12,change12, perchange12, goodbadbuy12, mabuy4, masell4, tibuy4, tisell4])

            # #13 usdcad
            with open(csvdirname13, 'a+', newline='') as csv13:
                csvwriter13 = writer(csv13)

                for row in soup.find_all('tr', id='TSB_pair_7'):
                    val13 = row.find_all('td')[3].text
                    goodbadbuy13 = row.find_all('td')[4].text

                #valchange, perchange
                change13 = soup.find_all('span', id="TSB__summary_change_value_7")[0].text
                perchange13 = soup.find_all('span', id="TSB__summary_change_percent_7")[0].text

                #Summary
                mabuy5 = tsb[10].text.split('Buy ')[1]
                tibuy5 = tsb[11].text.split('Buy ')[1]
                masell5 = tss[10].text.split('Sell ')[1]
                tisell5 = tss[11].text.split('Sell ')[1]
                for i in soup.find_all('tr', id='TSB_pair_7'):
                    clock13 = i.find('span').get('class')[1].split('Clock')[0]
                csvwriter13.writerow([timeshort, val13, clock13,change13, perchange13,   goodbadbuy13, mabuy5, masell5, tibuy5, tisell5])
   #
            #     #14 eurjpy
            with open(csvdirname14, 'a+', newline='') as csv14:
                csvwriter14 = writer(csv14)

                for row in soup.find_all('tr', id='TSB_pair_9'):
                    val14 = row.find_all('td')[3].text
                    goodbadbuy14 = row.find_all('td')[4].text

                #valchange, perchange
                change14 = soup.find_all('span', id="TSB__summary_change_value_9")[0].text
                perchange14 = soup.find_all('span', id="TSB__summary_change_percent_9")[0].text

                #Summary
                mabuy6 = tsb[12].text.split('Buy ')[1]
                tibuy6 = tsb[13].text.split('Buy ')[1]
                masell6 = tss[12].text.split('Sell ')[1]
                tisell6 = tss[13].text.split('Sell ')[1]
                for i in soup.find_all('tr', id='TSB_pair_9'):
                    clock14 = i.find('span').get('class')[1].split('Clock')[0]
                csvwriter14.writerow([timeshort, val14, clock14,change14, perchange14,  goodbadbuy14, mabuy6, masell6, tibuy6, tisell6])
    #
            #     # 15eurchf
            with open(csvdirname15, 'a+', newline='') as csv15:
                csvwriter15 = writer(csv15)

                for row in soup.find_all('tr', id='TSB_pair_10'):
                    val15 = row.find_all('td')[3].text
                    goodbadbuy15 = row.find_all('td')[4].text

                #valchange, perchange
                change15 = soup.find_all('span', id="TSB__summary_change_value_10")[0].text
                perchange15 = soup.find_all('span', id="TSB__summary_change_percent_10")[0].text

                #Summary
                mabuy7 = tsb[14].text.split('Buy ')[1]
                tibuy7 = tsb[15].text.split('Buy ')[1]
                masell7 = tss[14].text.split('Sell ')[1]
                tisell7 = tss[15].text.split('Sell ')[1]

                for i in soup.find_all('tr', id='TSB_pair_10'):
                    clock15 = i.find('span').get('class')[1].split('Clock')[0]
                csvwriter15.writerow([timeshort, val15,clock15,change15, perchange15, goodbadbuy15, mabuy7, masell7, tibuy7, tisell7])









            # ####################################################################################COMMODITIES?
        #
        #
        #
        #
        #16 gold
            with open(csvdirname16,'a+', newline='') as csv16:
                csvwriter16 = writer(csv16)
                val3 = soup.find('td', class_="lastNum pid-8830-last").text
                val3 = val3.replace(',', '')
                val3 = Decimal(float(val3))  # note it doesnt change to decimal
                val16 = round(val3, 2)
                # print('', val1)

                #valchng, perchange
                change16 = soup.find('td', id="sb_change_8830").text
                perchange16 = soup.find('td', id="sb_changepc_8830").text
                #clock
                for i in soup.find_all('span', id='sb_clock_8830'):
                    clock16 = i.get('class')[0].split('Clock')[0]
                csvwriter16.writerow([timeshort, val16, clock16, change16, perchange16])
        #17 silver
            with open(csvdirname17,'a+', newline='') as csv17:
                csvwriter17 = writer(csv17)
                val3 = soup.find('td', class_= "lastNum pid-8836-last").text
                val3 = val3.replace(',', '')
                val3 = Decimal(float(val3))  # note it doesnt change to decimal
                val17 = round(val3, 3)
                # print('', val1)

                #valchng, perchange
                change17 = soup.find('td', id="sb_change_8836").text
                perchange17 = soup.find('td', id="sb_changepc_8836").text

                for i in soup.find_all('span', id='sb_clock_8836'):
                    clock17 = i.get('class')[0].split('Clock')[0]
                csvwriter17.writerow([timeshort, val17, clock17, change17, perchange17])
        #18 copper
            with open(csvdirname18,'a+', newline='') as csv18:
                csvwriter18 = writer(csv18)
                val3 = soup.find('td', class_="lastNum pid-8831-last").text
                val3 = val3.replace(',', '')
                val3 = Decimal(float(val3))  # note it doesnt change to decimal
                val18 = round(val3, 3)
                # print('', val1)

                #valchng, perchange
                change18 = soup.find('td', id="sb_change_8831").text
                perchange18 = soup.find('td', id="sb_changepc_8831").text

                for i in soup.find_all('span', id='sb_clock_8831'):
                    clock18 = i.get('class')[0].split('Clock')[0]
                csvwriter18.writerow([timeshort, val18, clock18, change18, perchange18])
        #19 crude oil wti
            with open(csvdirname19,'a+', newline='') as csv19:
                csvwriter19 = writer(csv19)
                val3 = soup.find('td', class_="lastNum pid-8849-last").text
                val3 = val3.replace(',', '')
                val3 = Decimal(float(val3))  # note it doesnt change to decimal
                val19 = round(val3, 2)
                # print('', val1)

                #valchng, perchange
                change19 = soup.find('td', id="sb_change_8849").text
                perchange19 = soup.find('td', id="sb_changepc_8849").text

                for i in soup.find_all('span', id='sb_clock_8849'):
                    clock19 = i.get('class')[0].split('Clock')[0]
                csvwriter19.writerow([timeshort, val19, clock19, change19, perchange19])
        #20 brent oil
            with open(csvdirname20,'a+', newline='') as csv20:
                csvwriter20 = writer(csv20)
                val3 = soup.find('td', class_ ="lastNum pid-8833-last").text
                val3 = val3.replace(',', '')
                val3 = Decimal(float(val3))  # note it doesnt change to decimal
                val20 = round(val3, 2)
                # print('', val1)

                #valchng, perchange
                change20 = soup.find('td', id="sb_change_8833").text
                perchange20 = soup.find('td', id="sb_changepc_8833").text

                for i in soup.find_all('span', id='sb_clock_8833'):
                    clock20 = i.get('class')[0].split('Clock')[0]
                csvwriter20.writerow([timeshort, val20, clock20, change20, perchange20])
        # 21 natgas
            with open(csvdirname21,'a+', newline='') as csv21:
                csvwriter21 = writer(csv21)
                val3 = soup.find('td', class_ ="lastNum pid-8862-last").text
                val3 = val3.replace(',', '')
                val3 = Decimal(float(val3))  # note it doesnt change to decimal
                val21 = round(val3, 3)
                # print('', val1)

                #valchng, perchange
                change21 = soup.find('td', id="sb_change_8862").text
                perchange21 = soup.find('td', id="sb_changepc_8862").text

                for i in soup.find_all('span', id='sb_clock_8862'):
                    clock21 = i.get('class')[0].split('Clock')[0]
                csvwriter21.writerow([timeshort, val21, clock21, change21, perchange21])



    ############cryp
            #BTC 22
            # with open(csvdirname22, 'a+', newline='') as csv22:
            #     csvwriter22 = writer(csv22)
            #     val22 = soup.find('td', id='sb_last_945629').text
            #     change22 = soup.find('td', id='sb_change_945629').text
            #     perchange22 = soup.find('td', id='sb_changepc_945629').text
            #     clock22 = soup.find('span', id='sb_clock_945629').get('class')[0].split('Clock')[0]
            #     csvwriter22.writerow([timeshort, val22, clock22, change22, perchange22])

            # #ETH 23
            # with open(csvdirname23, 'a+', newline='') as csv23:
            #     csvwriter23 = writer(csv23)
            #     val23 = soup.find('td', id='sb_last_997650').text
            #     change23 = soup.find('td', id='sb_change_997650').text
            #     perchange23 = soup.find('td', id='sb_changepc_997650').text
            #     clock23 = soup.find('span', id='sb_clock_997650').get('class')[0].split('Clock')[0]
            #     csvwriter23.writerow([timeshort, val23, clock23, change23, perchange23])
            #
            # # BCH 24
            # with open(csvdirname24, 'a+', newline='') as csv24:
            #     csvwriter24 = writer(csv24)
            #     val24 = soup.find('td', id='sb_last_1058255').text
            #     change24 = soup.find('td', id='sb_change_1058255').text
            #     perchange24 = soup.find('td', id='sb_changepc_1058255').text
            #     clock24 = soup.find('span', id='sb_clock_1058255').get('class')[0].split('Clock')[0]
            #     csvwriter24.writerow([timeshort, val24, clock24, change24, perchange24])
            #
            # # LTC 25
            # with open(csvdirname25, 'a+', newline='') as csv25:
            #     csvwriter25 = writer(csv25)
            #     val25 = soup.find('td', id='sb_last_1010798').text
            #     change25 = soup.find('td', id='sb_change_1010798').text
            #     perchange25 = soup.find('td', id='sb_changepc_1010798').text
            #     clock25 = soup.find('span', id='sb_clock_1010798').get('class')[0].split('Clock')[0]
            #     csvwriter25.writerow([timeshort, val25, clock25, change25, perchange25])
            #
            #
            # # XRP 27
            # with open(csvdirname27, 'a+', newline='') as csv27:
            #     csvwriter27 = writer(csv27)
            #     val27 = soup.find('td', id='sb_last_1010782').text
            #     change27 = soup.find('td', id='sb_change_1010782').text
            #     perchange27 = soup.find('td', id='sb_changepc_1010782').text
            #     clock27 = soup.find('span', id='sb_clock_1010782').get('class')[0].split('Clock')[0]
            #     csvwriter27.writerow([timeshort, val27, clock27, change27, perchange27])


        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #

            print('_____________________________________INDICES________________________')

            print('\n\n')
            print('S&P500Future,          Nasdaq Futures        Dow 30                 S&P500                Nasdaq                  S&P500 Futures          Dollar Index')
            print(val1,clock1,'        ', val2,clock2,'       ', vala,clock3,'         ', val4,clock4,'         ', val5,clock5,'           ', val6,clock6,'              ', val7,clock7)
            print(change1, perchange1, '        ', change2, perchange2, '       ', change3, perchange3, '      ', change4, perchange4, '        ', change5, perchange5,'       ', change6, perchange6, '         ', change7, perchange7)

            print('\n\n')

            # print('EUR-USD      GBP-USD        USD-JPY       AUD-USD          USD-CAD            EUR-JPY      EUR-CHF')
            # print(val9, clock9, '   ', val10, clock10, '     ', val11, clock11, '    ', val12, clock12, '      ', val13, clock13, '        ', val14, clock14, '      ', val15, clock15)
            print('____________________________________CURRENCIES________________________')

            print('Currency  Price  Clock ValChng PerChng GoodBadBuy MABuy/Sell, TIBuy/Sell','\n',
            'EUR-USD:', val9,clock9,change9,perchange9, goodbadbuy9, mabuy1, masell1, tibuy1, tisell1,'\n',
            'GBP-USD:', val10, clock10, change10, perchange10, goodbadbuy10, mabuy2, masell2, tibuy2, tisell2,'\n',
            'USD-JPY:', val11, clock11, change11, perchange11, goodbadbuy11, mabuy3, masell3, tibuy3, tisell3,'\n',
            'AUD-USD:', val12, clock12, change12, perchange12, goodbadbuy12, mabuy4, masell4, tibuy4, tisell4,'\n',
            'USD-CAD:', val13, clock13, change13, perchange13, goodbadbuy13, mabuy5, masell5, tibuy5, tisell5,'\n',
            'EUR-JPY:', val14, clock14, change14, perchange14, goodbadbuy14, mabuy6, masell6, tibuy6, tisell6,'\n',
            'EUR-CHF:', val15, clock15, change15, perchange15, goodbadbuy15, mabuy7, masell7, tibuy7, tisell7)

            print('\n\n')

            print('___________________________________COMMODITIES________________________')
            print(' Commod.','Price','Clock','ValChng', 'PerChng' ,'\n'
                ' Gold:', val16, clock16, change16, perchange16 ,'\n',
                  'Silver:', val17, clock17, change17, perchange17,'\n',
                  'Copper:', val18, clock18, change18, perchange18,'\n',
                  'CrudeWTI:', val19, clock19, change19, perchange19,'\n',
                  'Brent:', val20, clock20, change20, perchange20,'\n',
                  'NatGas', val21, clock21, change21, perchange21)

            print('\n\n')
            print('___________________________________CRYPTOXCIES________________________')

            # print(' Cryp', 'Price','Clock', 'ValChng', 'PerChng','\n',
            #     'BTC',val22, clock22, change22, perchange22,'\n',
            #     'ETH',val23, clock23, change23, perchange23,'\n',
            #     'BCH',val24, clock24, change24, perchange24,'\n',
            #     'LTC',val25, clock25, change25, perchange25, '\n',
            #     'XRP',val27, clock27, change27, perchange27)

            time.sleep(1.5)#note if 1s, v numbers keep repeating for some reason
                            #note that might not want to get from investing cos im not getting straight from exzchange
                            #look at the numbers again. maybe try to keep track of the price changes as compared to investing.com
                            #note that price different cos maybe it shows different number but actual price is different, maybe got from another server. Prob might want to get price from different page. like Nasdaq or NYSe
            #### backtest model ; backtest VAR#

            #note the max number of excel is Approx 1900, henceill make another folder when count = 1500 to 1700


        else:
            csv1.close()
            csv2.close()
            csv3.close()
            csv4.close()
            csv5.close()
            csv6.close()
            csv7.close()

            csv9.close()
            csv10.close()
            csv11.close()
            csv12.close()
            csv13.close()
            csv14.close()
            csv15.close()
            csv16.close()
            csv17.close()
            csv18.close()
            csv19.close()
            csv20.close()
            csv21.close()
            # csv22.close()


            print('broken and closed file')
            # csv8.close()

            break
while True:
    iprint()